import re
p = re.compile('^python\s\w+')
p = re.compile('^python\s\w+', re.MULTILINE)

dest_str = '''python one
life is too short
python two
'''
m = p.findall(dest_str)
print(m)