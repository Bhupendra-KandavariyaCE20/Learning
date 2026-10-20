def wrapper(*args, **kwargs):
    print(f"Positional arg tuple {args}")
    print(f"keyword arguments dictionary {kwargs}")
wrapper(1,2,4,name="bk", age=10)
