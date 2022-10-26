import json
import os

class File_handler_json:
    def __init__(self, filename, information):
        self.filename = filename
        self.information = information

    def find_filepath(self):
        current_directory = os.getcwd()
        print(current_directory)
        print(current_directory)
        current_directory += "Storage"
        print(current_directory)
        return current_directory

    def read_method(self):
        filepath = self.find_filepath()+self.filename
        try:
            with open(filepath) as file:
                read_from_file = json.load(file)
        except FileNotFoundError:
                print("File not found.")
        except json.decoder.JSONDecodeError:
            print("File content is not JSON.")
        else:
            print("NÅ LESER VI FRA JSON FILA")
            print(read_from_file)
            return read_from_file

    def write_method(self):
        filepath = self.find_filepath() + self.filename
        try:
            with open(filepath, "w") as file:
                tobewritten=json.dumps(self.information.__dict__)
                print(f"ET ELLER ANNET{tobewritten}")
                json.dump(tobewritten, file, indent=4)
        except FileNotFoundError:
            print("File not found.")