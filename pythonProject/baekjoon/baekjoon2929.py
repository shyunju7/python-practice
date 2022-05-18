# baekjoon 10491 Quite a problem
# 브론즈 2
# 문자열 파싱
import sys
input = sys.stdin.readline
while True:
    line = input().rstrip()
    if line == "EOI":
        break

    if line.upper().find("NEMO") != -1:
            print("Found")
    else:
        print("Missing")


