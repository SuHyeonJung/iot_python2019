import re
def check_text(text):
    pattern = re.compile("^5")
    if pattern.match(text):
        return 'True'
    else:
        return 'False'

print(check_text('5-2345861'))
print(check_text('6-2345861'))
print(check_text('55'))

