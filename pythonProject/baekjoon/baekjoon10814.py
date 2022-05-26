# baekjoon 10814 나이순 정렬
# 실버 5
# 정렬
import sys

n = int(sys.stdin.readline())

users = []
for _ in range(n):
    line = sys.stdin.readline().rstrip()
    users.append(line)

print(*sorted(users, key=lambda x: int(x.split()[0])), sep="\n", end="")
