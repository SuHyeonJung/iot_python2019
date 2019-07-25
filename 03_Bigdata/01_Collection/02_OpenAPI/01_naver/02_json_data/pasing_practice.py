import json

def student_search(g_json_big_data):
    student_save_1 = g_json_big_data[0]
    student_save_2 = g_json_big_data[1]
    student_save_3 = g_json_big_data[2]

    print("아래 메뉴를 선택하세요.")
    search = input("1.전체 학생정보 조회\n 검색 조건 선택\n2.ID 검색\n3.이름 검색\n4.나이 검색\n"
          "5.주소 검색\n6.과거 수강 횟수 검색\n7.강의 코드\n"
          "8.현재 수강 중인 강의명\n9.현재 수강 강사\n10.이전 메뉴\n"
          "메뉴를 선택하세요: ")

    if search == '1':
        all_student_info(g_json_big_data)
    elif search == '10':
        return
    else:
        add_search = input("검색어를 입력하세요: ")
        student_name_info(student_save_1, student_save_2, student_save_3, add_search)


def all_student_info(g_json_big_data):
    count = 0
    for name in g_json_big_data:
        print("* 학생 ID: ", g_json_big_data[count]["student_ID"])
        print("* 이름: ", g_json_big_data[count]["student_name"])
        print("* 나이: ", g_json_big_data[count]["student_age"])
        print("* 주소: ", g_json_big_data[count]["address"])
        print("* 수강정보")
        print("+ 과거 수강횟수: ", g_json_big_data[count]["total_course_info"]["num_of_course_learned"])
        print("+ 현재 수강과목")
        print("강의 코드: ", g_json_big_data[count]["total_course_info"]
        ["learning_course_info"][0]["course_code"])
        print("강의명: ", g_json_big_data[count]["total_course_info"]
        ["learning_course_info"][0]["course_name"])
        print("강사: ", g_json_big_data[count]["total_course_info"]
        ["learning_course_info"][0]["teacher"])
        print("개강일: ", g_json_big_data[count]["total_course_info"]
        ["learning_course_info"][0]["open_date"])
        print("종료일: ", g_json_big_data[count]["total_course_info"]
        ["learning_course_info"][0]["close_date"])

        count = count + 1

def student_name_info(student_save_1, student_save_2 ,student_save_3, add_search):

    if add_search in student_save_1.values() or \
            add_search in student_save_1["total_course_info"]["learning_course_info"][0].values():
        print("* 학생 ID: ", student_save_1["student_ID"])
        print("* 이름: ", student_save_1["student_name"])
        print("* 나이: ", student_save_1["student_age"])
        print("* 주소: ", student_save_1["address"])
        print("* 수강정보")
        print("+ 과거 수강횟수: ", student_save_1["total_course_info"]["num_of_course_learned"])
        print("+ 현재 수강과목")
        print("강의 코드: ", student_save_1["total_course_info"]
                    ["learning_course_info"][0]["course_code"])
        print("강의명: ", student_save_1["total_course_info"]
                    ["learning_course_info"][0]["course_name"])
        print("강사: ", student_save_1["total_course_info"]
            ["learning_course_info"][0]["teacher"])
        print("개강일: ", student_save_1["total_course_info"]
            ["learning_course_info"][0]["open_date"])
        print("종료일: ", student_save_1["total_course_info"]
            ["learning_course_info"][0]["close_date"])
    if add_search in student_save_2.values()or \
            add_search in student_save_2["total_course_info"]["learning_course_info"][0].values():
        print("* 학생 ID: ", student_save_2["student_ID"])
        print("* 이름: ", student_save_2["student_name"])
        print("* 나이: ", student_save_2["student_age"])
        print("* 주소: ", student_save_2["address"])
        print("* 수강정보")
        print("+ 과거 수강횟수: ", student_save_2["total_course_info"]["num_of_course_learned"])
        print("+ 현재 수강과목")
        print("강의 코드: ", student_save_2["total_course_info"]
                    ["learning_course_info"][0]["course_code"])
        print("강의명: ", student_save_2["total_course_info"]
                    ["learning_course_info"][0]["course_name"])
        print("강사: ", student_save_2["total_course_info"]
            ["learning_course_info"][0]["teacher"])
        print("개강일: ", student_save_2["total_course_info"]
            ["learning_course_info"][0]["open_date"])
        print("종료일: ", student_save_2["total_course_info"]
            ["learning_course_info"][0]["close_date"])
    if add_search in student_save_3.values()or \
            add_search in student_save_3["total_course_info"]["learning_course_info"][0].values():
        print("* 학생 ID: ", student_save_3["student_ID"])
        print("* 이름: ", student_save_3["student_name"])
        print("* 나이: ", student_save_3["student_age"])
        print("* 주소: ", student_save_3["address"])
        print("* 수강정보")
        print("+ 과거 수강횟수: ", student_save_3["total_course_info"]["num_of_course_learned"])
        print("+ 현재 수강과목")
        print("강의 코드: ", student_save_3["total_course_info"]
                    ["learning_course_info"][0]["course_code"])
        print("강의명: ", student_save_3["total_course_info"]
                    ["learning_course_info"][0]["course_name"])
        print("강사: ", student_save_3["total_course_info"]
            ["learning_course_info"][0]["teacher"])
        print("개강일: ", student_save_3["total_course_info"]
            ["learning_course_info"][0]["open_date"])
        print("종료일: ", student_save_3["total_course_info"]
            ["learning_course_info"][0]["close_date"])
    else:
        print("입력하신 정보가 없습니다.")
g_json_big_data = []
with open('ITT_Student.json', encoding='UTF8') as json_file:
    json_object = json.load(json_file)
    json_string = json.dumps(json_object)
    g_json_big_data = json.loads(json_string)

print(f'{"<< JSON기반 학생 정보 관리 프로그램 >>":^50}')
student_info = input("1.학생 정보입력\n2.학생 정보조회\n3.학생 정보수정\n"
                      "4.학생 정보삭제\n5.프로그램 종료\n"
                      "메뉴를 선택하세요: ")

if student_info == '1':
    pass
elif student_info == '2':
    student_search(g_json_big_data)
elif student_info == '3':
    pass
elif student_info == '4':
    pass
else:
    print("학생 정보 관리 프로그램을 종료합니다.")


