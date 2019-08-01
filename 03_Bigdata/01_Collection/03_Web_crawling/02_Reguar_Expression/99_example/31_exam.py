import re
street = 'Python Exercises, PHP exercises.'
p = re.compile('[ ,.]')
m = p.sub(':',street)
print(m)
