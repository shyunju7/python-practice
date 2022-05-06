# baekjoon 13866 팀 나누기
# 브론즈 4
# 수학 구현 사칙연산


arr = list(map(int, input().split()))
sumArr = sum(arr)
maxMin = max(arr) + min(arr)

print(abs(sumArr - maxMin - maxMin))
