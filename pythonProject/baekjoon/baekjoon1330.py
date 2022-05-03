# baekjoon 1330 두 수 비교하기
# 브론즈 4
# 수학 구현 사칙연산
a, b = map(int, input().split())
if a > b:
    print(">")
elif a == b:
    print("==")
else:
    print("<")

