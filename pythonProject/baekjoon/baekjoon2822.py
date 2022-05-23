# baekjoon 2822 점수 계산
# 실버 5
# 정렬
score = []
exam = []
for i in range(8):
    score.append(int(input()))
sorted_score = sorted(score, reverse=True)
for i in range(5):
    exam.append(str(score.index(sorted_score[i])+1))
print(sum(sorted_score[:5]))
print(" ".join(sorted(exam)))
