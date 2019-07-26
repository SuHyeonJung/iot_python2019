import json

def foreign_visit_number(g_json_big_data):
    count = 0
    for index in g_json_big_data:
        count = count + index["visit_cnt"]
    print("%d명"% count)

def modify_data(g_json_big_data):
    modify_list = []
    for index in g_json_big_data:
        del index['nat_cd']
        del index['yyyymm']
        index = index['nat_name']
        modify_list.append(index)
        print(modify_list)


with open('(2017)_해외방문객정보_2017.json', encoding='UTF8') as json_file:
    json_object = json.load(json_file)
    json_string = json.dumps(json_object)
    g_json_big_data = json.loads(json_string)

while True:
    input_national = input("1.외국인 방문객 수\n2.방문형태 변경\n3.프로그램 종료\n메뉴선택: ")
    if input_national == '1':
        foreign_visit_number(g_json_big_data)
    elif input_national == '2':
        modify_data(g_json_big_data)
    else:
        print("프로그램을 종료합니다.")
