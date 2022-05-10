# baekjoon 1267 핸드폰 요금
# 브론즈 3
# 수학 사칙연산

callCount = int(input())
arr = list(map(int, input().split()))
yCharge = 0
mCharge = 0

for i in range(callCount):
    yCharge += arr[i] // 30 + 1
    mCharge += arr[i] // 60 + 1

yCharge *= 10
mCharge *= 15

if yCharge > mCharge:
    print("M", mCharge)
elif yCharge == mCharge:
    print("Y M", yCharge)
else:
    print("Y", yCharge)

