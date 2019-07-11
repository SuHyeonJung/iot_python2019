sum = []
sum = list(map(int,input("숫자 입력: ").split(',')))
result = 0
for index in sum:
    result = result + index
print(result)

