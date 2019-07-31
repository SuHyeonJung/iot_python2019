import re
p = re.compile('[a-z]+')
m = p.match('ppytaaahon')
print(m)
p = re.compile('[a-z]')
m = p.match('ppytaaahon')
print(m)

