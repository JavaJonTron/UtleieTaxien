import pickle
import os

class File_handler_pickle:
    def __init__(self, filename, information):
        self.filename = filename
        self.information = information

    #def find_filepath(self):
    #   dirname = os.path.dirname(__file__)
    #   return dirname[:-14]


    def read_method(self):
        try:
            with open(self.filename, 'rb') as read_from_file:
                unpickling = pickle.load(read_from_file)
        except FileNotFoundError:
            print("File not found.")
        except FileExistsError:
            print("FileExistsError")
        except EOFError:
            print("EOFError")
        except AttributeError:
            print("Attribute Error")
        else:
            return unpickling

    def write_method(self):
        write_to_file = open(self.filename, 'wb')
        pickle.dump(self.information, write_to_file)
        write_to_file.close()
