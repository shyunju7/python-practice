# baekjoon 2490 윷놀이
# 브론즈 3
# 구현

answer = ""
playSet = {0: "D", 1: "C", 2: "B", 3: "A", 4: "E"}

for i in range(3):
    result = sum(list(map(int, input().split(" "))))
    answer += playSet.get(result, -1) + "\n"
print(answer)
