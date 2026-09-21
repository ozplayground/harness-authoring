#!/usr/bin/env python3
"""스킬 본문과 description에서 다른 스킬의 이름이 나오는 줄을 찾는다.

usage: check_cross_refs.py <skills-root>
  <skills-root> 바로 아래의 <이름>/SKILL.md 들을 스킬 목록으로 삼고,
  각 스킬 디렉터리 안의 .md 파일에서 자기 아닌 스킬 이름이 나오는 줄을 출력한다.
  "name:"으로 시작하는 줄은 제외한다. 값·파일명과 우연히 겹친 것도 나오므로 후보로 보고 사람이 판정한다.
  마지막 줄의 건수는 (줄, 스킬 이름) 쌍의 수다. agents/ 는 검사하지 않는다.
"""
import pathlib
import re
import sys


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    root = pathlib.Path(sys.argv[1])
    skills = sorted(p.parent.name for p in root.glob("*/SKILL.md"))
    if not skills:
        sys.exit(f"{root} 아래에 */SKILL.md 가 없다")
    # 경계는 ASCII 기준: 이름 뒤에 한글 조사("를", "가")가 붙어도 잡는다
    pats = {s: re.compile(r"(?<![A-Za-z0-9_-])" + re.escape(s) + r"(?![A-Za-z0-9_-])") for s in skills}
    hits = 0
    for own in skills:
        for f in sorted((root / own).rglob("*.md")):
            for no, line in enumerate(f.read_text(encoding="utf-8").split("\n"), 1):
                if line.startswith("name:"):
                    continue
                for s in skills:
                    if s != own and pats[s].search(line):
                        print(f"{f}:{no}: [{s}] {line.strip()[:120]}")
                        hits += 1
    print(f"-- 후보 {hits}건 (스킬 {len(skills)}개)")


if __name__ == "__main__":
    main()
