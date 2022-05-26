# baekjoon 1026 보물
# 실버 4
# 수학 그리디 알고리즘 정렬
# n은 길이 a,b는 n의 크기를 가지는 정수 배열, b는 재정렬 금지
import sys

answer = 0
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().rstrip().split()))
b = list(map(int, sys.stdin.readline().rstrip().split()))

a.sort()
for i in range(n):
    answer += a[i] * b.pop(b.index(max(b)))
print(answer, end="")
