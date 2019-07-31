import json

with open('대구_대기정보_가상.json', encoding='utf-8') as json_file:
    base_f = json.load(json_file)
    print(base_f)
# for index in base_f:
#     print(index)
#     base_tuple.append()
    # if int(index["pm25Value"]) > 1:
    #     print("hello")
    # elif int(index["pm25Value"]) < 1:
    #     print("hi")
