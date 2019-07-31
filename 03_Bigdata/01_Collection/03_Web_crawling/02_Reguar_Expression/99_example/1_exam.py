import re

data = 'abcdefBEERDF0123456789'

p = re.compile('[^a-zA-Z0-9]')
m = p.search(data)
print(m)
if m:print('true')
else:print('false')

data = '%^&$'

p = re.compile('[a-zA-Z0-9]')
m = p.search(data)
print(m)
if m:print('true')
else:print('false')
