# baekjoon 10173 니모를 찾아서
# 브론즈 2
# 문자열
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


