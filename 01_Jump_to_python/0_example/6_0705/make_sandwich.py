ingredient_list = []
def input_ingredient(ingredient_input):
    while True:
        ingredient_input = input("안녕하세요. 원하시는 재료를 입력하세요: ")
        if ingredient_input == '종료':
            break
        else:
            ingredient_list.append(ingredient_input)
            continue
    ingredient = ingredient_list
    make_sandwiches(ingredient)

def make_sandwiches(ingredient):
    print("샌드위치를 만들겠습니다.")
    for i in ingredient:
        print("%s 추가합니다."%i)

    print("여기 주문하신 샌드위치 만들었습니다. 맛있게 드세요.")

a = 0
wait_message = int(input("안녕하세요. 저희 가게에 방문해 주셔서 감사합니다.\n1. 주문\n2. 종료\n입력: "))
if wait_message == 1:
    input_ingredient(a)
else:
    print("안녕히 가세요.")
