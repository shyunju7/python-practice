# 백준 9012 괄호
# 실버 4
# 자료구조 문자열 스택
import sys

num = int(sys.stdin.readline())

for i in range(num):
    line = sys.stdin.readline().strip()
    while True:
        if line.count("()") == 0:
            print("YES" if len(line) == 0 else "NO")
            break
        else:
            line = line.replace("()", "")
