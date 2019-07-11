fibonacci_one = 0
fibonacci_two = 1
absolute = int(input("정수를 입력하세요: "))

print(fibonacci_one)
print(fibonacci_two)
while True:
    fibonacci_three = fibonacci_one + fibonacci_two
    temp = fibonacci_two
    fibonacci_two = fibonacci_three
    fibonacci_one = temp
    if fibonacci_three > absolute:
        break
    print(fibonacci_three)
