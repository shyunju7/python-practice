# baekjoon 11365 !밀비 급일
# 브론즈 2
# 구현 문자열
import sys
input = sys.stdin.readline
answer = ""
while True:
    line = input().rstrip()
    if line == "END":
        break
    answer += line[::-1] + "\n"
print(answer.rstrip())