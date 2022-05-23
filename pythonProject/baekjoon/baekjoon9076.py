# 백준 9076 점수 집계
# 브론즈 2
# 구현 정렬

answer = []
num = int(input())
for _ in range(num):
    line = sorted(list(map(int, input().split())))
    if line[-2] - line[1] >= 4:
        answer.append("KIN")
    else:
        answer.append(sum(line[1:4]))
print(*answer, sep="\n", end="")
