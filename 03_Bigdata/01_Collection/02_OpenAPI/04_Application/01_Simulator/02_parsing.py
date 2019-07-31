import time
import urllib.request
import datetime
import json

access_key="GSvfm5b9FmoYf6uKR%2Ftufw4y7ExGKO0j9LXOiMTO5ZPXbCtKqtfR76BJ64A94O5h6TBx5PFPZHl26bYBdwdFkA%3D%3D"
location = '대구'
json_air_result = []
json_unique_result = []
def get_Request_URL(url):
    req = urllib.request.Request(url)

    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            print("[%s] Url Request Success = %s "% (datetime.datetime.now(), url))
            return response.read().decode('utf-8')
    except Exception as e:
        print(e)
        print("[%s] Error for URL : %s" % (datetime.datetime.now(), url))
        return None

def get_air_pollution_URL():
    end_point="http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty"

    parameters = "?serviceKey="+access_key
    parameters += "&sidoName=%s"% urllib.parse.quote(location)
    parameters += "&_returnType=json"
    url = end_point+parameters

    retData = get_Request_URL(url)


    if(retData == None):
        return None
    else:
        return json.loads(retData)

json_air_result = get_air_pollution_URL()
index = 0

for i in json_air_result["list"]:
    if json_air_result['list'][index]['stationName'] == '신암동':

        json_unique_result.append(json_air_result['list'][index])
    index = index + 1

with open('대구_대기정보.json','w',encoding='utf8') as outfile:
    retJson = json.dumps(json_unique_result, indent=4, sort_keys=True, ensure_ascii=False)
    outfile.write(retJson)

print('대구_대기정보.json SAVED\n')