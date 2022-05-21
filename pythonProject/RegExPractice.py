# 정규표현식과 일치하는 모든 부분 찾기 -> findall
import re
regex = r'0\d{1,2}[ -]?\d{3,4}[ -]?\d{3,4}'
search_target = '''Luke Skywarker 02-123-4567 luke@daum.net
다스베이더 070-9999-9999 darth_vader@gmail.com
princess leia 010 2454 3457 leia@gmail.com'''
result = re.findall(regex, search_target)
print("\n".join(result))

# + 하나 혹은 그 이상
regex = r'\d+' # 하나 혹은 그 이상의 숫자로만 구성된 정규표현식

# * 0개 이상
regex = r'[1-9]\d*' # 처음에 1-9사이에 수가 나오고 그 뒤로는 0개 이상의 숫자

# ? 있거나 없거나
regex = r'\d+-?\d+-?\d+-?' # 숫자가 0개 이상 나오고 - 있거나 없거나
regex = r'[- ]?' # -이거나 공백이거나 없거나

# {숫자} 숫자만큼 반복
regex = r'\d{2}[- ]?' # 숫자2개가 반복되고 -이거나 공백이거나 없거나
regex = r'\d{2,3}[- ]?\d{3,4}[- ]?\d{4}' #2-3자리 숫자 다음에 -또는 공백 또는 없거나 3-4자리 숫자 다음 -또는 공백 또는 없거나 4자리 숫자

# [] 특정 모음
regex = r'[aeiou]' # a or e or i or o or u
regex = r'[a-z]' # a부터 z까지

regex = r'[a-z]+' # a부터 z까지가 1개 또는 그 이상 ex) Skywarker -> kywarker

# 한글 찾기
regex = '[가-힣]+' # 모든 한글 찾기