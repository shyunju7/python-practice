def solution(n):
    answer = 0
    share = n
    remain = []
    while True:
        if share < 3:
            remain.append(share)
            break
        remain.append(share % 3)
        share //= 3
    length = len(remain)
    for i in range(length):
        answer += remain[i] * 3 ** (length - 1 - i)
    return answer


print(solution(45))
print(solution(125))
