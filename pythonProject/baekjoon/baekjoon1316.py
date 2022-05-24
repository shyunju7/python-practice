# baekjoon 1316 그룹 단어 체커
# 실버 5
# 구현 문자열
# 그룹 단어란, 단어에 존재하는 모든 문자에 대해서, 각 문자가 연속해서 나타나는 경우

num = int(input())
answer = 0
for _ in range(num):
    line = input()
    is_group_word = False
    for i in range(len(line)):
        count = line.count(line[i])
        if line.find(line[i] * count) == -1:
            is_group_word = False
            break
        else:
            is_group_word = True

    answer += 1 if is_group_word else 0
print(answer, end="")
