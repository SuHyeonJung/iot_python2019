import re
pattern = 'exercises'
sample_text = 'Python exercises, PHP exercises, C# exercises'
for match in re.finditer(pattern, sample_text):
    s = match.start()
    e = match.end()
    print('Found "%s" at %d:%d' % (sample_text[s:e], s, e))

