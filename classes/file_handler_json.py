import json

class File_handler_jsjon:
    def __init__(self, filepath, information):
        self.filepath=filepath
        self.information=information

    def read_method(self):
        fil_set = open(self.filepath, 'r')
        try:
            with fil_set:
                read_from_file = json.loads(self.filepath)
        except FileNotFoundError:
            print("File not found.")
            return read_from_file

    def write_method(self):
        fil_set = open(self.filepath, 'w')
        try:
            with fil_set:
                json.dumps(self.information, self.filepath, indent=4)
        except FileNotFoundError:
            print("File not found.")
        except json.decoder.JSONDecodeError:
            print("File content is not JSON.")
