def my_generator():
    n = 0

    n += 2
    yield n

    n  += 2
    yield n

    n += 2
    yield n

    n += 2
    yield n


obj = my_generator()
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
