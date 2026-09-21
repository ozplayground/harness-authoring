# Changelog

## [0.1.0] - 2026-09-21

초기 버전.

### Added

- `skill-authoring` 스킬 — 방법론 스킬과 도구 스킬의 구분(에이전트 이름은 도구 스킬에서만), 스킬에 넣는 것과 빼는 것, 이름(하는 일로), description, 제목 줄, frontmatter, 파일 나누기
- `agent-authoring` 스킬 — 에이전트 frontmatter 배선, 본문의 역할 계약, 넣지 않는 것
- `harness-audit` 스킬 — 검사 절차. 기계 검사 스크립트(`check_frontmatter.py`, `check_cross_refs.py`), 도구 동작 실험 절차, 보고 형식. 판정 기준은 두 작성 스킬에 둔다
- `harness-auditor` 에이전트 — 읽기 전용 검토자. 세 스킬을 불러 검사한다
- MIT 라이선스
