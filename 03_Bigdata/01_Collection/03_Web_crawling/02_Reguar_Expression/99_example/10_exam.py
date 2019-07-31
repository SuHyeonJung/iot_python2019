import re
def check_text(text):
    pattern = r'\Ab'
    if re.search(pattern, text):
        return 'Found match'
    else:
        return 'Not match'

print(check_text('abbbbbc'))
print(check_text('abbbcAbbc'))
print(check_text('babbcb'))

