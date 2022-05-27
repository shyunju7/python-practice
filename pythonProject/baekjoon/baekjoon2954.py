# baekjoon 2954 창영이의 일기장
# 브론즈 1
# 구현 문자열
# ppopopopopo -> ppopopo
import sys

line = sys.stdin.readline()
collection = ["a", "e", "i", "o", "u"]
answer = ""
i = 0
while i < len(line):
    answer += line[i]
    if line[i] in collection:
        i += 2
    i += 1

print(answer)