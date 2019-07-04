#coding: cp949
age = 0
baby_money = 0
child_money = 2000
teenage_money = 3000
adult_money = 5000
oldman_money = 0
my_money = 0
while True: 
    age = int(input("나이를 입력하세요: "))
    if age < 4 and age > -1:
        print("귀하는 유아등급이며 요금은 %d원입니다."%baby_money)
        print("감사합니다. 티켓을 발행합니다.")
    elif age > 3 and age < 14:
        print("귀하는 어린이등급이며 요금은 %d원입니다."%child_money)
        my_money = int(input("요금을 입력하세요: "))
        if my_money < child_money:
            print("%d원이 모자랍니다.입력 하신 %d원을 반환합니다."%(child_money-my_money, my_money))
        elif my_money > child_money:
            print("감사합니다. 티켓을 발행하고 거스름돈 %d원을 반환합니다."%(my_money-child_money))
        else:
            print("감사합니다. 티켓을 발행합니다.")
    elif age > 13 and age < 19:
        print("귀하는 청소년등급이며 요금은 %d원입니다."%teenage_money)
        my_money = int(input("요금을 입력하세요: "))
        if my_money < teenage_money:
            print("%d원이 모자랍니다.입력 하신 %d원을 반환합니다."%(teenage_money-my_money, my_money))
        elif my_money > teenage_money:
            print("감사합니다. 티켓을 발행하고 거스름돈 %d원을 반환합니다."%(my_money-teenage_money))
        else:
            print("감사합니다. 티켓을 발행합니다.")
    elif age > 18 and age < 65:
        print("귀하는 성인등급이며 요금은 %d원입니다."%adult_money)
        my_money = int(input("요금을 입력하세요: "))
        if my_money < adult_money:
            print("%d원이 모자랍니다.입력 하신 %d원을 반환합니다."%(adult_money-my_money, my_money))
        elif my_money > adult_money:
            print("감사합니다. 티켓을 발행하고 거스름돈 %d원을 반환합니다."%(my_money-adult_money))
        else:
            print("감사합니다. 티켓을 발행합니다.")
    elif age < 0:
        print("다시 입력하세요")
    else:
        print("귀하는 노인등급이며 요금은 %d원입니다."%oldman_money)
        print("감사합니다. 티켓을 발행합니다.")

