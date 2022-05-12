# baekjoon 1076 저항
# 브론즈 2
# 구현
import math
colorSet = {
    "black": 0,
    "brown": 1,
    "red": 2,
    "orange": 3,
    "yellow": 4,
    "green": 5,
    "blue": 6,
    "violet": 7,
    "grey": 8,
    "white": 9,
}
arr = []

for _ in range(3):
    arr.append(input())

answer = str(colorSet.get(arr[0])) + str(colorSet.get(arr[1]))
answer = int(answer) * math.pow(10, colorSet.get(arr[2]))

print(int(answer))
