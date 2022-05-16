# baekjoon 1100 하얀 칸
# 브론즈 2
# 구현 문자열
count = 0
for i in range(8):
    line = list(input())
    if i % 2 == 1: # 홀수 라인
        for j in range(8):
            if j % 2 == 1 and line[j] == "F": # 짝수 칸
                count += 1
    else: # 짝수 라인
        for j in range(8):
            if j % 2 != 1 and line[j] == "F": # 홀수 칸
                count += 1

print(count)
