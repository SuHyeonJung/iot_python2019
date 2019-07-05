
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
        for index in range(count, star_value):
            print(end =null*' ')
            print(star*'*')
            null = null - 1
            star = star + 2
print("프로그램을 종료하였습니다.")