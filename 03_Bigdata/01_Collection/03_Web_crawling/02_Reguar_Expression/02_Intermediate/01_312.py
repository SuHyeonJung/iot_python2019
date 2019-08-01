import re

p = re.compile('(ABC)+')
m = p.search('ABCABCABC OK?')
print(m)
print(m.group(0))
print(m.group())

p = re.compile('(정수현)+')
m = p.search('정수현정수현 OK? 정수현')
print(m)
print(m.group())
print(m.group(1))
