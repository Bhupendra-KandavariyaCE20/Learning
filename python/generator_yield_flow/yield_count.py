def count_to_3():
    print("Intitalizing 1")
    yield 1
    print("Intitalizing 2")
    yield 2

counter  = count_to_3()
print(next(counter))
