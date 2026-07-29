def deco(func):
    def wrapper(*args, **kwargs):
        print("starting our new function")
        y = func(*args, **kwargs)
        print("end of our new func deco")
        return y 
    return wrapper


def dela(num, delab):
    print(num * delab)
    return num * delab

x = deco(dela)
print(x(30, delab=60))


@deco
def dela2(num, delab):
    print("deco methon 2")
    print(num*delab)
    return num * delab

print(dela2(30, 60))
