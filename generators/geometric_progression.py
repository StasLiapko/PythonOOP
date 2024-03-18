def geometric_progression(x, y):
    temp = x
    while True:
        yield temp
        temp *= y
        
generator = geometric_progression(4, 3)

for _ in range(5):
    print(next(generator))