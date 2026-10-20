import time
from functools import wraps
def my_deco(my_func):
    @wraps(my_func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = my_func(*args,**kwargs)
        end = time.time()
        print(f"Finished in {end - start:.4f} seconds")
        return result
    return wrapper

@my_deco
def calculate_square(n: int):
    return n*n

result = calculate_square(5)
print(result)
print(calculate_square.__name__)
