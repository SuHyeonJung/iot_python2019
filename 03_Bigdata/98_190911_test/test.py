from operator import itemgetter

list = [['대구광역시 동구 용계동(동대구역네거리 인근)','62','0','19','39'],
['0','44','대구광역시 동구 효목동(큰고개오거리 인근)','11','33'],
['41','31','대구광역시 동구 신천동(신천네거리 인근)','07','0'],
]
list_1 = '7'
print(len(list_1))
if len(str(list_1)) == 1:

    list_1 = list_1.zfill(2)
    print(list_1)
# for temp in list:
#     print(temp.sort())
#     print(sorted(temp))
    # list_1.append(sorted(temp))
# for i in list_1:
#     i.reverse()
#     print(i)
# print(list_1)
# list.sort(key=itemgetter(2), reverse=True)
