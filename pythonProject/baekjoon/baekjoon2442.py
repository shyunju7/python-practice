# baekjoon 2441 별찍기 - 5
# 브론즈 3
# 구현

num = int(input())

for i in range(num, 0, -1):
    print(" " * (i-1) + "*" * (num-i) + "*" + "*" * (num-i))

