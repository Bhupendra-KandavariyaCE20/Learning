lazy_gen = ( x**2 for x in range(10000))

first_val = next(lazy_gen)
print(first_val)

second_cal = next(lazy_gen)
print(second_cal)

