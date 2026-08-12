from __future__ import annotations

import contextlib
import io
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
import kb  # noqa: E402


QUERY_CASES = (
    "做一个长期后台 Agent",
    "给 QQ Bot 做定时任务系统",
    "设计一个浏览器渲染模块",
    "给项目增加系统代理支持",
    "该选哪种 Agent Skills",
    "做一个新的 RAG 框架",
    "设计一个支持故障恢复的数据库任务调度系统",
    "比较几种 MCP 服务架构",
    "集成一套通用自动化工作流",
    "实现一个新的 DevTools 系统",
)

SKIP_CASES = (
    "README 改个错别字",
    "变量 foo 改成 bar，简单重命名",
    "这个函数少一个分号",
    "把按钮从左边移动到右边",
    "解释这三行代码",
    "修复当前文件已明确定位的空指针",
    "format these imports",
    "润色这一段文档",
    "把常量 1 改成 2",
    "给现有测试补一条已经写明的断言",
)


def run_cli(*args: str) -> tuple[int, str, str]:
    stdout = io.StringIO()
    stderr = io.StringIO()
    with contextlib.redirect_stdout(stdout), contextlib.redirect_stderr(stderr):
        code = kb.main(list(args))
    return code, stdout.getvalue(), stderr.getvalue()


class RouterTests(unittest.TestCase):
    def test_should_query_all_ten(self) -> None:
        for task in QUERY_CASES:
            with self.subTest(task=task):
                self.assertTrue(kb.should_query(task)[0])

    def test_should_skip_all_ten(self) -> None:
        for task in SKIP_CASES:
            with self.subTest(task=task):
                self.assertFalse(kb.should_query(task)[0])

    def test_empty_route_is_human_readable_error(self) -> None:
        code, _, error = run_cli("route", "")
        self.assertEqual(1, code)
        self.assertIn("cannot be empty", error)
        self.assertNotIn("Traceback", error)


class CLITests(unittest.TestCase):
    def test_search_limits_results_and_gives_next_action(self) -> None:
        code, output, _ = run_cli("search", "Agent Skills 选型")
        self.assertEqual(0, code)
        self.assertLessEqual(output.count("Relevance:"), 3)
        self.assertIn("Recommended next action:", output)
        self.assertIn("Source dive: NOT NEEDED YET", output)

    def test_bilingual_aliases(self) -> None:
        cases = (
            ("后台任务", "prime-agent"),
            ("child agent", "prime-agent"),
            ("network proxy", "fanqiang"),
        )
        for query, expected in cases:
            with self.subTest(query=query):
                code, output, _ = run_cli("search", query)
                self.assertEqual(0, code)
                self.assertIn(expected, output)

    def test_show_is_short_and_summary_only(self) -> None:
        code, output, _ = run_cli("show", "prime-agent")
        self.assertEqual(0, code)
        self.assertIn("30 秒快速判断", output)
        self.assertLessEqual(len(output), 1400)
        self.assertNotIn("# 核心技术", output)

    def test_reuse_extracts_one_section(self) -> None:
        code, output, _ = run_cli("reuse", "prime-agent", "subagent")
        self.assertEqual(0, code)
        self.assertEqual(1, output.count("\n# ") + output.startswith("# "))
        self.assertIn("子 Agent", output)
        self.assertNotIn("# 决策表", output)

    def test_architecture_extracts_one_section(self) -> None:
        code, output, _ = run_cli("architecture", "ladybird", "rendering")
        self.assertEqual(0, code)
        self.assertEqual(1, output.count("\n# ") + output.startswith("# "))
        self.assertLessEqual(len(output), 2200)

    def test_architecture_missing_is_clear(self) -> None:
        code, _, error = run_cli("architecture", "fanqiang", "proxy")
        self.assertEqual(1, code)
        self.assertIn("has no ARCHITECTURE.md", error)
        self.assertNotIn("Traceback", error)

    def test_path_lists_docs_and_ignored_source(self) -> None:
        code, output, _ = run_cli("path", "prime-agent")
        self.assertEqual(0, code)
        self.assertIn("SUMMARY.md", output)
        self.assertIn("source:", output)
        self.assertIn("ignored", output)

    def test_status_has_required_metadata(self) -> None:
        code, output, _ = run_cli("status", "prime-agent")
        self.assertEqual(0, code)
        for label in ("Analyzed commit:", "Analysis date:", "License:", "Main languages:"):
            self.assertIn(label, output)

    def test_unknown_project_is_clear(self) -> None:
        code, _, error = run_cli("show", "does-not-exist")
        self.assertEqual(1, code)
        self.assertIn("Unknown project", error)
        self.assertNotIn("Traceback", error)

    def test_empty_capability_is_clear(self) -> None:
        code, _, error = run_cli("reuse", "prime-agent", "")
        self.assertEqual(1, code)
        self.assertIn("Capability cannot be empty", error)
        self.assertNotIn("Traceback", error)

    def test_no_match_stops_retrieval(self) -> None:
        code, output, _ = run_cli("search", "quantum-zebra-compiler")
        self.assertEqual(0, code)
        self.assertIn("Stop KB retrieval", output)


if __name__ == "__main__":
    unittest.main()

