
# 파이썬에서 정규표현식 사용할 때 쓰는 모듈
# match(), fullmatch(), findall(), search(), sub()
# sub(패턴, 교체할 문자열, 문자열, 최대교체수, 플래그)
import re
demo = " This is test example. Welcome to Python!  "
# 문자열의 시작부분 공백 제거 => lstrip
print(demo.lstrip())
print(re.sub(r"^\s+", "", demo))
# 문자열 끝에서 공백 제거 => rstrip
print(demo.rstrip())
print(re.sub(r"\s+$", "", demo))
# 문자열 시작과 끝 공백제거 => strip
print(demo.strip())
print(re.sub(r"^\s+|\s+$", "", demo))
# 문자열의 모든 공백 제거
print(demo.replace(" ",""))
print(re.sub(r"\s", "", demo))
# 문자열의 복제된 공백만 제거


# 문자열에서 숫자를 가져오기
practice_string = "Today is 2022-05-23, Mon 122"
nums = [int(temp)for temp in practice_string.split() if temp.isdigit()]
print(nums)
print([int(s) for s in re.findall(r'-?\d+\.?\d*', practice_string)])
numsRe = [float(num)for num in re.findall(r'\d', practice_string)]
print(numsRe)