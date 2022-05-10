# baekjoon 2747 피보나치 수
# 브론즈 3
# 수학 구현

num = int(input())
answer = 0

cur, nxt = 1, 1

for i in range(2, num):
    cur, nxt = nxt, cur + nxt

print(nxt)
