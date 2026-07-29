def print_user_profile(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}:{value}")
print_user_profile(name="Alice", age=18, role="rapist")

