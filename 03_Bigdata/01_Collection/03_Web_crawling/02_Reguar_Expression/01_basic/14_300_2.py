import re
original_text = 'life is too short'
p = re.compile('[a-z]+')
m = p.search(original_text)
print(m)

match_list = p.findall(original_text) # 검색결과는 list로 반환해준다.
print(match_list)
for match_element in match_list:
    print(match_element)
