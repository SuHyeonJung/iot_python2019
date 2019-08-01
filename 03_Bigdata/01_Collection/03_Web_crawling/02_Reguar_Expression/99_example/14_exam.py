import re
def check_text(text):
    pattern = '^[a-zA-Z0-9_]*$'
    if re.search(pattern, text):
        return 'Found match'
    else:
        return 'Not match'

print(check_text('The_Quick_brown_lazy dog5'))
print(check_text('Python_Exercises_1'))
print(check_text('i_Need_water_3'))

