# baekjoon 2441 별찍기 - 6
# 브론즈 3
# 구현

num = int(input())

for i in range(num, 0, -1):
    print(" " * (num-i) + "*" * (i-1) + "*" + "*" * (i-1))

