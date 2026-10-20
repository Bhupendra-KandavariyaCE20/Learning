from functools import wraps

def repeat_ntimes(n: int):
    def deco(my_func):
        def wrapper(*args, **kwargs):
            print('Wrapper init')
            result = []
            for i in range(n):
                result.append(my_func(*args, **kwargs))
            print('Wrapper end')
            return result
        return wrapper
    return deco


@repeat_ntimes(n=4)
def sum(a, b):
    return a+b

print(sum(3,5))
