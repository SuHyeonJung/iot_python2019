import re
patterns = 'fox'
sample_text = 'The quick brown fox jumps over the lazy dog.'
match = re.search(patterns, sample_text)
s = match.start()
e = match.end()
print('Found "%s" in "%s" form %d to %d ' % (patterns, match.string, s, e))

