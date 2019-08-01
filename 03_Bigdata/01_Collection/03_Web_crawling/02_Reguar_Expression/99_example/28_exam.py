import re
text = "The following example creates an ArrayList with a capacity of 50 elements. Four element are then added to the ArrayList and the ArrayList is trimmed accordingly."

result = re.compile("[ae]\w+")
m = result.findall(text)
print(m)
# for element in m:
#     print(element)
# result_1 = re.split("\d+", text)
# for i in result_1:
#     print(i)
