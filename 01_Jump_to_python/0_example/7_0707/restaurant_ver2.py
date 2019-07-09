cook = []
name_list = []
class Restaurant:
    def __init__(self,name,type):
        self.restaurant_name = name
        self.cuisine_type = type
    def describe_restaurant(self):
        return "저희 레스토랑 명칭은 '%s'이고 %s 전문점입니다."% (self.restaurant_name,self.cuisine_type)
    def open_restaurant(self):
        return "저희 %s 레스토랑이 오픈했습니다. 어서오세요."% self.restaurant_name
for i in range(0,3):
    cook = input("레스토랑 이름과 요리 종류를 선택하세요.(공백으로 구분): ")
    list_cook = cook.split()
    [name,type] = [list_cook[0],list_cook[1]]
    a = Restaurant(name, type)
    name_list = name_list + [name]
    describe = a.describe_restaurant()
    open = a.open_restaurant()
    print(describe)
    print(open)
print("\n저녁 10시가 되었습니다.\n")
for j in name_list:
    print("%s 레스토랑 문닫습니다."%j)
# print(name)
# print(type)
# a = Restaurant(name, type)
# describe = a.describe_restaurant()
# open = a.open_restaurant()
# print(describe)
# print(open)
