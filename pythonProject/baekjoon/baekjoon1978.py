# baekjoon 1978 소수 찾기
# 실버 4
# 수학 정수론 소수 판정 에라토스테네스의 체


def is_prime(n):
    for j in range(2, n):
        if n % j == 0:
            return False
    return True


num = int(input())
arr = list(map(int, input().split()))
count = 0

for v in arr:
    rlt = is_prime(v) if v > 1 else False
    count += 1 if rlt else 0

print(count)
