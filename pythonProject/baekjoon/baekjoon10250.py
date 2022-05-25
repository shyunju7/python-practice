# baekjoon 10250 ACM 호텔
# 브론즈 3
# 수학 구현 사칙연산

n = int(input())
for i in range(n):
    cnt = 1
    h, w, n = map(int, input().split())
    y = n % h if n % h != 0 else h
    x = n // h + 1 if y != h else n // h
    print(y * 100 + x)
