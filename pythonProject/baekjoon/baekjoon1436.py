# baekjoon 1427 소트인사이드
# 실버 5
# 문자열 정렬

num_arr = list(map(int, list(input())))
num_arr.sort(reverse=True)
print(*num_arr, sep="")
