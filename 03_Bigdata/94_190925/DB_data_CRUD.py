import MySQLdb

con = MySQLdb.connect(host='localhost', port= 3306, db='erd_students', user = 'root', passwd = '1111', charset='utf8')
c = con.cursor()

def create_data():
    data = []
    print("예)ITT001 홍길동 남 45 행정학 java 중 1년")
    rows = input("입력: ").split()
    for row in rows:
        data.append(str(row).strip())
    print(data)
    c.execute("""INSERT INTO student_info 
            (Student_ID,Name,Sex,Age,Major,Language_Name,Level,Period) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);""", data)
    con.commit()

def data_show(number):
    if number == 1:
        c.execute("SELECT * FROM student_info")
        rows = c.fetchall()
        for row in rows:
            row_list_output = []
            for column_index in range(len(row)):
                row_list_output.append(str(row[column_index]))
            print(row_list_output)
    elif number == 2:
        id_search = input("ID를 입력하세요: ")
        c.execute("SELECT * FROM student_info WHERE Student_ID = %s", id_search)
        rows = c.fetchall()
        for row in rows:
            row_list_output = []
            for column_index in range(len(row)):
                row_list_output.append(str(row[column_index]))
            print(row_list_output)

def data_update():
    update_id = input("아디를 입력하세요: ")
    c.execute("SELECT * FROM student_info WHERE Student_ID = %s", update_id)
    rows = c.fetchall()
    for row in rows:
        row_list_output = []
        for column_index in range(len(row)):
            row_list_output.append(str(row[column_index]))
        print(row_list_output)

    update_data = []
    print("예)홍길동 남 45 행정학 java 중 1년")
    rows = input("입력: ").split()
    for row in rows:
        update_data.append(str(row).strip())
    update_data.append(str(update_id).strip())
    c.execute("""UPDATE student_info SET Name=%s, Sex=%s, Age=%s, Major=%s, Language_Name=%s, Level=%s, Period=%s
            WHERE Student_ID=%s;""", update_data)
    con.commit()
    print("변경되었습니다.")

def data_delete():
    update_id = input("아디를 입력하세요: ")
    c.execute("SELECT * FROM student_info WHERE Student_ID = %s", update_id)
    rows = c.fetchall()
    for row in rows:
        row_list_output = []
        for column_index in range(len(row)):
            row_list_output.append(str(row[column_index]))
        print(row_list_output)
    delete_row = input("삭제하시겠습니까(y/n): ")
    if delete_row == 'y':
        c.execute("DELETE FROM student_info WHERE Student_ID=%s;", update_id)
    else:
        pass
    con.commit()

while True:
    print("<메인 메뉴>")
    print("1.생성(Insert)")
    print("2.조회(Select)")
    print("3.변경(Update)")
    print("4.삭제(Delete)")
    print("5.종료")
    menu = input("메뉴를 선택하세요: ")
    menu = int(menu)
    if menu == 1:
        create_data()
    elif menu == 2:
        while True:
            print("<2.데이터 조회>")
            print("1.전체 조회")
            print("2.아이디 조회")
            print("3.이전 메뉴")
            sub_menu = input("메뉴를 입력하세요: ")
            sub_menu = int(sub_menu)
            if sub_menu == 1:
                data_show(1)
            elif sub_menu == 2:
                data_show(2)
            elif sub_menu == 3:
                break
            else:
                print("잘못 입력하였습니다.다시 입력하세요.")
    elif menu == 3:
        data_update()
    elif menu == 4:
        data_delete()
    elif menu == 5:
        break
    else:
        print("잘못 입력하였습니다.다시 입력하세요.")
