import urllib.request
import datetime
import json
import time

access_key="GSvfm5b9FmoYf6uKR%2Ftufw4y7ExGKO0j9LXOiMTO5ZPXbCtKqtfR76BJ64A94O5h6TBx5PFPZHl26bYBdwdFkA%3D%3D"


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

def get_Weather_URL(now_date, day_time):
    end_point="http://newsky2.kma.go.kr/service/SecndSrtpdFrcstInfoService2/ForecastTimeData"

    parameters = "?_type=json&ServiceKey="+access_key
    parameters += "&base_date="+str(now_date)
    parameters += "&base_time="+str(day_time)
    parameters += "&nx="+x_coodinate
    parameters += "&ny="+y_coodinate
    url = end_point+parameters

    retData = get_Request_URL(url)


    if(retData == None):
        return None
    else:
        return json.loads(retData)

def Make_Weather_Json(now_date, day_time):

    jsonData = get_Weather_URL(now_date, day_time)
    index = 0
    for i in jsonData['response']['body']['items']['item']:
        if (jsonData['response']['header']['resultMsg'] == 'OK'):
            searchtime = jsonData['response']['body']['items']['item'][index]["baseTime"]
            yyyymmdd = jsonData['response']['body']['items']['item'][index]["baseDate"]
            category = jsonData['response']['body']['items']['item'][index]["category"]
            fcstdate = jsonData['response']['body']['items']['item'][index]["fcstDate"]
            fcsttime = jsonData['response']['body']['items']['item'][index]["fcstTime"]
            fcstvalue = jsonData['response']['body']['items']['item'][index]["fcstValue"]
            nx = jsonData['response']['body']['items']['item'][index]["nx"]
            ny = jsonData['response']['body']['items']['item'][index]["ny"]
            json_weather_result.append({'baseDate': yyyymmdd, 'baseTime': searchtime,
                                    'category': category, 'fcstDate': fcstdate,
                                    'fcstTime': fcsttime, 'fxstValue': fcstvalue,
                                        'nx': nx, 'ny': ny})
            index = index + 1

    with open('동구_신암동_초단기예보조회_%s%s.json'%(now_date,day_time),'w',
              encoding='utf8') as outfile:
        retJson = json.dumps(json_weather_result, indent=4, sort_keys=True, ensure_ascii=False)
        outfile.write(retJson)

    print('동구_신암동_초단기예보조회_%s_%s.json SAVED\n' % (now_date, day_time))

def get_Realtime_Weather_Info():
    now_data = 20190729
    day_time = 1230
    Make_Weather_Json(now_data, day_time)

json_weather_result = []

x_coodinate = "89"
y_coodinate = "91"

get_Realtime_Weather_Info()



