import argparse

# 1. Create the parser
parser = argparse.ArgumentParser(description="Calculate the square of a number.")

# 2. Add a mandatory positional argument
parser.add_argument("number", type=int, help="The number to square")

# 3. Parse arguments
args = parser.parse_args()

# 4. Access the parsed argument via args.number
result = args.number ** 2
print(f"The square of {args.number} is {result}")
