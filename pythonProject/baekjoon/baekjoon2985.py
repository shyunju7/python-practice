# baekjoon 2576 홀수
# 브론즈 3
# 수학 구현

arr = []
oddList = []

for _ in range(7):
    arr.append(int(input()))

for i in range(7):
    if arr[i] % 2 == 1:
        oddList.append(arr[i])

if len(oddList) == 0:
    print(-1)

else:
    print(sum(oddList))
    print(min(oddList))
