from functools import wraps


def repeat(n_times):
    def deco_repeat(my_func):
        @wraps(my_func)
        def wrapper(*args, **kwargs):
            result = []
            for _ in range(n_times):
                result = my_func(*args, **kwargs)
            return result
        return wrapper
    return deco_repeat

@repeat(n_times=3)
def greet(name: str):
    print(f"hello {name}")

greet("bhupendra")
