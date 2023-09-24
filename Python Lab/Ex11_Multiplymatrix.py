def multiply(a, b):
    c = [[0] * len(b)] * len(a[0])

    for i in range(0, len(a)):
        for j in range(0, len(b[0])):
            res = 0
            for k in range(0, len(b)):
                res += a[i][k] * b[k][j]
            c[i][j] = res
            print(c[i][j])
    
    return c

a = [[1, 2, 3],
     [1, 1, 1],
     [1, 1, 1]]

b = [[1, 1, 1],
     [1, 1, 1],
     [1, 1, 1]]

c = multiply(a, b)
for i in range(0, len(c)):
    for j in range(0, len(c[0])):
        print(c[i][j])

print(c)