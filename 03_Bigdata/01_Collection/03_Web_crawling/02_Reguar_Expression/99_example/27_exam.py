import re
text = "Ten 10, Twenty 20, Thirty 30"
result = re.compile("\D+")
m = result.split(text)
print(m)
# for element in m:
#     print(element)
# result_1 = re.split("\d+", text)
# for i in result_1:
#     print(i)
