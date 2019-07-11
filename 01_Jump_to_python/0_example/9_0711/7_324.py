multiplication_table = int(input("구구단을 출력할 숫자를 입력하세요(2~9): "))
result = 0
for index in range(1,10):
    result = multiplication_table * index
    print(result, end=' ')