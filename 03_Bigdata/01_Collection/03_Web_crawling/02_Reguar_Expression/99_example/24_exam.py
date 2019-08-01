import re

words = ["Python PHP", "Java JavaScript", "c c++"]

for i in words:
    m = re.match("(P\w+)\s(P\w+)", i)
    if m:
        print(m.groups())
