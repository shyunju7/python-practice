# baekjoon 1085 직사각형에서 탈출
# 브론즈 3
# 수학 기하학

x, y, w, h = map(int, input().split())
xGap = abs(x - w)
yGap = abs(y - h)
print(min(x, y, xGap, yGap))

