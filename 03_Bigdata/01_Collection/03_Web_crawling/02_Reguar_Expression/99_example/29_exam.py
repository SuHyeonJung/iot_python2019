import re
text = "The following example creates an ArrayList with a capacity of 50 elements. Four element are then added to the ArrayList and the ArrayList is trimmed accordingly."

result = re.compile("\d+")
m = result.finditer(text)
print(m)
for i in m:
    print(i.group())
    print("Index position:", i.start())
# for element in m:
#     print(element)
# result_1 = re.split("\d+", text)
# for i in result_1:
#     print(i)
