# baekjoon 1292 쉽게 푸는 문제
# 실버 5
# 구현 수학
start, end = map(int, input().split())
arr = []
for i in range(1, end+1):
    for j in range(i):
        if len(arr) == end:
            break
        arr.append(i)

print(sum(arr[start-1:end]))
