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
        end = int(odd / 2)
        mirror = int(odd / 2)
        star = odd - 2
        k = mirror - 1
        j = 1
        while end >= 1:
            while k < mirror:
                print(end=' ')
                k = k + 1
            print(star*'*')
            star = star - 2
            end = end - 1
            j = j + 1
            k = k - j
print("프로그램을 종료합니다.")