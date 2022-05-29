# baekjoon 10820 문자열 분석
# 브론즈 2
# 구현 문자열
# 소문자 대문자 숫자 공백
import re

while True:
    try:
        line = input()
        lower_case_count = len(re.findall(r"[a-z]", line))
        upper_case_count = len(re.findall(r"[A-Z]", line))
        num_count = len(re.findall(r"\d", line))
        space_count = len(re.findall(" ", line))

        print(lower_case_count, upper_case_count, num_count, space_count)

    except EOFError:
        break
