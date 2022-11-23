import pickle
import os

#dirname = os.path.dirname(__file__)
#dirname = dirname.replace(r"\\FileHandling", "")
#dirname = dirname[:-14]
#dirname = os.path.dirname(__file__)

class File_handler_pickle:
    def __init__(self, filename, information):
        self.filename = filename
        self.information = information


    def find_filepath(self):
        dirname = os.path.dirname(__file__)
        return dirname[:-14]


    def create_directory(self):
        pass


    def read_method(self):
        #filename = os.path.join(self.find_filepath(), self.filename)
        try:
            with open(self.filename, 'rb') as read_from_file:
                #read_from_file = open(self.filename, 'rb')
                unpickling = pickle.load(read_from_file)
        except FileNotFoundError:
            print("File not found.")
            print("Exception happened")
        except FileExistsError:
            print("FileExistsError")
        except EOFError:
            print("EOFError")
        else:
            return unpickling

    def write_method(self):
        #filename = os.path.join(self.find_filepath(), self.filename)
        write_to_file = open(self.filename, 'wb')
        pickle.dump(self.information, write_to_file)
        write_to_file.close()




#root_filepath = os.getcwd()
#filepath = os.path.join(root_filepath, "Mappe1")
#print(filepath)
#os.mkdir(filepath)
#filepath +="/important"
#file = open(filepath, 'wb')
#pickle.dump(ny_klasse, file)
#file.close()