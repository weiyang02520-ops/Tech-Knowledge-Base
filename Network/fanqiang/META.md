---
project_name: "fanqiang"
upstream_repository: "bannedbook/fanqiang"
github_url: "https://github.com/bannedbook/fanqiang"
author_or_organization: "bannedbook and contributors"
default_branch: "master"
analyzed_commit: "3eed6fb9871dcda66f2071b7ce3977c62501d603"
analysis_date: "2026-08-09"
license: "Unknown / repository-wide license not identified"
main_languages: ["Kotlin", "JavaScript", "Go", "HTML", "Java", "Python", "Shell"]
main_technologies: ["Android", "V2Ray", "Xray", "Shadowsocks", "Clash-family", "Tor", "system proxy", "router proxy"]
project_status: "Active repository containing mixed-current and historical material"
tags: ["network", "proxy", "windows", "linux", "android", "ios", "router", "v2ray", "shadowsocks", "clash", "tor", "historical", "security-sensitive"]
possible_reuse_areas: ["cross-platform proxy taxonomy", "historical implementation map", "client and routing terminology"]
---

# Metadata

## Documentation Location

- Main index: `source/README.md`
- Platform guides: `source/windows/`, `source/android/`, `source/ios/`, `source/macos/`, `source/linux/`, `source/router/`
- Protocol and server notes: `source/v2ss/`
- Explicit historical material: `source/deprecated/`

## Important Directories

| Directory | Role | Analysis Note |
| --- | --- | --- |
| `android/`, `ios/`, `windows/`, `macos/`, `linux/` | Platform tutorials | Individual pages have different ages; revalidate before use. |
| `router/` | OpenWrt and router notes | Concepts remain useful; exact packages and commands are dynamic. |
| `v2ss/` | Server/protocol articles and assets | Useful as a vocabulary map, not an authoritative current setup guide. |
| `fqnews/`, `fqnews2/` | Android application source trees | Separate applications, not merely documentation. |
| `deprecated/` | Old GoAgent, PAC, iOS and related material | Historical only. |
| `ChromeGo*`, `EdgeGo`, `FirefoxFqLinux`, `apk/`, `tor-browser-portable/` | Bundles or download entry points | Do not execute; provenance and freshness require separate verification. |

## Repository Size at Analysis

- Tracked files: 1,874
- Local shallow-clone size: approximately 175 MB including Git metadata
- Worktree state after clone: clean

## License Verification Notes

**Fact:** No repository-root `LICENSE`, `COPYING`, or standard SPDX license was found. `fqnews/` and `fqnews2/` contain their own license files, but those component licenses do not automatically cover the entire repository. The root README contains a distribution/non-commercial statement, which is not a standard open-source license and does not resolve rights for every bundled component.

**Recommendation:** Treat repository-wide licensing as `Unknown`. Do not redistribute `source/`, bundled programs, images, or copied tutorials. Public only independent analysis and short necessary quotations with attribution.

## Analysis Scope

Read the root and platform indexes, inspected the directory distribution, separated the explicitly deprecated area, identified license boundaries, and checked current GitHub metadata for representative successors such as v2rayN, v2rayNG, Xray-core, Clash-family clients, Shadowsocks and OpenClash. No executable, script, APK, installer, proxy program, or application code was run.

