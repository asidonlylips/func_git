class My_manager():
    def __init__(self, file_name, method):
        self.file_name = file_name
        self.method = method
    def __enter__(self):
        self.file = open(self.file_name, self.method) 
        return self.file
    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.file.close()
