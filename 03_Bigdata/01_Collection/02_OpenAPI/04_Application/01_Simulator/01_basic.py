import time
import urllib.request
import datetime
import json
import threading
import ctypes


access_key="GSvfm5b9FmoYf6uKR%2Ftufw4y7ExGKO0j9LXOiMTO5ZPXbCtKqtfR76BJ64A94O5h6TBx5PFPZHl26bYBdwdFkA%3D%3D"
g_Radiator = False
g_Gas_Valve = False
g_Balcony_Windows = True
g_Door = False
g_AI_Mode = False
json_air_result = []
location = '대구'
json_unique_result = []
schedule_cycle = 5
simulation_list = []

def print_main_menu():
    print("\n1. 장비상태 확인")
    print("2. 장비 제어")
    print("3. 스마트모드")
    print("4. 시뮬레이션모드")
    print("5. 프로그램 종료")

def terminate_ai_mode():
    """Terminates a python thread form another thread.
    :param thread: a threading.thread instance
    """
    if not ai_scheduler.isAlive():
        return
    exc = ctypes.py_object(SystemExit)
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(
        ctypes.c_long(ai_scheduler.ident), exc)
    if res == 0:
        raise ValueError("nonexistent thread id")
    elif res > 1:
        # """if it returns a number greater than one, you`re in trouble,
        # and you should call it again with exc=NULL to revert the effect"""
        ctypes.pythonapi.PyThreadState_SetAsyncExc(ai_scheduler.ident, None)
        raise SystemError("PyThreadState_SetAsyncExc failed")

def update_scheduler(air_poll):
    global g_Balcony_Windows
    air_pollution = air_poll[0]["pm25Value"]
    while True:
        time.sleep(schedule_cycle)
        print(f"스케줄러 작동.. {schedule_cycle}초 주기")
        if int(air_pollution) >= 1 and g_Balcony_Windows == True:
            print("미세먼지로 인해 창문 상태를 체크합니다.")
            check_device_status()
            g_Balcony_Windows = not g_Balcony_Windows
            print("창문을 닫습니다.")
        elif int(air_pollution) < 1 and g_Balcony_Windows!= True:
            g_Balcony_Windows = not g_Balcony_Windows
            print("창문을 엽니다.")
        else:
            print("조건이 만족하지 않아 아무런 작동을 하지 않습니다.")
def print_device_status(device_name, device_status):
    print("%s 상태: "% device_name, end= "")
    if device_status == True : print("열림")
    else: print("닫힘")

def check_device_status():
    print('')
    print_device_status('난방기', g_Radiator)
    print_device_status('가스밸브', g_Gas_Valve)
    print_device_status('발코니(베란다) 창문', g_Balcony_Windows)
    print_device_status('출입문 상태', g_Door)

def print_device_menu():
    print("\n상태 변경할 기기를 선택하세요.")
    print("1. 난방기")
    print("2. 가스밸브")
    print("3. 발코니(베란다)창")
    print("4. 출입문")

def control_device():
    global g_Radiator, g_Gas_Valve, g_Balcony_Windows, g_Door

    check_device_status()
    print_device_menu()
    menu_num = int(input("번호를 입력하세요: "))

    if menu_num == 1: g_Radiator = not g_Radiator
    if menu_num == 2: g_Gas_Valve = not g_Gas_Valve
    if menu_num == 3: g_Balcony_Windows = not g_Balcony_Windows
    if menu_num == 4: g_Door = not g_Door

    check_device_status()

def get_Request_URL(url):
    req = urllib.request.Request(url)

    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            print("[%s] Url Request Success"% datetime.datetime.now())
            return response.read().decode('utf-8')
    except Exception as e:
        print(e)
        print("[%s] Error for URL : %s" % (datetime.datetime.now(), url))
        return None

def get_air_pollution_URL():
    end_point = "http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty"

    parameters = "?serviceKey=" + access_key
    parameters += "&sidoName=%s" % urllib.parse.quote(location)
    parameters += "&_returnType=json"
    url = end_point + parameters

    retData = get_Request_URL(url)

    if (retData == None):
        return None
    else:
        return json.loads(retData)

def get_realtime_weather_info():
    global g_Radiator, g_Gas_Valve, g_Balcony_Windows, g_Door

    json_air_result = get_air_pollution_URL()

    index = 0

    for i in json_air_result["list"]:
        if json_air_result['list'][index]['stationName'] == '신암동':
            json_unique_result.append(json_air_result['list'][index])
        index = index + 1
    update_scheduler(json_unique_result)

def smart_mode():
    global g_AI_Mode
    print("1. 인공지능 모드 조회")
    # print("2. 인공지능 모드 상태 변경")
    print("2. 실시간 기상정보 Update 및 인공지능 작동")
    menu_num = int(input("메뉴를 선택하세요: "))

    if menu_num == 1:
        print("현재 인공지능 모드: ", end='')
        if g_AI_Mode == True:
            print("작동 완료!")
        else:
            print("중지!")
    # if menu_num == 2:
    #     print("현재 인공지능 모드: ", end='')
    #     g_AI_Mode = not g_AI_Mode
    #     if g_AI_Mode == True:
    #         ai_scheduler = threading.Thread(target=update_scheduler)
    #         ai_scheduler.daemon = True
    #         ai_scheduler.start()
    #         print("작동 완료!")
    #     else:
    #         ai_sceduler  = threading.Thread(target=update_scheduler)
    #         while ai_sceduler.is_alive():
    #             try:
    #                 terminate_ai_mode()
    #             except:
    #                 pass
    #         print("정지 완료!")

    elif menu_num == 2:
        get_realtime_weather_info()

def simulation_mode():
    global g_Balcony_Windows
    f = open('대구_대기정보_가상.json', 'r', encoding='utf8')
    base_f = f.readlines()

    if int(base_f['pm25Value']) < 1 and g_Balcony_Windows != True:
        while True:
                time.sleep(schedule_cycle)
                print(f"스케줄러 작동.. {schedule_cycle}초 주기")
                if int(index['pm25Value']) >= 1 and g_Balcony_Windows == True:
                    print("미세먼지로 인해 창문 상태를 체크합니다.")
                    check_device_status()
                    g_Balcony_Windows = not g_Balcony_Windows
                    print("창문을 닫습니다.")
                elif int(index['pm25Value']) < 1 and g_Balcony_Windows != True:
                    g_Balcony_Windows = not g_Balcony_Windows
                    print("창문을 엽니다.")
                else:
                    print("조건이 만족하지 않아 아무런 작동을 하지 않습니다.")

print("<스마트 홈네트워크 시뮬레이션 프로그램 ver 1.0>")
print("                              - 이 현 구 -")

while True:
    print_main_menu()
    menu_num = int(input("메뉴를 선택하세요: "))

    if menu_num == 1:
        check_device_status()
    elif menu_num == 2:
        control_device()
    elif menu_num == 3:
        smart_mode()
    elif menu_num == 4:
        simulation_mode()
    elif menu_num == 5:
        break


