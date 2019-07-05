def avg_numbers(*args):
    result = 0
    for i in args:
        result = result + i
    return result / len(args)

result = avg_numbers(1, 2)
print(result)
b = avg_numbers(1, 2, 3, 4, 5)
print(b)