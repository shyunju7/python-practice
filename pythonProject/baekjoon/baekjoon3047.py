# baekjoon 3047 ABC
# 브론즈 2
# 구현
answer = ""
nums = sorted(list(map(int, input().split())))
order = input()

for i in range(3):
    if order[i] == "A":
        answer += str(nums[0]) + " "
    elif order[i] == "B":
        answer += str(nums[1]) + " "
    else:
        answer += str(nums[2]) + " "
print(answer)
