x = [1, 2, 3]
print(tuple(x[-1:]))
y = x
y.append(tuple(x[-1:]))
x[2] = 5
result = ''.join([str(elem) for elem in y])
print(result)
