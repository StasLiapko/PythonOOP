def my_range(start, stop = None, step = 1):
    if stop is None:
        stop = start
        start = 0

    current = start
    while current < stop if step > 0 else current > stop:
        yield current
        current += step


for i in my_range(2, 30, 3):
    print(i)

print("Second example")

for i in my_range(50, 2, -5):
    print(i)