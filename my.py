def generator(n):
    a, b = 0, 1
    for i in range (1, n + 1):
        yield a
        a, b = b, a + b


for i in generator(10):
    print(i)