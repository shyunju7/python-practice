# baekjoon 1773 폭죽쇼
# 브론즈 2
# 수학 구현

n, c = map(int, input().split())
answer = [0] * c

for _ in range(n):
    curNum = int(input())
    for i in range(curNum, c + 1, curNum):

        if answer[i - 1] == 0:
            answer[i - 1] = 1

print(sum(answer))



