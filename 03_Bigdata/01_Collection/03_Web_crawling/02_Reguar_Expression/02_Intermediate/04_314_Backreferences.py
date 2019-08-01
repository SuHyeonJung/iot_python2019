import re
p = re.compile(r'(\b\w+)\s+\1')
# p = re.compile(r'(\w+)\s+\w+\s+\w+\s+\1')
# p = re.compile(r'(\w+)\s+\w+\s+\w+\s+\1')
# print(p.search('Paris in the the spring. it is was really great').group())
print(p.search('Paris in the spring spring. it is was really great').group())
