#coding: cp949
age = 0
baby_money = 0
child_money = 2000
teenage_money = 3000
adult_money = 5000
oldman_money = 0
my_money = 0
charge_type = 0
credit_card = 0
while True: 
    age = int(input("나이를 입력하세요: "))
    if age < 4 and age > -1:
        print("귀하는 유아등급이며 요금은 %d원입니다."%baby_money)
    elif age > 65: 
        print("귀하는 노인등급이며 요금은 %d원입니다."%oldman_money)
    elif age < 0:
        print("다시 입력하세요")
    else:        
        if age > 3 and age < 14:
            print("귀하는 어린이등급이며 요금은 %d원입니다."%child_money)
            charge_type = int(input("요금 유형을 선택하세요:ex)1:현금, 2:공원 전용 신용카드 "))
            if charge_type == 1:
                my_money = int(input("요금을 입력하세요: "))
                if my_money < child_money:
                    print("%d원이 모자랍니다.입력 하신 %d원을 반환합니다."%(child_money-my_money, my_money))
                elif my_money > child_money:
                    print("감사합니다. 티켓을 발행하고 거스름돈 %d원을 반환합니다."%(my_money-child_money))
            elif charge_type == 2:
                credit_card = child_money * 0.9
                print("%d원 결제 되었습니다. 티켓을 발행합니다."%credit_card)

        elif age > 13 and age < 19:
            print("귀하는 청소년등급이며 요금은 %d원입니다."%teenage_money)
            charge_type = int(input("요금 유형을 선택하세요:ex)1:현금, 2:공원 전용 신용카드 "))
            if charge_type == 1:
                my_money = int(input("요금을 입력하세요: "))
                if my_money < teenage_money:
                    print("%d원이 모자랍니다.입력 하신 %d원을 반환합니다."%(teenage_money-my_money, my_money))
                elif my_money > teenage_money:
                    print("감사합니다. 티켓을 발행하고 거스름돈 %d원을 반환합니다."%(my_money-teenage_money))
            elif charge_type == 2:
                credit_card = teenage_money * 0.9
                print("%d원 결제 되었습니다. 티켓을 발행합니다."%credit_card)
        
        elif age > 18 and age < 66:
            print("귀하는 성인등급이며 요금은 %d원입니다."%adult_money)
            charge_type = int(input("요금 유형을 선택하세요:ex)1:현금, 2:공원 전용 신용카드 "))
            if charge_type == 1:
                my_money = int(input("요금을 입력하세요: "))
                if my_money < adult_money:
                    print("%d원이 모자랍니다.입력 하신 %d원을 반환합니다."%(adult_money-my_money, my_money))
                elif my_money > adult_money:
                    print("감사합니다. 티켓을 발행하고 거스름돈 %d원을 반환합니다."%(my_money-adult_money))
            elif charge_type == 2:
                credit_card = adult_money * 0.9
                print("%d원 결제 되었습니다. 티켓을 발행합니다."%credit_card)
            elif age >59 and age <66 and charge_type ==2:
                credit_card = adult_money * 0.95
                print("%d원 결제 되었습니다. 티켓을 발행합니다."%credit_card)
        print("감사합니다. 티켓을 발행합니다.")

