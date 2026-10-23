import argparse


def greet(name: str, count: int):
    for i in range(count):
        print(f"Hello {name}")


def main():

    parser = argparse.ArgumentParser(description="A greeting CLI")


    parser.add_argument("name", help="Name of the person to greet")

    parser.add_argument("--count", type=int, default=1, help="Number of greeting(default:1)")

    args = parser.parse_args()

    if args.count<1:
        parse.error("--count must be atleast 1")


    greet(args.name, args.count)

if __name__ == "__main__":
    main()
