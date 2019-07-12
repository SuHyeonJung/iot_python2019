def DashInsert(number):
    list = []
    for index in range(0,len(number)-1):
        list.append(number[index])
        if int(number[index]) % 2 == 0 and int(number[index+1]) % 2 == 0:
            list.append('*')
        elif int(number[index]) % 2 == 1 and int(number[index+1]) % 2 == 1:
            list.append('-')
    list.append(number[len(number)-1])
    return ','.join(list)

number = input("입력: ")
print(DashInsert(number))