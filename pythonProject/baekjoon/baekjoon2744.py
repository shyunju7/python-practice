# baekjoon 2744 대소문자 바꾸기
# 브론즈 2
# 구현 문자열

line = input()
answer = ""
for i in range(len(line)):
    answer += line[i].lower() if line[i].isupper() else line[i].upper()
print(answer)