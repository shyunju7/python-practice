# baekjoon 10987 모음의 개수
# 브론즈 2
# 구현 문자열

import re
line = input()
print(len(re.findall(r'[aeiou]', line)))


