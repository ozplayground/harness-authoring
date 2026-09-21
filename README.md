# harness-authoring

[![Release](https://img.shields.io/github/v/release/ozplayground/harness-authoring)](https://github.com/ozplayground/harness-authoring/releases)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Claude Code Plugin](https://img.shields.io/badge/Claude%20Code-plugin-D97757)](https://code.claude.com/docs/en/plugins)

Claude Code **스킬과 서브에이전트 정의를 쓰고 검사하는 방법론**을 담은 플러그인이다.

- 스킬에는 지시만 쓴다 — 절차·금지·형식·판정 기준·흔한 실패
- 스킬은 두 종류다 — 방법론 스킬(어떤 일을 어떻게 하는가)과 도구 스킬(에이전트를 부르고 하네스의 장치를 다루는 절차). 에이전트 이름은 도구 스킬에서만 쓴다
- 에이전트 정의에는 배선과 역할 계약만 쓴다 — 도구, 불러올 스킬, 부를 에이전트, 하는 것과 하지 않는 것
- 규칙이 생긴 이유는 `CHANGELOG.md`에 쓴다
- 도구 동작에 대한 문장은 실험이나 공식 문서로 확인한 것만 쓴다

## 구성

| 종류 | 이름 | 하는 일 |
|---|---|---|
| 스킬 | `skill-authoring` | 스킬을 쓰거나 고칠 때. 방법론·도구 두 종류, 넣는 것과 빼는 것, 이름, description, 제목 줄, frontmatter, 파일 나누기 |
| 스킬 | `agent-authoring` | 에이전트 정의를 쓰거나 고칠 때. frontmatter 배선, 본문의 역할 계약, 넣지 않는 것 |
| 스킬 | `harness-audit` | 이미 있는 스킬·에이전트를 검사하는 절차. 기계 검사 스크립트 2개, 도구 동작 실험 절차(`references/probe.md`), 보고 형식. 판정 기준은 위 두 스킬을 쓴다 |
| 에이전트 | `harness-auditor` | 작성한 쪽과 다른 인스턴스로 검사를 맡는 읽기 전용 검토자. 세 스킬을 모두 불러 쓴다 |

설치하면 이름 앞에 플러그인 이름이 붙는다. `harness-authoring:skill-authoring`, `harness-authoring:harness-auditor`.

검사 스크립트는 파이썬 표준 라이브러리만 쓴다.

```bash
python3 skills/harness-audit/scripts/check_frontmatter.py <하네스 루트>
python3 skills/harness-audit/scripts/check_cross_refs.py <skills 디렉터리>
```

## 설치

GitHub 저장소를 마켓플레이스로 추가하고 설치한다.

```
/plugin marketplace add ozplayground/harness-authoring
/plugin install harness-authoring@harness-authoring
```

로컬에 받은 디렉터리로도 된다. `/plugin marketplace add <디렉터리 경로>`

## 디렉터리 구조

```
.
├── .claude-plugin/
│   ├── plugin.json
│   └── marketplace.json
├── agents/
│   └── harness-auditor.md
├── skills/
│   ├── agent-authoring/SKILL.md
│   ├── harness-audit/
│   │   ├── SKILL.md
│   │   ├── references/probe.md
│   │   └── scripts/
│   │       ├── check_cross_refs.py
│   │       └── check_frontmatter.py
│   └── skill-authoring/SKILL.md
├── .gitignore
├── CHANGELOG.md
├── LICENSE
└── README.md
```

## 라이선스

MIT
