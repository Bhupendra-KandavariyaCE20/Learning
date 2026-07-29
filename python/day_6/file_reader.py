class FileReader:
    def __init__(self, filename:str,  mode:str = 'r'):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        """Opens the file and returns the file object (or self)."""
        print(f"Opening '{self.filename}'...")
        self.file = open(self.filename, self.mode)
        return self.file # What gets assigned to 'as f'

    def __exit__(self, exec_type, exec_value, exec_tb):
        """Ensures the file is closed, even if an error occurred inside the block."""
        if self.file:
            self.file.close()
            print(f"Closed {self.filename}")

        return False


with FileReader("data.txt", "r") as file_handle:
    content = file_handle.read()
    print("File Content:")
    print(content)

print("Finished!")

