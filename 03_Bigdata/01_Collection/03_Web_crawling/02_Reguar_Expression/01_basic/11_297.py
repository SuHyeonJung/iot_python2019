import re

p = re.compile('ab?c')
m = p.match('abc')
print(m)
m = p.match('abbc')
print(m)


p = re.compile('1')
m = p.match('1')
print(m)
p = re.compile('a')
m = p.match('abc')
print(m)
