#coding: cp949
age = 0

while True: 
    age = int(input("���̸� �Է��ϼ���: "))
    if age < 4 or age > 65:
        print("����� 0���Դϴ�.")
    elif age > 3 and age < 14:
        print("����� 2000���Դϴ�.")
    elif age > 13 and age < 19:
        print("����� 3000���Դϴ�.")
    elif age > 18 and age < 65:
        print("����� 5000���Դϴ�.")

