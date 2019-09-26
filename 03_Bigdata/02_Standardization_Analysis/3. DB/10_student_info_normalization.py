import time
import csv
import MySQLdb

def sump_db():

    count = 0
    parent_test = ''
    lan_cnt = 0
    cnt_level = 0
    cnt_python = 0
    age_20 = []
    age_30 = []
    age_40 = []
    major_cnt = 0
    boy = 0
    girl = 0
    output_full = []
    output_full2 = []

    mysql_set.execute("SELECT * FROM %s;"%table_list)
    rows = mysql_set.fetchall()
    for row in rows:
        output = []
        for column_index in range(len(row)):
            output.append(str(row[column_index]))
        output_full.append(output)

    mysql_set.execute("SELECT * FROM %s;"%table_language)
    rows = mysql_set.fetchall()
    for row in rows:
        output = []
        for column_index in range(len(row)):
            output.append(str(row[column_index]))
        output_full2.append(output)

    for parent in output_full:

        if parent[2].find('남') != -1:
            boy += 1
        elif parent[2].find('여') != -1:
            girl += 1

        if int(parent[3]) < 30:
            age_20.append(parent[1]+':'+parent[3])
        elif int(parent[3]) < 40:
            age_30.append(parent[1]+':'+parent[3])
        if int(parent[3]) < 50:
            age_40.append(parent[1]+':'+parent[3])

        if parent[4].find("컴퓨터") != -1 or parent[4].find('통계') != -1:
            major_cnt += 1
        count += 1

    for parent in output_full2:

        if parent[1].find("python") != -1:
            cnt_python += 1
        if parent[2].find("상") != -1:
            cnt_level += 1
        if parent[0] != parent_test:
            lan_cnt += 1
        parent_test = parent[0]

    print("*전체 학생수:%d"%count)



con = MySQLdb.connect(host='localhost', port=3306, db='it_student2', user='root', passwd='1111', charset='utf8mb4')
mysql_set = con.cursor()
table_list = 'student_info'
table_language = 'student_languages'

while True:
    print("학생정보 db데이터 분석 시작..")
    input_data = input("1.요약정보 \n2.입력 \n3.조회 \n4.수정 \n5.삭제 \n6.종료 \n7.데이터입력 \n메뉴 입력: ")
    if input_data == '6':
        print("학생 정보 분석 완료!")
        quit()
    elif input_data == '1':
        sump_db()
    elif input_data == '1':
        sump_db()
    elif input_data == '1':
        sump_db()
    elif input_data == '1':
        sump_db()
    elif input_data == '1':
        sump_db()
    elif input_data == '1':
        sump_db()
