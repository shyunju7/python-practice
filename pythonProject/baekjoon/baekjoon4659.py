# 백준 4153
# 브론즈 3
# 수학 기하학 피타고라스 정리
import math
import sys

input = sys.stdin.readline
answer = []
while True:
    line = input().rstrip()
    if line == "0 0 0":
        break
    nums = list(map(int, line.split()))
    nums.sort()
    answer.append("right" if math.pow(nums[0], 2) + math.pow(nums[1], 2) == math.pow(nums[-1], 2) else "wrong")

print(*answer, sep="\n", end="")
