odd = 0
while True:
    odd = int(input("홀수를 입력하세요(0 <- 종료): "))
    end = int(odd / 2)
    second_end  = end + 1
    if odd == 0:
        break
    elif odd % 2== 0:
        print("잘못 입력하셨습니다.다시 입력하세요.")
    else:
        count = 1
        i = 1
        while second_end > 0:
            while end != 0:
                print(end=' ')
                end = end - 1
            end = int(odd /2) - i
            print(count*'*')
            count = count + 2
            second_end = second_end - 1
            i = i + 1
print("프로그램을 종료합니다.")
