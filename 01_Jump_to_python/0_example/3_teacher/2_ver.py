#coding: cp949
age = 0

while True: 
    age = int(input("나이를 입력하세요: "))
    if age < 4 and age > -1:
        print("귀하는 유아등급이며 요금은 0원입니다.")
    elif age > 3 and age < 14:
        print("귀하는 어린이등급이며 요금은 2000원입니다.")
    elif age > 13 and age < 19:
        print("귀하는 청소년등급이며 요금은 3000원입니다.")
    elif age > 18 and age < 65:
        print("귀하는 성인등급이며 요금은 5000원입니다.")
    elif age < 0:
        print("다시 입력하세요")
    else:
        print("귀하는 노인등급이며 요금은 0원입니다.")

