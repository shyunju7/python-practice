# baekjoon 11651 좌표 정렬하기 2
# 실버 5
# 정렬

n = int(input())
loc = []
for i in range(n):
    line = list(map(int, input().split()))
    loc.append(line)

loc.sort(key=lambda x: x[0])
loc.sort(key=lambda x: x[1])

for i in range(n):
    print(*loc[i])
