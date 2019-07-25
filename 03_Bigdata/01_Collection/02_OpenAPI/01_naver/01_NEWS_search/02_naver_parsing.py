import json
import operator

news_domain_all_list = []
domain_info_list = []
num_of_corrupted_data=0

with open('아베_naver_news.json', encoding='utf-8')as json_file:
    json_data_load = json.load(json_file)
print(json_data_load[0])
print(json_data_load[0]["org_link"])
print("데이터 분석을 시작합니다..")
count = 0
a=0
incorrect_count = 0
total_count = 0
number = 1
domain_count = 0
org_list = []
for number in json_data_load:
    count = count + 1
for index in range(0, 900):
    if json_data_load[index]["org_link"] == "":
        print("'org_link'가 없는 기사를 발견했습니다.")
        incorrect_count = incorrect_count + 1
    try:
        org_list.append(json_data_load[index]["org_link"].split('/')[2])
    except:
            pass
overap_list = set(org_list)
for j in overap_list:
    domain_count = domain_count + 1
print("<네이버 검색 빅데이터 분석>")
print("검색어: 아베")
print("전체 도메인 수: %d"% domain_count)
print("전체 건수: %d"% (count-incorrect_count))
print("부정확한 데이터수: %d" %incorrect_count)
print("- 도메인 별 뉴스 기사 분석")
final_dic = {}
for k in org_list:
    # final_dic[k] = org_list.count(k)
    final_dic[org_list.count(k)]= k
# final_dic2 = sorted(final_dic, key=lambda k: final_dic[k].reverce=True)
# print(final_dic)
# print(sorted_list.reverse())
# total_list = sorted_list.reverse()
# print(total_list)
final_dic_1 = {}
for f in sorted(final_dic):
    print(final_dic[f], ":", f, "건")
    final_dic_1[final_dic[f]] = f
print(final_dic_1)
# final_dic2 = sorted(final_dic_1.items(), key=lambda x:x[1], reverse=True)
# num  = 0
# # num_1 = 1
# # for g in final_dic2:
#     print(g[num][num_1], ":", "건")
#     num = num + 1
