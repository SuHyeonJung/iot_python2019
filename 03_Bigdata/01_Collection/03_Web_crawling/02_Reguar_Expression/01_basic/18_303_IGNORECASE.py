import re
orginal_data = 'Life'
p = re.compile('[a-z]', re.I)
m = p.match(orginal_data)
print(m)
