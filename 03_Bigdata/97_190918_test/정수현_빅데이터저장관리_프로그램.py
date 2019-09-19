# 분산 저장 v6
# 헤더파일 중복저장 되는 문제 해결
import csv
import os
from xlwt import Workbook

base_repository_name = 'Bigdata_Repository'
type_folder_1 = 'Type A'
type_folder_2 = 'Type B'
file_name = '시뮬레이션_남해군_관광지별_방문객'
dir_delimeter = '/'
file_format = 'csv'
simulation_count = 100
simulation_data = ['1111', '상주면', '남해군', '보리암', '1', '14137', '43677']
file_size_limit = 10000
dest_file_name = f'{base_repository_name}{dir_delimeter}{file_name}1.{file_format}'
file_size = 0
is_header = False
is_first = True

def config_modify(base_repository_name, file_name, file_format, file_size_limit):
    print("1.디렉토리명 초기값: ", base_repository_name)
    print("2.파일명 초기값: ", file_name)
    print("3.포멧 초기값(1.csv 2.xls): ", file_format)
    print("4.데이터 용량 제한(byte) 초기값: ", file_size_limit)
    print("5.이전메뉴")
    config = base_repository_name, file_name, file_format, file_size_limit
    return config

def getTourPoint_csv(filewriter):
    filewriter.writerow(simulation_data)
    return

def getTourPoint_exel(output_worksheet):
    output_worksheet.write(simulation_data)

def get_dest_file_name(file_index, base_repository_name, file_name, file_format):
    global is_header
    dest_file_name = f'{base_repository_name}{dir_delimeter}{file_name}{str(file_index)}.{file_format}'

    try:
        file_size = os.path.getsize(dest_file_name)
        print(f"'{dest_file_name}' file size: {file_size}")
        print(f"파일당 size 제한: {file_size_limit}")

        if file_size > file_size_limit:
            file_size = 0
            dest_file_name = f'{base_repository_name}{dir_delimeter}{file_name}{str(file_index+1)}.{file_format}'
            is_header = True
        else:
            is_header = False
    except:
        pass
    return dest_file_name

def save_file(file_index, base_repository_name, file_name, file_format, file_limit_size):
    dest_file_name = get_dest_file_name(file_index, base_repository_name, file_name, file_format)
    global is_header
    global is_first
    if file_format == 'csv':
        csv_out_file = open(dest_file_name, 'a', newline='')
        filewriter = csv.writer(csv_out_file)
        if is_header == True or is_first == True:
            header_list = ['addrCd', 'gungu', 'sido', 'resNm', 'rnum', 'csForCnt', 'csNatCnt']
            filewriter.writerow(header_list)
            is_first = False
            is_header = False

        for index in range(simulation_count):
            getTourPoint_csv(filewriter)
        csv_out_file.close()

    elif file_format == 'xls':
        output_workseet = Workbook().add_sheet(file_name)
        if is_header == True or is_first == True:
            header_list = ['addrCd', 'gungu', 'sido', 'resNm', 'rnum', 'csForCnt', 'csNatCnt']
            output_workseet.write(header_list)
            is_first = False
            is_header = False

        for index in range(simulation_count):
            getTourPoint_exel(output_workseet)

        Workbook().save(dest_file_name)


def file_count():
    index = len(os.listdir(base_repository_name))
    return index

def configuration(base_repository_name, file_name, file_format, file_size_limit):
    print("1.디렉토리명 초기값: ", base_repository_name)
    print("2.파일명 초기값: ", file_name)
    print("3.포멧 초기값(1.csv 2.xls): ", file_format)
    print("4.데이터 용량 제한(byte) 초기값: ", file_size_limit)
    print("5.이전메뉴")
    while True:
        sub_menu = input("환경설정 메뉴를 선택하세요: ")
        if sub_menu == '1':
            base_repository_name = input("디렉토리명 설정: ")
            config = config_modify(base_repository_name, file_name, file_format, file_size_limit)
        elif sub_menu == '2':
            file_name = input("파일명 설정: ")
            config = config_modify(base_repository_name, file_name, file_format, file_size_limit)
        elif sub_menu == '3':
            format_data = input("포멧 설정: ")
            config = config_modify(base_repository_name, file_name, format_data, file_size_limit)
        elif sub_menu == '4':
            data_volume = input("용량 설정: ")
            config = config_modify(base_repository_name, file_name, file_format, data_volume)
        elif sub_menu == '5':
            break
        else:
            print("잘못 입력하셨습니다. 다시 입력하세요.")
            continue
    return config


while True:
    print("1.환경설정(디렉토리명, 저장 방식...)")
    print("2.작업수행")
    print("3.종료")
    menu = input("메뉴를 선택하세요:")
    if menu == '1':
        config = configuration(base_repository_name, file_name, file_format, file_size_limit)
    elif menu == '2':
        if not os.path.exists(base_repository_name):
            os.mkdir(base_repository_name)

        if not os.path.exists(dest_file_name):
            save_file(1, config[0], config[1], config[2], config[3])
        else:
            save_file(file_count(), config[0], config[1], config[2], config[3])
    elif menu == '3':
        break
    else:
        print("잘못 입력하셨습니다. 다시 입력하세요.")


