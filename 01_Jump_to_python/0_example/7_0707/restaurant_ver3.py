number_served = 0
class Restaurant:
    def __init__(self,name,type,number):
        self.restaurant_name = name
        self.cuisine_type = type
        self.number = number
    def describe_restaurant(self):
        return "저희 레스토랑 명칭은 '%s'이고 %s 전문점입니다."% (self.restaurant_name,self.cuisine_type)
    def open_restaurant(self):
        return "저희 %s 레스토랑이 오픈했습니다."% self.restaurant_name
    def reset_number_served(self):
        return "손님 %d명 들어오셨습니다."% self.number
        self.total_served_number = total_served_number + self.number
    def increment_number_served(number):

    def check_customer_number(self):
        return "지금까지 총 %s명 손님께서 오셨습니다."% self.total_serverd_number

name, type = input("레스토랑 이름과 요리 종류를 선택하세요.(공백으로 구분): ").split()
a = Restaurant(name, type, number_served)
print(a.describe_restaurant())
while True:
    open = input("레스토랑을 오픈하시겠습니까?(y/n): ")
    if open == 'n':
        continue
    else:
        break
print(a.open_restaurant())
while True:
    guide = input("어서오세요. 몇명이십니까?(초기화:0입력,종료:-1,누적고객확인:p): ")
    if guide == '0':
        print(a.reset_number_served())
    elif guide == '-1':
        print("%s 레스토랑 문닫습니다."% name)
        break
    elif guide == 'p':
        print(a.check_customer_number())
    else:

"""    elif guide == -1:
        print("%s 레스토랑 문닫습니다." % name)
        break
    else:
        print("지금까지 총 %d명 손님께서 오셨습니다."%)"""
