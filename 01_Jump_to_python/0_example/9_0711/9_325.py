f = open("sample.txt", 'r')
point = f.readlines()
result = 0
average = 0
f.close()
print(point)
for index in point:
    result = result + int(index.rstrip())
    average = result / 10
print(result)
print(average)
