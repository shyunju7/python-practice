# baekjoon 178383 코맨드
# 브론즈 2
# 구현 문자열

num = int(input())

for _ in range(num):
    line = input()
    lastIndex = len(line) - 1
    if lastIndex == 6 and line[0] != line[lastIndex]:
        print(1 if line[0] * 2 + line[lastIndex] * 2 + line[0] + line[lastIndex] * 2 == line else 0)
    else:
        print(0)




