import re
pattern = 'exercises'
sample_text = 'Python exercises, PHP exercises, C# exercises'
for match in re.findall(pattern, sample_text):
    print(match)

