# baekjoon 10773 제로
# 실버 4
# 구현 자료 구조 스택

k = int(input())
stack = []
for _ in range(k):
    num = int(input())
    if num == 0:
        stack.pop()
    else:
        stack.append(num)
print(sum(stack), end="")


