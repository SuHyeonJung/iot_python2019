import re
original_text = """a1 ajfkljdfkaljf
b3 djalkjfkslafj
3k dajsfkljkfafjd
5j djfkaldsjfklajldf
k4 dafjkljflka
9p fjkdasjfkaldjfakl
u9 adsjfklajfdk
"""

p = re.compile('[a-zA-Z0-9][0-9]')
m = p.match(original_text)
print(m)

