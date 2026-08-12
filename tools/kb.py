#!/usr/bin/env python3
"""Low-token retrieval CLI derived entirely from the knowledge base Markdown."""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import re
import sys
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CORE_DOCUMENTS = ("META.md", "SUMMARY.md", "REUSE_GUIDE.md", "ARCHITECTURE.md", "STATUS.md")
ALIASES = {
    "long-running-agent": ("长期后台 agent", "后台 agent", "background agent", "background task", "后台任务", "long-running task", "persistent task", "daemon"),
    "subagent": ("子 agent", "sub-agent", "child agent", "agent-to-agent"),
    "system-proxy": ("系统代理", "system proxy", "network proxy", "网络代理"),
    "browser-renderer": ("浏览器渲染", "browser rendering", "browser renderer", "rendering engine", "渲染模块"),
    "agent-skills": ("agent skills", "agent skill", "skills 选型", "技能选型"),
    "scheduler": ("定时任务", "scheduled task", "scheduler", "cron", "heartbeat"),
    "rag": ("rag", "retrieval augmented generation", "检索增强"),
    "bot": ("qq bot", "chat bot", "聊天机器人", "机器人"),
}
ALIAS_TERMS = frozenset(ALIASES) | frozenset(term for variants in ALIASES.values() for term in variants)
ROUTE_NEGATIVE = (
    "错别字", "typo", "润色", "format", "格式化", "重命名", "rename", "分号",
    "semicolon", "移动按钮", "move button", "解释这", "explain these", "null pointer",
    "空指针", "already specified", "已明确指定",
)
ROUTE_POSITIVE = (
    "新功能", "系统设计", "架构", "architecture", "技术选型", "选型", "framework",
    "框架", "集成", "integration", "实现一个", "设计一个", "agent", "rag", "mcp",
    "浏览器", "browser", "代理", "proxy", "自动化", "automation", "数据库", "database",
    "bot", "devtools", "后台任务", "长期运行", "定时任务", "scheduler", "比较方案",
)


class KBError(Exception):
    pass


@dataclass
class Project:
    slug: str
    directory: Path
    meta: dict[str, object]

    def document(self, name: str) -> Path:
        return self.directory / name


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        raise KBError(f"Cannot read {path.relative_to(ROOT)}: {exc}") from exc


def parse_scalar(value: str) -> object:
    value = value.strip()
    if value.startswith("[") and value.endswith("]"):
        try:
            return json.loads(value)
        except json.JSONDecodeError:
            return [item.strip().strip('"\'') for item in value[1:-1].split(",") if item.strip()]
    return value.strip('"\'')


def parse_front_matter(text: str) -> dict[str, object]:
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---", 4)
    if end < 0:
        return {}
    result: dict[str, object] = {}
    for line in text[4:end].splitlines():
        if ":" not in line or line.startswith((" ", "\t", "#")):
            continue
        key, value = line.split(":", 1)
        result[key.strip()] = parse_scalar(value)
    return result


def discover_projects() -> list[Project]:
    projects = []
    for meta_path in sorted(ROOT.glob("*/*/META.md")):
        meta = parse_front_matter(read_text(meta_path))
        projects.append(Project(meta_path.parent.name, meta_path.parent, meta))
    if not projects:
        raise KBError("No projects found. Expected <domain>/<project>/META.md files.")
    return projects


def get_project(name: str) -> Project:
    normalized = name.casefold().strip()
    matches = [p for p in discover_projects() if p.slug.casefold() == normalized]
    if not matches:
        available = ", ".join(p.slug for p in discover_projects())
        raise KBError(f"Unknown project '{name}'. Available: {available}")
    return matches[0]


def normalize_terms(query: str) -> list[str]:
    lowered = query.casefold().strip()
    terms = set(re.findall(r"[a-z0-9][a-z0-9+.#-]*|[\u4e00-\u9fff]{2,}", lowered))
    for canonical, variants in ALIASES.items():
        if canonical in lowered or any(variant in lowered for variant in variants):
            terms.add(canonical)
            terms.update(variants)
    for term in tuple(terms):
        if re.fullmatch(r"[a-z]{6,}ing", term):
            terms.add(term[:-3])
    return sorted(term for term in terms if len(term) > 1)


def project_corpus(project: Project) -> str:
    parts = [project.slug, json.dumps(project.meta, ensure_ascii=False)]
    for name in CORE_DOCUMENTS:
        path = project.document(name)
        if path.exists():
            parts.append(read_text(path))
    return "\n".join(parts).casefold()


def match_score(corpus: str, terms: list[str]) -> tuple[int, list[str]]:
    matched = []
    score = 0
    for term in terms:
        count = corpus.count(term.casefold())
        if count:
            matched.append(term)
            score += 5 if term in ALIAS_TERMS else min(count, 3)
    return score, matched


def relative(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def compact(value: object, fallback: str = "Unknown / Needs Verification") -> str:
    if value in (None, "", []):
        return fallback
    if isinstance(value, list):
        return ", ".join(str(item) for item in value)
    return str(value)


def split_sections(text: str) -> list[tuple[str, str]]:
    matches = list(re.finditer(r"(?m)^# (.+?)\s*$", text))
    sections = []
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        sections.append((match.group(1).strip(), text[match.end():end].strip()))
    return sections


def select_sections(path: Path, query: str, maximum: int, fallback_titles: tuple[str, ...] = ()) -> list[tuple[str, str]]:
    sections = split_sections(read_text(path))
    terms = normalize_terms(query)
    ranked = []
    for order, (title, body) in enumerate(sections):
        title_score, _ = match_score(title.casefold(), terms)
        body_score, _ = match_score(body.casefold(), terms)
        score = title_score * 3 + body_score
        if title in fallback_titles:
            score += 2
        ranked.append((score, -order, title, body))
    positive = [item for item in sorted(ranked, reverse=True) if item[0] > 0]
    chosen = positive[:maximum] if positive else sorted(ranked, key=lambda item: -item[1])[:1]
    return [(title, body) for _, _, title, body in chosen]


def trim(text: str, limit: int) -> str:
    if len(text) <= limit:
        return text.rstrip()
    shortened = text[:limit].rsplit("\n", 1)[0].rstrip()
    return shortened + "\n\n[Output limited; refine the capability to retrieve a narrower section.]"


def command_search(args: argparse.Namespace) -> int:
    terms = normalize_terms(args.query)
    if not terms:
        raise KBError("Search query must contain a capability or technical keyword.")
    ranked = []
    for project in discover_projects():
        score, matched = match_score(project_corpus(project), terms)
        if score:
            ranked.append((score, project, matched))
    ranked.sort(key=lambda item: (-item[0], item[1].slug))
    if not ranked or ranked[0][0] < 10:
        print("No high-relevance local result. Stop KB retrieval and continue the task normally; use external research only if justified.")
        log_usage(args, terms, [], False)
        return 0
    candidates = [item for item in ranked if item[0] >= 5][:3]
    for index, (score, project, matched) in enumerate(candidates, 1):
        relevance = "HIGH" if score >= 10 else "MEDIUM"
        why = ", ".join(matched[:6])
        print(f"[{index}] {project.slug}\nRelevance: {relevance}\nWhy: matched {why}")
        print(f'Recommended next action: python tools/kb.py reuse {project.slug} "{args.query}"')
        print("Source dive: NOT NEEDED YET\n")
    log_usage(args, terms, [item[1].slug for item in candidates], False)
    return 0


def command_show(args: argparse.Namespace) -> int:
    project = get_project(args.project)
    path = project.document("SUMMARY.md")
    wanted = {"一句话说明", "30 秒快速判断"}
    sections = [(title, body) for title, body in split_sections(read_text(path)) if title in wanted]
    if not sections:
        sections = split_sections(read_text(path))[:2]
    output = "\n\n".join(f"# {title}\n\n{body}" for title, body in sections)
    print(trim(output, 1400))
    return 0


def command_extract(args: argparse.Namespace, filename: str, limit: int) -> int:
    if not args.capability.strip():
        raise KBError("Capability cannot be empty.")
    project = get_project(args.project)
    path = project.document(filename)
    if not path.exists():
        raise KBError(f"{project.slug} has no {filename}. Use 'reuse' or 'path' instead.")
    sections = select_sections(path, args.capability, 1)
    output = "\n\n".join(f"# {title}\n\n{body}" for title, body in sections)
    print(trim(output, limit))
    return 0


def command_path(args: argparse.Namespace) -> int:
    project = get_project(args.project)
    print(f"Project: {project.slug}")
    for name in CORE_DOCUMENTS:
        path = project.document(name)
        if path.exists():
            print(f"{name}: {path}")
    print(f"source: {project.directory / 'source'} (local, ignored, read only when justified)")
    return 0


def command_status(args: argparse.Namespace) -> int:
    project = get_project(args.project)
    status_path = project.document("STATUS.md")
    status_sections = split_sections(read_text(status_path))
    overview = status_sections[0][1] if status_sections else "Unknown / Needs Verification"
    print(f"Project: {project.slug}")
    print(f"Status: {trim(overview, 650)}")
    print(f"Analyzed commit: {compact(project.meta.get('analyzed_commit'))}")
    print(f"Analysis date: {compact(project.meta.get('analysis_date'))}")
    print(f"License: {compact(project.meta.get('license'))}")
    print(f"Main languages: {compact(project.meta.get('main_languages'))}")
    return 0


def should_query(task: str) -> tuple[bool, str]:
    lowered = task.casefold().strip()
    if not lowered:
        raise KBError("Task text cannot be empty.")
    negative = next((phrase for phrase in ROUTE_NEGATIVE if phrase in lowered), None)
    if negative:
        return False, f"localized/simple-task signal: {negative}"
    positive = next((phrase for phrase in ROUTE_POSITIVE if phrase in lowered), None)
    if positive:
        return True, f"reusable/system-design signal: {positive}"
    return False, "no strong reusable-capability signal"


def command_route(args: argparse.Namespace) -> int:
    decision, reason = should_query(args.task)
    print(f"Decision: {'QUERY' if decision else 'SKIP'}")
    print(f"Reason: {reason}")
    if decision:
        print(f'Recommended next action: python tools/kb.py search "{args.task}"')
    return 0


def log_usage(args: argparse.Namespace, terms: list[str], projects: list[str], deepened: bool) -> None:
    if os.environ.get("KB_USAGE_LOG") != "1":
        return
    log_dir = ROOT / ".local"
    log_dir.mkdir(exist_ok=True)
    record = {
        "timestamp": dt.datetime.now(dt.timezone.utc).isoformat(),
        "tool": os.environ.get("KB_TOOL", "cli"),
        "keywords": sorted(canonical for canonical in ALIASES if canonical in terms),
        "matched_projects": projects,
        "deepened": deepened,
    }
    with (log_dir / "kb-usage.log").open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(record, ensure_ascii=False) + "\n")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="kb", description="Progressive retrieval for Tech-Knowledge-Base")
    sub = parser.add_subparsers(dest="command", required=True)
    search = sub.add_parser("search", help="find up to three relevant projects")
    search.add_argument("query")
    search.set_defaults(func=command_search)
    show = sub.add_parser("show", help="show the 30-second project summary")
    show.add_argument("project")
    show.set_defaults(func=command_show)
    reuse = sub.add_parser("reuse", help="extract one relevant reuse section")
    reuse.add_argument("project")
    reuse.add_argument("capability")
    reuse.set_defaults(func=lambda args: command_extract(args, "REUSE_GUIDE.md", 1800))
    architecture = sub.add_parser("architecture", help="extract one relevant architecture section")
    architecture.add_argument("project")
    architecture.add_argument("capability")
    architecture.set_defaults(func=lambda args: command_extract(args, "ARCHITECTURE.md", 2200))
    path = sub.add_parser("path", help="show public-document and ignored-source paths")
    path.add_argument("project")
    path.set_defaults(func=command_path)
    status = sub.add_parser("status", help="show freshness, commit, license and language")
    status.add_argument("project")
    status.set_defaults(func=command_status)
    route = sub.add_parser("route", help="simulate the lightweight router decision")
    route.add_argument("task")
    route.set_defaults(func=command_route)
    return parser


def main(argv: list[str] | None = None) -> int:
    try:
        args = build_parser().parse_args(argv)
        return args.func(args)
    except KBError as exc:
        print(f"kb: error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
