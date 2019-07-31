import re
def check_text(text):
    pattern = 'ab{3}c'
    if re.search(pattern, text):
        return 'Found match'
    else:
        return 'Not match'

print(check_text('abbbc'))
print(check_text('abbc'))
print(check_text('abbbbc'))
