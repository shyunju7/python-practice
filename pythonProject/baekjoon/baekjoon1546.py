# baekjoon 1546 평균
# 브론즈 1
# 수학 사칙연산

answer = 0
num = int(input())
arr = list(map(int, input().split()))
arr.sort()

for i in range(num - 1):
    answer += arr[i] / arr[-1] * 100

print((answer + 100) / num)