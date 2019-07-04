#coding: cp949
age = 0

while True: 
    age = int(input("나이를 입력하세요: "))
    if age < 4 or age > 65:
        print("요금은 0원입니다.")
    elif age > 3 and age < 14:
        print("요금은 2000원입니다.")
    elif age > 13 and age < 19:
        print("요금은 3000원입니다.")
    elif age > 18 and age < 65:
        print("요금은 5000원입니다.")

