from contextlib import contextmanager

@contextmanager
def open_file_writer(filename: str):
    print(f"Opening '{filename}' for writing...")
    file = open(filename, 'w')

    try:
        yield file
    finally:
        file.close()
        print("File Closed Successfully")


with open_file_writer("output.txt") as f:
    f.write("Line 1: Writing data using @contextmanager!\n")
    f.write("Line 2: Python context managers are awesome.\n")

print("File write completed successfully!")
