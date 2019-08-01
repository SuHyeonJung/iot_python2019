import re
street = '21 Ramkrishna Road'
p = re.compile('Road$')
m = p.sub('Rd.',street)
print(m)
print(re.sub('Road$', 'Rd.', street))
