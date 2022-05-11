# baekjoon 1075 나누기
# 브론즈 2
# 수학

n = input()
f = int(input())
minNum = int(n[:-2] + "00")
if minNum % f != 0:
    result = str((minNum // f + 1) * f)[-2:]
else:
    result = str(minNum)[-2:]
print(result)
