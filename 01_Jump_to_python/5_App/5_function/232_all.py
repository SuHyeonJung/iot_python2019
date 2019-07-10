# all은 iterable 객체 (2개 이상의 값을 담을 수 있는 자료형)에 적용가능하다.
# all 함수는 입력받은 데이터의 정합성을 체크할 때 사용할 수 있다.
print(all([1,2,3]))
print(all([1,2,0]))
print(all(['hello','world']))
print(all(['hello',' ']))
print(all(['hello','']))
print(all((1,2)))
print(all((1,0)))
print(all({'조문수':'남','김혜경':'여'}))
print(all({}))
print(all([1,'2',0.0]))

result = [1,2,3].append(4)
print(result)
print([1,2,3].append(4))
result = [1,2,3]
result.append(4)
print(result)
