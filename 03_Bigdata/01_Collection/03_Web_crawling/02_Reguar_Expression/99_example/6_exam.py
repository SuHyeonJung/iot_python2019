import re
def check_text(text):
    pattern = 'ab{2,3}c'
    if re.search(pattern, text):
        return 'Found match'
    else:
        return 'Not match'

print(check_text('abbbbbc'))
print(check_text('abbbc'))
print(check_text('abbc'))
