# 백준 3447 버그왕
# 브론즈 1
# 문자열 파싱
import sys
input = sys.stdin.readlines()

for line in input:
    while line.find("BUG") != -1:
        line = line.replace("BUG", "")
    print(line, end='')
