# baekjoon 1181 단어 정렬
# 실버 5
# 문자열 정렬

num = int(input())
arr = []
for _ in range(num):
    arr.append(input())

arr = list(set(arr))
arr.sort()
arr = sorted(arr, key=lambda x: len(x))
print(*arr, sep="\n", end="")
