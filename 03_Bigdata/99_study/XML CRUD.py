from xml.etree.ElementTree import Element, parse, SubElement

tree = parse("students_info2.xml")
note = tree.getroot()

def summary_info(note):
    count = 0
    man_count = 0
    woman_count = 0
    major_count = 0
    experience = 0
    high_level = 0
    python = 0
    young_age_count = 0
    middle_age_count = 0
    old_age_count = 0
    for country in note.getiterator("student"):
        count = count + 1
        if country.attrib["sex"] == '남':
            man_count = man_count + 1
        else:
            woman_count = woman_count + 1
        if country.findtext("major") == '컴퓨터 공학' or country.findtext("major") == '통계빅데이터':
            major_count = major_count + 1
        if int(country.findtext("age")) < 30:
            young_age_count = young_age_count + 1
        elif int(country.findtext("age")) >= 30 and int(country.findtext("age")) < 40 :
            middle_age_count = middle_age_count + 1
        else:
            old_age_count = old_age_count + 1
        for spec in country.getiterator("language"):
            if spec.attrib["name"] == 'C' or spec.attrib["name"] == 'Java':
                experience = experience + 1
            if spec.attrib["level"] == ' 상':
                high_level = high_level + 1
            if spec.attrib["name"] == 'Python':
               python = python + 1
    print("* 전체 학생수: %d"% count)
    print("* 성별\n- 남학생: %d명(%0.1f%%)\n- 여학생: %d명(%0.1f%%)"
          % (man_count, (man_count/count)*100,woman_count,
             (woman_count/count)*100))
    print("* 전공여부")
    print("- 전공자(컴퓨터 공학,통계): %d명 (%0.1f%%)"%
          (major_count, (major_count/count)*100))
    print("프로그래밍 언어 경험자: %d명 (%0.1f%%)"% (experience, (experience/count)*100))
    print("프로그래밍 언어 상급자: %d명 (%0.1f%%)"% (high_level, (high_level/count)*100))
    print("파이썬 경험자: %d명 (%0.1f%%)"% (python, (python/count)*100))
    print("* 연령대")
    print("- 20대: %d명 (%0.1f%%)"% (young_age_count,(young_age_count/count)*100), end='')
    young_dic = {}
    for country in note.getiterator("student"):
        if int(country.findtext("age")) < 30:
            young_dic[country.attrib["name"]] = country.findtext("age")
    print(young_dic)
    print("- 30대: %d명 (%0.1f%%)"% (middle_age_count, (middle_age_count/count)*100), end='')
    middle_dic = {}
    for country in note.getiterator("student"):
        if int(country.findtext("age")) >= 30 and int(country.findtext("age")) < 40:
            middle_dic[country.attrib["name"]] = country.findtext("age")
    print(middle_dic)
    print("- 40대: %d명 (%0.1f%%)"% (old_age_count,(old_age_count/count)*100), end='')
    old_dic = {}
    for country in note.getiterator("student"):
        if int(country.findtext("age")) > 40:
            old_dic[country.attrib["name"]] = country.findtext("age")
    print(old_dic)
def student_info(note):
    for country in note.getiterator("student"):
        print("* ", country.attrib["name"])
        print("성별: ", country.attrib["sex"])
        print("나이: ", country.findtext("age"))
        print("전공: ", country.findtext("major"))
        print("-사용 가능한 컴퓨터 언어")
        for spec in country.getiterator("language"):
            print(spec.attrib["name"]+"(학습기간: ", spec.attrib["level"],end ='')
            for period in spec.getiterator("period"):
                print(", Level: ", period.attrib["value"]+")")
def student_search(tree, note):
    while True:
        sub_menu = input("<조회 서브 메뉴>\n1.개별 학생 조회\n2.전체 학생 조회\n"
                         "3.상위 메뉴\n메뉴 입력: ")
        if sub_menu == '1':
            while True:
                print("< 검색 조건 >")
                search_condition = input("1.ID\n2.이름\n3.나이\n4.전공\n5.컴퓨터 언어 명\n"
                                         "6.컴퓨터 언어 학습 기간\n7.컴퓨터 언어 레벨\n"
                                         "8.상위 메뉴\n메뉴 입력: ")
                if search_condition == '8':
                    break
                else:
                    while True:
                        input_search = input("검색어를 입력하세요: ")
                        for parent in note.getiterator("student"):
                            if parent.find(input_search) in parent:
                                print(parent.get("name"))
                                print(parent.get("ID"))
                            # print("- 성별: ", country.get("sex"))

                            break
                        # print("- 성별: ", input_search.get("sex"))
                        # print("- 나이: ", input_search.findtext("age"))
                        # print("- 전공: ", input_search.findtext("major"))
                        # print("-사용 가능한 컴퓨터 언어")
                        # for spec in input_search.getiterator("language"):
                        #     print(spec.attrib["name"] + "(학습기간: ", spec.attrib["level"], end='')
                        #     for period in spec.getiterator("period"):
                        #         print(", Level: ", period.attrib["value"] + ")")

        elif sub_menu == '2':
            for country in note.getiterator("student"):
                print("* ", country.get("name"))
                print("성별: ", country.get("sex"))
                print("나이: ", country.findtext("age"))
                print("전공: ", country.findtext("major"))
                print("-사용 가능한 컴퓨터 언어")
                for spec in country.getiterator("language"):
                    print(spec.attrib["name"] + "(학습기간: ", spec.attrib["level"], end='')
                    for period in spec.getiterator("period"):
                        print(", Level: ", period.attrib["value"] + ")")
        else:
            break



while True:
    input_number = input("\n1.요약 정보\n2.입력\n3.조회\n4.수정\n5.삭제\n6.종료\n메뉴 입력: ")
    if input_number == '1':
        summary_info(note)
    elif input_number == '2':
        student_info(note)
    elif input_number == '3':
        student_search(tree, note)
    elif input_number == '4':
        pass
    elif input_number == '5':
        pass
    else:
        print("종료합니다.")
        break