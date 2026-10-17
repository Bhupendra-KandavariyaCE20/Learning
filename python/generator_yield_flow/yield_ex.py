# If we don't use yield

def get_error_logs(filename):
    errors = []
    with open(filename) as f:
        for line in f:
            if "ERROR" in line:
                errors.append(line)
    return errors



# if we use yield
def get_error_logs_stream(filename):
    with open(filename) as f:
        for line in f:
            if "ERROR" in line:
                yield line

