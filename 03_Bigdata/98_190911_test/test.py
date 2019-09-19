from operator import itemgetter

list = [['대구광역시 동구 용계동(동대구역네거리 인근)','62','0','19','39'],
['0','44','대구광역시 동구 효목동(큰고개오거리 인근)','11','33'],
['41','31','대구광역시 동구 신천동(신천네거리 인근)','07','01'],
]
list_1 = []
for i in list:
    list01 = i[0]
    list02 = i[1]
    list03 = i[2]
    list04 = i[3]
    list05 = i[4]
    list_1.append({list01, list02, list03, list04, list05})
for k in list_1:
    print(sorted(k))

