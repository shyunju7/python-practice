# baekjoon 2441 별찍기 - 7
# 브론즈 3
# 구현

num = int(input())

for i in range(num, 0, -1):
    print(" " * (i-1) + "*" * (num-i) + "*" + "*" * (num-i))

for i in range(num, 0, -1):
    print(" " * (num-i) + "*" * (i-1) + "*" + "*" * (i-1))

