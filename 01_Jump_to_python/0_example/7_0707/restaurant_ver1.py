cook = []
class Restaurant:
    def __init__(self,name,type):
        self.restaurant_name = name
        self.cuisine_type = type
    def describe_restaurant(self):
        return "저희 레스토랑 명칭은 '%s'이고 %s 전문점입니다."% (self.restaurant_name,self.cuisine_type)
    def open_restaurant(self):
        return "저희 %s 레스토랑이 오픈했습니다. 어서오세요."% self.restaurant_name

cook = input("레스토랑 이름과 요리 종류를 선택하세요.(공백으로 구분): ")
list_cook = cook.split()
[name,type] = [list_cook[0],list_cook[1]]
# print(name)
# print(type)
a = Restaurant(name, type)
print(a.describe_restaurant())
print(a.open_restaurant())
