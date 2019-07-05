while True:
    odd_number = int(input("홀수를 입력하세요(0 <- 종료): "))
    null = int(odd_number / 2)
    star_value = int(odd_number / 2) + 1
    count = 0
    star = 1
    if odd_number == 0:
        break
    elif odd_number % 2 == 0:
        print("짝수를 입력하였습니다. 다시 입력하세요")
    else:
        odd_number1 = odd_number
        print(" "+odd_number*'-')
        for index in range(count, star_value):
            print(end ='|'+null*' ')
            print(star*'*'+null*' '+'|')
            null = null - 1
            star = star + 2
        null = int(odd_number / 2)
        count = 0
        star = 1
        for descending in range(count, null):
            odd_number = odd_number - 2
            print(end ='|'+star*' ')
            print(odd_number*'*'+star*' '+'|')
            star = star + 1
        print(" "+odd_number1*'-')

print("프로그램을 종료하였습니다.")