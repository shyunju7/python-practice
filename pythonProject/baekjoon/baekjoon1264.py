# baekjoon 1264 모음의 개수
# 브론즈 2
# 구현 문자열

import sys
testCase = ["a", "e", "i", "o", "u"]
answer = ""
count = 0
input = sys.stdin.readline
while True:
    line = input().rstrip()
    if line == "#":
        break

    for i in range(len(testCase)):
        count += line.lower().count(testCase[i])

    answer += str(count) + "\n"
    count = 0

print(answer)