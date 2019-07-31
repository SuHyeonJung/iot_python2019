import re
def text_match(text):
    pattern = 'ab*?'
    if re.search(pattern, text):
        return 'Found a match'
    else:
        return  'Not match'

print(text_match('ac'))
print(text_match('a'))
