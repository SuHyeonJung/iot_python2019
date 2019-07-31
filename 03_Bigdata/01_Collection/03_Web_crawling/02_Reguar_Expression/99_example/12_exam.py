import re
def check_text(text):
    pattern = '[z]+'
    if re.search(pattern, text):
        return 'Found match'
    else:
        return 'Not match'

print(check_text('abbbbbc.'))
print(check_text('abbbczbbc '))
print(check_text('babbAcb. '))

