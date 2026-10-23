def add(a, b):
    return a+b


def divide(a, b):
    if b==0:
        raise ValueError("Can't divide by 0")
    return a/b
