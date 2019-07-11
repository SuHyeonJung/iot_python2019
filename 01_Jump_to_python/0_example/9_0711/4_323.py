A = [20,55,67,82,45,33,90,87,100,25]
A = list(filter(lambda A: A >= 50, A))
print(A)
result = 0
for i in A[0:]:
    result = result + i
print(result)