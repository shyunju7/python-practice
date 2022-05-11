# baekjoon 2986 세수
# 브론즈 3
# 수학 구현 사칙연산 많은 조건 분기
num1, num2, num3 = map(int, input().split())

# baekjoon 2986 세수
# 브론즈 3
# 수학 구현 사칙연산 많은 조건 분기
num1, num2, num3 = map(int, input().split())
if max(num1, num2, num3) == num2:
    if num2 - num3 == num1:
        print(f"{num1}={num2}-{num3}")
    else:
        print(f"{num1}={num2}/{num3}")

else:
    if num1 > num3:
        if num2 + num3 == num1:
            print(f"{num1}={num2}+{num3}")
        else:
            print(f"{num1}={num2}*{num3}")
    else:
        if num2 + num1 == num3:
            print(f"{num1}+{num2}={num3}")
        else:
            print(f"{num1}*{num2}={num3}")

# 풀이 2
# if num1 == num2 - num3:
#     print(f"{num1}={num2}-{num3}")
# elif num1 == num2 / num3:
#     print(f"{num1}={num2}/{num3}")
# elif num1 == num2 + num3:
#     print(f"{num1}={num2}+{num3}")
# elif num1 == num2 * num3:
#     print(f"{num1}={num2}*{num3}")
# elif num1 + num2 == num3:
#     print(f"{num1}+{num2}={num3}")
# else:
#     print(f"{num1}*{num2}={num3}")
