print(f'{"hi":<10}')

a = '학생'

print("신분: ", a)

b =[]
c = {"hi":"hello", "good":"bad", 1 : 3}
f = {}
# print(c['hi'].values())
for index in c.keys():
    f[str(index)] = str(c[index])
print(f)
# d = {"hi":"hello", "good":"bad", "total":[{"high":"low"}]}
# e = d
# print(e)
# add = input("입력:")
# if add in d["total"][0].values():
#     print("학생: ",c['hi'])
# if add in d.values():
#     print("학생: ",c['hi'])