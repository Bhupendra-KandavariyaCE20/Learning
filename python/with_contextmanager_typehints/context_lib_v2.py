from contextlib import contextmanager


@contextmanager
def open_file(filename, mode='w'):
    print("Opening the file")
    file = open(filename, mode)

    try:
        yield file
    finally:
        file.close()
        print('File Closed')


with open_file('output.txt', 'w') as out:
    out.write("Line 1: Writing data using @contextmanager!\n")
print("successfully writtent the content")

