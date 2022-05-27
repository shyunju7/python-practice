# baekjoon 14405
# 실버 5
# 문자열 정규표현식

import sys

import re

line = sys.stdin.readline().rstrip()
line = re.sub(r"pi|ka|chu", "", line)
print("YES" if len(line) == 0 else "NO")


