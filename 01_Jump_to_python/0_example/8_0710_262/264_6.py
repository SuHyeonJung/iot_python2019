def mul(x): return x * 3
print(list(map(mul, [1, 2, 3, 4])))
print(list(map(lambda x: x * 3, [1,2,3,4])))