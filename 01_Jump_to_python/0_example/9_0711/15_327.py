input_number = []
count = 0
input_number = input("입력: ").split(' ')

for index in input_number:
    if len(index) != 10 :
        count = count + 1
    for line in index:
        if index.count(line) > 1:
            count = count + 1

    if count > 0:
        print("False", end=' ')
    else:
        print("True", end=' ')
    count = 0
