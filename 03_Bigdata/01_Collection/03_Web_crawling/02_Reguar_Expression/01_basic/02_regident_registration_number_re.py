import re

data = """
park 800905-1049118
kim  700905-1059119
"""

pat = re.compile("(\d{6})[-]\d{7}")
print(pat)
print(pat.sub("\g<1>-*******", data))
data_1 = pat.sub("\g<1>-*******", data)
print(data_1)


