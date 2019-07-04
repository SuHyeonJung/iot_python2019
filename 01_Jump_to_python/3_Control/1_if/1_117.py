#coding: cp949
print("기본 if문법")
money = False

#if money:
#print("택시를 타고 가라") # if이하에는 반드시 1개 이상의 statement가 있어야 한다.

#if money:
    print("택시를 타고 가라") 
# print("택시를 타고 가라") indentation은 공백,탭 모두 허용한다.


#if money:
#    print("현금이 있는 것으로 확인 되었습니다")#동일한 indentation으로 
#    print("택시를 타고 가라") # 구성된 statement는 같은 statement block을
                                # 형성한다.
#if money:
#   print("현금이 있는 것으로 확인 되었습니다")
#    print("택시를 타고 가라")# 동일한 indentation을 맞추어야 한다.

if money:
    print("현금이 있는 것으로 확인 되었습니다")
    print("택시를 타고 가라") 
else:
    print("현금이 없는 것으로 확인 되었습니다")
    print("걸어 가라")
print("프로그램 종료")#최상위 레벨의 statement(if와 else문과 상관없음)

