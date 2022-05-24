# baekjoon 2750 수 정렬하기
# 브론즈 1
# 구현 정렬
# n개의 수 오름차순 정렬
# 미해결

num = int(input())
num_arr = []
for _ in range(num):
    num_arr.append(int(input()))
num_arr.sort(reverse=True)

# *리스트명 -> 리스트에 구분자 추가하여 바로 출력
# print(*num_arr, sep="\n")
for i in range(num):
    if i == num -1:
        print(num_arr[i], end="")
        break
    print(num_arr[i])
