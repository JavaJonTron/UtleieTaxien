import json

class File_handler:
    def __init__(self, filepath, information):
        self.filepath=filepath

    def read_method(self):
        print("*********************")
        print(self.filepath)
        fil_set = open(self.filepath, 'r')
        print(fil_set.read())
        print("*********************")
        return fil_set

    def write_method(self):
        print("*********************")
        print(self.filepath)
        fil_set = open(self.filepath, 'w')
        print(fil_set.read())
        print("*********************")
        return fil_set