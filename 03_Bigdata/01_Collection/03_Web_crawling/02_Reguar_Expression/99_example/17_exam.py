import re
def check_text(text):
    pattern = re.compile(".*[0-9]$")
    if pattern.match(text):
        return 'True'
    else:
        return 'False'

print(check_text('abcdef5'))
print(check_text('advdv'))
print(check_text('55'))

