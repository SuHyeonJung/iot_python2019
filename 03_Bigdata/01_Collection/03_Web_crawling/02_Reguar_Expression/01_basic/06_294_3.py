import re

p = re.compile('[\d]') #[0-9]
m = p.match('1')
print(m)
m = p.match('a')
print(m)


p = re.compile('[\D]') #[0-9]
m = p.match('1')
print(m)
m = p.match('a')
print(m)
m = p.match('   a')
print(m)

p = re.compile('[\s]') #[0-9]
m = p.match('   1')
print(m)
m = p.match('a')
print(m)
m = p.match('-')
print(m)
m = p.match('''
''')
print(m)


p = re.compile('[\S]') #[0-9]
m = p.match('   1')
print(m)
m = p.match('1')
print(m)
m = p.match('-')
print(m)

p = re.compile('[\w]') #[0-9]
m = p.match('   1')
print(m)
m = p.match('a')
print(m)
m = p.match('1')
print(m)
m = p.match('-')
print(m)


p = re.compile('[\W]') #[0-9]
m = p.match('   1')
print(m)
m = p.match('-')
print(m)
