# baekjoon 2441 별찍기 - 4
# 브론즈 3
# 구현

num = int(input())

for i in range(num, -1, -1):
    print(" " * (num-i) + "*" * i)
