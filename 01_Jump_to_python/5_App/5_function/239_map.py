def two_times(numberlist):
    result = []
    for number in numberlist:
        result.append(number*2)
    return result

print(two_times([1,2,3,4]))

def two_times(x): return x*2

print(list(map(two_times, [1,2,3,4])))
