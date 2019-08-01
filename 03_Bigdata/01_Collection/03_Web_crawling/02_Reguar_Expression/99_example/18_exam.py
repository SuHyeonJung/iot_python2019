import re
result = re.finditer("([0-9]{1,3})", "Exercises number 1, 12, 13 and 345 are 6789")
for n in result:
    print(n.group((0)))
