# baekjoon 2592 대표값
# 브론즈 2
# 수학 구현
arr = []
max_count = 0
value = ""
for _ in range(10):
    arr.append(int(input()))

for i in range(10):
    if arr.count(arr[i]) > max_count:
        max_count = arr.count(arr[i])
        value = arr[i]
print(int(sum(arr) / 10))
print(value)


