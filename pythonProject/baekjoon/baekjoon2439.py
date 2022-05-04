# baekjoon 2438 별찍기 - 2
# 브론즈 3
# 구현

num = int(input())

for i in range(num-1, -1, -1):
    print(" " * i + "*" * (num-i))
