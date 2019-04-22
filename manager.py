class Context_manager():

    def __init__(self, file_name, method):
        self.file_name = file_name
        self.method = method

    def __enter__(self):
        self.file = open(self.file_name, self.method)
        return self.file

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.file.close()


def read_file(file_name):
    with Context_manager(file_name, 'r') as f_read:
        return f_read.read()


def write_to_file(file_name, method, your_text):
    with Context_manager(file_name, method) as f_write:
        f_write.write('\n' + your_text)
