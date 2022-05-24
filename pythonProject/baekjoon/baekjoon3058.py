# baekjoon 3058 짝수를 찾아라
# 브론즈 3
# 수학 구현 사칙연산

num = int(input())

for _ in range(num):
    nums = list(map(int, input().split()))
    even_nums = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            even_nums.append(nums[i])

    print(sum(even_nums), min(even_nums))
