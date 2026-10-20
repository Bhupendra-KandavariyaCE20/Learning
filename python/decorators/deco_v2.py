def decorator_(func):
    def wrapper(*args, **kwargs):
        print("Starting initialization of the function")
        y =  func(*args, **kwargs)
        print("Function initialization completed")
        return y
    return wrapper



def sum_v2(a, b):
    print(f"mult v2 of {a} and {b}")
    return a*b


wrap = decorator_(sum_v2)
print("Print statement before calling wrap and after declaring wrap")
print(wrap(2,5))


@decorator_
def sum_v3(a, b):
    print(f"Mult v3 of {a} and {b}")
    return a*b

print("Print statement of v3 deco")
print(sum_v3(2,5))
