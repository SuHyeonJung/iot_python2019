input_number = []
count = 0
input_number = input("입력: ").split(' ')
# print(input_number)
# print(input_number[0][0])
# print(len(input_number[0][:]))

for index in range(0, len(input_number)):
    for line in range(0, len(input_number[index][:-1])):
        if input_number[index][line] == input_number[index][line+1] or input_number[index][0] == input_number[index][line+1]:
            count = count + 1
    if count > 0:
        print("False", end=' ')
    else:
        print("True", end=' ')

