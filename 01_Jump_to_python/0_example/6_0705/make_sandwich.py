ingredient_list = []
def input_ingredient(ingredient_list):

    while True:
        ingredient_list = str(input("안녕하세요. 원하시는 재료를 입력하세요: "))
        if ingredient_list == '종료':
            break

def make_sandwiches(*ingredient_list):
    print("샌드위치를 만들겠습니다.")
    for i in ingredient_list:
        print(i)

    print("여기 주문하신 샌드위치 만들었습니다. 맛있게 드세요.")

wait_message = int(input("안녕하세요. 저희 가게에 방문해 주셔서 감사합니다.\n1. 주문\n2. 종료\n입력: "))
if wait_message == 1:
    input_ingredient(1)
    make_sandwiches(ingredient_list)
else:
    print("안녕히 가세요.")
