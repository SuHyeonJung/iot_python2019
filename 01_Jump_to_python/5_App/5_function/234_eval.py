print("미니 계산기 ver1.0")
while True:
    formula = input("아래 연산 수식을 입력하시고 Enter를 치세요. 수식을 계산해드립니다.")
    print(eval(formula))
    if formula == '':
        break