import argparse


parser = argparse.ArgumentParser(
        description="A simple file processing program"
)

parser.add_argument("filename", help="File to process")

parser.add_argument("--count", type=int, default=1)

args = parser.parse_args()


print(f"Processing File: {args.filename} and it's count is {args.count}")
