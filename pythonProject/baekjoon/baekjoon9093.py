# 백준 9093
# 브론즈 1
# 구현 문자열

num = int(input())
answer = ""
for i in range(num):
    tmp = input().split()

    for j in range(len(tmp)):
        answer += tmp[j][::-1] + " " # 역순 출력

    answer += "\n"

print(answer)
