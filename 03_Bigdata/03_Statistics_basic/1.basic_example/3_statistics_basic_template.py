import csv
import math

def get_row_index(search_key):
    index=0
    return index;

def print_row(search_key):
    for row in big_data:
        if search_key in row:
            print(row)

def get_column_instance(column_name):
    col_instance=[]
    return col_instance

def print_column(column_name):
    for row in big_data:
        column =row.index(column_name)
        break
    for row in big_data:
        print(row[column])

def my_sum(column_name):
    total_sum = 0
    print_column(column_name)
    for row in big_data:
        column =row.index(column_name)
        break
    for row in big_data:
        if column_name not in row:
            print(row[column])
            total_sum += int(row[column])
    print(f'총 합은 {total_sum}입니다.')

def my_average(column_name):
    total_sum = 0
    count = 0
    print_column(column_name)
    for row in big_data:
        column =row.index(column_name)
        break
    for row in big_data:
        if column_name not in row:
            print(row[column])
            total_sum += int(row[column])
            count += 1
    average = total_sum / count
    print(f'총 합은 {total_sum}입니다.')
    print(f'총 갯수는 {count}입니다.')
    print("평균은 %.3f입니다."%average)

def my_max(column_name):
    temp = 0
    for row in big_data:
        column =row.index(column_name)
        break
    for row in big_data:
        if column_name not in row:
            print(row[column])
            max_value = int(row[column])
            if max_value > temp:
                number_one = max_value
                temp = max_value

    print(f'가장 큰 값은 {number_one}입니다.')
def my_min(column_name):
    temp = 1000
    for row in big_data:
        column =row.index(column_name)
        break
    for row in big_data:
        if column_name not in row:
            print(row[column])
            max_value = int(row[column])
            if max_value < temp:
                number_one = max_value
                temp = max_value

    print(f'가장 작은 값은 {number_one}입니다.')


def my_deviation(column_name):
    total_sum = 0
    count = 0
    deviation = ['표본','평균','편차']
    list = []
    for row in big_data:
        column =row.index(column_name)
        break
    for row in big_data:
        if column_name not in row:
            print(row[column])
            total_sum += int(row[column])
            count += 1
    average = total_sum / count
    print(deviation[0], deviation[1], deviation[2])
    for row in big_data:
        if column_name not in row:
            list = []
            list.append(row[column])
            list.append(average)
            list.append(float(row[column])-float(average))
            list_1 = round(list[1], 2)
            list_2 = round(list[2], 2)
            print(list[0], list_1, list_2)

def my_standard_deviation(column_name):
    pass
def my_variance(column_name):
    pass
def my_sorting (column_name):
    pass
def check_type(column_name):
    pass

with open('Demographic_Statistics_By_Zip_Code.csv', newline='') as inflie:
    big_data = list(csv.reader(inflie))

while True:
    print("<메뉴>")
    print("1.행 2.열 3.총합 4.평균 5.최대값 6.최소값 7.편차 8.분산 9.표준편차 10.정렬(오름차순,내림차순) 11.종료")
    menu = int(input("원하는 서비스를 입력하세요: "))

    if menu == 1:
        search_key = input("Access Key를 입력하세요: ")
        print_row(search_key)
    elif menu == 2:
        column_name = input("데이터 필드명을 입력하세요: ")
        print_column(column_name)
    elif menu == 3:
        column_sum = input("총 합을 구하고자 하는 데이터 필드명을 입력하세요: ")
        my_sum(column_sum)
    elif menu == 4:
        column_average = input("평균을 구하고자 하는 데이터 필드명을 입력하세요: ")
        my_average(column_average)
    elif menu == 5:
        column_max = input("최대값을 구하고자 하는 데이터 필드명을 입력하세요: ")
        my_max(column_max)
    elif menu == 6:
        column_min = input("최소값을 구하고자 하는 데이터 필드명을 입력하세요: ")
        my_min(column_min)
    elif menu == 7:
        column_deviation = input("최소값을 구하고자 하는 데이터 필드명을 입력하세요: ")
        my_deviation(column_deviation)
    elif menu == 8:
        column_variance = input("분산을 구하고자 하는 데이터 필드명을 입력하세요: ")
        my_variance(column_variance)
    elif menu == 9:
        my_standard_deviation()
    elif menu == 10:
        my_sorting()
    elif menu == 11:
        break
    else:
        print("잘못 입력하였습니다.다시 입력하세요.")

