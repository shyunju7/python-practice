# baekjoon 2875 대회 or 인턴
# 브론즈 3
# 수학 구현 사칙연산
n, m, k = map(int, input().split())
team = 0

while n >= 2 and m >= 1 and n + m - 3 > k:
    n -= 2
    m -= 1
    team += 1

print(team)
