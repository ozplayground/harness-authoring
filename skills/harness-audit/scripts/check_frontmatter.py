#!/usr/bin/env python3
"""스킬·에이전트 정의의 frontmatter를 검사한다.

usage: check_frontmatter.py <root>
  <root> 아래를 재귀로 찾아 모든 SKILL.md 와, agents/ 디렉터리 안의 *.md 를 검사한다.
  보고하는 것:
    - frontmatter가 없는 파일
    - 따옴표 없는 값 안의 콜론+공백(': ')
    - 콜론으로 끝나는 따옴표 없는 값
  찾은 것이 있으면 파일:줄:열과 함께 출력하고 종료 코드 1. 없으면 0.
  들여쓴 이어지는 줄(여러 줄 값)은 검사하지 않는다.
"""
import pathlib
import re
import sys

QUOTED_START = ('"', "'", "[", "{", "|", ">")


def targets(root: pathlib.Path):
    yield from sorted(root.rglob("SKILL.md"))
    for d in sorted(root.rglob("agents")):
        if d.is_dir():
            yield from sorted(d.glob("*.md"))


def check(path: pathlib.Path):
    lines = path.read_text(encoding="utf-8").split("\n")
    if not lines or lines[0].strip() != "---":
        return [(1, 1, "frontmatter 없음")]
    found = []
    for no, line in enumerate(lines[1:], start=2):
        if line.strip() == "---":
            break
        m = re.match(r"^([A-Za-z_][\w-]*):(\s+)(.*)$", line)
        if not m:
            continue
        key, gap, val = m.group(1), m.group(2), m.group(3)
        if not val or val.startswith(QUOTED_START):
            continue
        start = len(key) + 1 + len(gap)  # 값이 시작하는 0 기준 열
        i = val.find(": ")
        if i != -1:
            found.append((no, start + i + 1, f"{key} 값 안에 따옴표 없는 ': ' — …{val[max(0, i - 10):i + 8]}…"))
        elif val.rstrip().endswith(":"):
            found.append((no, start + len(val.rstrip()), f"{key} 값이 따옴표 없이 ':'로 끝남"))
    return found


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    root = pathlib.Path(sys.argv[1])
    bad = 0
    for p in targets(root):
        for no, col, msg in check(p):
            print(f"{p}:{no}:{col}: {msg}")
            bad += 1
    print(f"-- {bad}건")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
