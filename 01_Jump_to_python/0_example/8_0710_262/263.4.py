def positive(x):
    return x > 0

print(list(filter(positive, [1,-2,3,-5,8,-3])))

print(list(filter(lambda x: x >0, [1, -2, 3, -5, 8, -3])))