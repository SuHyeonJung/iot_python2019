import re
def check_text(text):
    pattern = '^[a-z]+_[a-z]+$'
    if re.search(pattern, text):
        return 'Found match'
    else:
        return 'Not match'

print(check_text('abbb_bbc'))
print(check_text('abbbc_Abbc'))
print(check_text('ABC_abbcb'))

