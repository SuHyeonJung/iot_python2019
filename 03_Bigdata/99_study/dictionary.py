list = ['사과','배','수박','사과','참외','수박','바나나']
d= {}

for i in list:
    if i not in d:
        d[i] = 1
    else:
        d[i] = d[i] + 1

print(d)