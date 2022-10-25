import json
import os

class File_handler_json:
    def __init__(self, filename, information):
        self.filename = filename
        self.information=information

    def find_filepath(self):
        current_directory = os.getcwd()
        current_directory += "\Storage"
        print(current_directory)
        return current_directory


    def read_method(self):
        filepath = self.find_filepath()+self.filename
        fil_set = open(filepath, 'r')
        try:
            with fil_set:
                read_from_file = json.loads(filepath)
        except FileNotFoundError:
            print("File not found.")
            return read_from_file

    def write_method(self):
        filepath = self.find_filepath() + self.filename
        fil_set = open(filepath, 'w')
        try:
            with fil_set:
                json.dumps(self.information, indent=4)
        except FileNotFoundError:
            print("File not found.")
        except json.decoder.JSONDecodeError:
            print("File content is not JSON.")
