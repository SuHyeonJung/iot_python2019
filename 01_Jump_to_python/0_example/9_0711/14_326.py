list_1 = []
def compress(letter):
    for check in letter:
        a = letter.count(check)
        change = check+str(a)
        list_1.append(change)

    result = set(list_1)
    result_1 = list(result)
    print(''.join(result_1))



input_letter = input("문자열 입력: ")
compress(input_letter)