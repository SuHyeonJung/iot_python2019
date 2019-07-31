import re
def check_text(text):
    pattern = 'ab?'
    if re.search(pattern, text):
        return 'Found match'
    else:
        return 'Not match'

print(check_text('ac'))