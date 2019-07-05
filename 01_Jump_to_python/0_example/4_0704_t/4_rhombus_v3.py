odd = 0
while True:
    odd = int(input("홀수를 입력하세요(0 <- 종료): "))
    value = int(odd / 2)
    second_end = value + 1
    if odd == 0:
        break
    elif odd % 2 == 0:
        print("잘못 입력하셨습니다.다시 입력하세요.")
    else:
        number = 0
        star = 1
        print(end=' ')
        print(odd*'-')
        for index in range(number, second_end):
            print('|', end = '')
            count = 0
            for second_index in range(count, value):
                print(end=' ')
                count = count + 1
            print(star*'*', end = value*' ')
            value = value - 1
            number = number + 1
            star = star + 2
            print('|')

        number = 0
        value = int(odd / 2)
        second_star = odd - 2
        k = 2
        second_value = value - 1
        count = 1
        for index in range(number, value):
            print('|', end = '')
            for second_index in range(second_value, value):
                print(end=' ')
                second_value = second_value + 1
            print(second_star*'*', end = count*' ')
            count = count + 1
            second_value = second_value - k
            second_star = second_star - 2
            k = k + 1
            number = number + 1
            print('|')
        print(end=' ')
        print(odd*'-')
print("프로그램을 종료합니다.")