# baekjoon 2750 수 정렬하기 1
# 브론즈 1
# 정렬
import sys

# 파이썬3의 최대 재귀 깊이는 1000임으로 임의적으로 파이썬 기본 제귀 깊이 변경 필요
sys.setrecursionlimit(99999)


def quick_sort(nums):
    if len(nums) <= 1:
        return nums

    pivot = nums[0]
    left = []
    right = []

    for i in range(1, len(nums)):
        if pivot <= nums[i]:
            right.append(nums[i])
        else:
            left.append(nums[i])

    left = quick_sort(left)
    right = quick_sort(right)

    left.append(pivot)
    left.extend(right)
    return left


input = sys.stdin.readline
n = int(input())

num_arr = []
for _ in range(n):
    num_arr.append(int(input()))

print(*quick_sort(num_arr), sep="\n", end="")
