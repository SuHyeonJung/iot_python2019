import re
p = re.compile('ca*t')
m = p.match('ct')
print(m)
m = p.match('cat')
print(m)
m = p.match('caaat')
print(m)

p = re.compile('go*gle')
m = p.match('ggle')
print(m)


