import re

p = re.compile('[a-z]+')
m = p.match('3 python')

print(m)
# if m:print('Match found: ', m.group())
# else:print('No match')

m = p.search('3 python')
print(m)
