# baekjoon 1037 약수
# 실버 5
# 수학 정수론

num = int(input())
num_arr = list(map(int, input().split()))
num_arr.sort()
print(num_arr[0] * num_arr[-1], end="")


