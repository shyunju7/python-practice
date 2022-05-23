# baekjoon 11721 열 개씩 끊어 출력하기
# 브론즈 2
# 구현 문자열

line = input()
for i in range(0, len(line), 10):
    print(line[i:i+10])


