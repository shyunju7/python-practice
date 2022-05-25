# 프로그래머스 월간 코드 챌린지 시즌2 약수의 개수와 덧셈
# 제곱수의 약수의 갯수는 홀수!
def solution(left, right):
    answer = 0
    for i in range(left, right + 1):
        tmp = 0
        for j in range(1, i + 1):
            tmp += 1 if i % j == 0 else 0
        answer = answer + i if tmp % 2 == 0 else answer - i
    return answer


print(solution(13, 17))
print(solution(24, 27))

