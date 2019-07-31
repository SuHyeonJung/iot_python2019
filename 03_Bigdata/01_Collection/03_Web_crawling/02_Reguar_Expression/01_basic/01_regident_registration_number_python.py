data = """
park 800905-1049118
kim  700905-1059119
"""
print(data)
result = []
for index in data.split('\n'):
    word_result = []
    print(index)
    for word in index.split(" "):
        if len(word) == 14 and word[:6].isdigit() and word[7:].isdigit():
            word = word[:6] + "-" + "*******"
        word_result.append(word)
    result.append(" ".join(word_result))
print(result)
data_modify = "\n".join(result)
print(type(data_modify))
print(data_modify)


