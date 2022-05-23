# 백준 5543 상근날드
# 브론즈 4
# 수학 사칙연산
# 입력 : 상덕버거, 중덕버거, 하덕버거, 콜라, 사이다 순 가격
# 출력 : 가장 싼 세트 메뉴 가격 출력(세트시 50원 할인)

menu = []
for _ in range(5):
    menu.append(int(input()))
print(min(menu[:3]) + min(menu[3:]) - 50, end="")
