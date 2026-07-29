def create_multiplier(multi):

    def multiply(number):
        return multi * number
    return multiply

x = create_multiplier(5)

print(x(3))

