# baekjoon 1032 프롬
# 브론즈 2
# 구현 문자열

num = int(input())

arr = []
for _ in range(num):
    arr.append(input())

answer = ""
isSame = False
for i in range(len(arr[0])):

    if num == 1:
        isSame = True
        answer = arr[0]
        break

    for j in range(num - 1):
        if arr[j][i] != arr[j + 1][i]:
            isSame = False
            break
        else:
            isSame = True

    if isSame:
        answer += arr[0][i]
    else:
        answer += "?"

print(answer)
