def new_range(start, stop=None, step=None):
    if stop is None:
        stop = start
        start = 0
    if step is None:
        step = 1
    while start < stop:
        yield start
        start += step



for i in range(1, 1):
    print(i)

for j in new_range(1, 1):
    print(j)
