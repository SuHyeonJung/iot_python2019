f = open('test1.txt', 'w')
f.write("Life is too short\nyou need java")
f.close()

f = open('test1.txt', 'r')
body = f.read()
print(body)
f.close()
body = body.replace("java", "python")

f = open('test1.txt', 'w')
f.write(body)
f.close()