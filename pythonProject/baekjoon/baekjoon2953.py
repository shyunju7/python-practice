# baekjoon 2953나는 요리사다
# 브론즈 3
# 구현

arr = []
maxSum = 0
index = -1
for i in range(5):
    arr.append(list(map(int, input().split())))

    if maxSum < sum(arr[i]):
        maxSum = sum(arr[i])
        index = i + 1

print(str(index) + " " + str(maxSum))
