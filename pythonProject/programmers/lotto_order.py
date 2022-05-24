# 2021 Dev-matching 로또의 최고 순위와 최저 순위
def solution(lottos, win_nums):
    answer = [0] * 2
    arr = [num for num in lottos if num not in win_nums]
    winning_count = 6 - len(arr)
    zero_count = arr.count(0)
    if zero_count == 0:
        answer[0] = 6 if winning_count == 0 else 7 - winning_count
        answer[1] = 6 if winning_count == 0 else 7 - winning_count
    else:
        answer[0] = 7 - zero_count - winning_count
        answer[1] = 6 if 7 - winning_count >= 6 else 7 - winning_count
    return answer


print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))
print(solution([0, 0, 0, 0, 0, 0], [31, 10, 45, 1, 6, 19]))
print(solution([45, 4, 35, 20, 3, 9], [20, 9, 3, 45, 4, 35]))
print(solution([1, 1, 1, 1, 1, 1], [2, 3, 4, 5, 6, 7]))
