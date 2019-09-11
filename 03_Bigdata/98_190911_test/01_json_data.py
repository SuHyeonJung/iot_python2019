import urllib.request
import datetime
import json
import csv
import sys
access_key="GSvfm5b9FmoYf6uKR%2Ftufw4y7ExGKO0j9LXOiMTO5ZPXbCtKqtfR76BJ64A94O5h6TBx5PFPZHl26bYBdwdFkA%3D%3D"

output_file = sys.argv[1]

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

def get_accident_URL(now_date, sido, gugun):
    end_point="http://apis.data.go.kr/B552061/frequentzoneLg/getRestFrequentzoneLg"

    parameters = "?serviceKey="+access_key
    parameters += "&searchYearCd="+str(now_date)
    parameters += "&siDo="+str(sido)
    parameters += "&guGun="+str(gugun)
    parameters += "&type=json"
    parameters += "&numOfRows=10&pageNo=1"
    url = end_point+parameters

    retData = get_Request_URL(url)


    if(retData == None):
        return None
    else:
        return json.loads(retData)

def Number_of_traffic_accident_Json(now_date, sido, gugun):

    jsonData = get_accident_URL(now_date, sido, gugun)
    index = 0
    json_accident_result = []
    for i in jsonData['items']['item']:
        location = jsonData['items']['item'][index]['spot_nm']
        losses = jsonData['items']['item'][index]['caslt_cnt']
        losses = str(losses)
        number_of_deaths = jsonData['items']['item'][index]['dth_dnv_cnt']
        number_of_deaths = str(number_of_deaths)
        number_of_injured = jsonData['items']['item'][index]['se_dnv_cnt']
        number_of_injured = str(number_of_injured)
        if len(number_of_injured) == 1:
            number_of_minor_injured = number_of_minor_injured.zfill(2)
        number_of_minor_injured = jsonData['items']['item'][index]['sl_dnv_cnt']
        number_of_minor_injured = str(number_of_minor_injured)
        json_accident_result.append({location, losses, number_of_deaths,
                                     number_of_injured, number_of_minor_injured})
        index = index + 1

    with open(output_file, 'w', newline='') as outfile:
        filewriter = csv.writer(outfile)
        header_list = ['number of deaths', 'number of injured',
                       'number of minor injured','losses','location']
        filewriter.writerow(header_list)
        for row in json_accident_result:
            row = sorted(row)
            filewriter.writerow(row)

    print('동구_2017년_사고_다발정보_서비스.csv SAVED\n')

def accident_Info():
    now_data = 2017
    sido = 27
    gugun = 140
    Number_of_traffic_accident_Json(now_data, sido, gugun)


accident_Info()



