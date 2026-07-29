x = "Global"

def outer_function():

    x = "enclosing"

    def inner_function():

        x = "Local"

        print(x)
    inner_function()

    print(f"Enclosing one {x}")

outer_function()
print(f"Global one {x}")
