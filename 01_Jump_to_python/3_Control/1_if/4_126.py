#coding: cp949

pocket = ['paper', 'cellphone','card']
#card = True
#if 'money' in pocket:
#    print("택시를 타고 가라")
#elif card:
#elif 'card' in pocket:
#    print("택시를 타고 가라")
#else: 
#    print("걸어 가라")

#if 'money' or 'credit_card' in pocket: 'money'은 상수형 문자열 객체로서
    #값이 있기 때문에 무조건 true를 반환한다.
    #따라서 pocket에 현금과 신용카드가 있는 조건을 표현하려면 아래와 같이
    #작성해야 한다. 이는 프로그램 중복으로 볼수는 없다.
if 'money' in pocket or 'credit_card' in pocket:
    print("택시를 타고 가라")
else:
    print("걸어 가라")
