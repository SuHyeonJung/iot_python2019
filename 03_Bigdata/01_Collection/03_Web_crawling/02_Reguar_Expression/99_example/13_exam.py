import re
def check_text(text):
    pattern = '\Bz\B'
    if re.search(pattern, text):
        return 'Found match'
    else:
        return 'Not match'

print(check_text('The quick brown lazy dog.'))
print(check_text('Python Exercises.'))
print(check_text('babbAcb lze der '))

