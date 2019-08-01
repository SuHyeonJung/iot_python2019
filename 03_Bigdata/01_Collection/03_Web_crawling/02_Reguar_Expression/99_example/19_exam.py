import re
patterns = ['fox', 'dog', 'horse']
sample_text = 'The quick brown fox jumps over the lazy dog.'

for pattern in patterns:
    print('Searching for "%s" in "%s" ->' % (pattern, sample_text))
    if re.search(pattern, sample_text):
        print('Matched!')
    else:
        print('Not matched!')


