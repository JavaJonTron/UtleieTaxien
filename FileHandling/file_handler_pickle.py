import pickle
import os

class File_handler_pickle:
    def __init__(self, filename, information):
        self.filename = filename
        self.information = information


    #def find_filepath(self):
    #    print('getcwd:      ', os.getcwd())
    #    filepath = os.getcwd()
    #    print(filepath)
    #    filepath
    #    return filepath

    def create_directory(self):
        pass


    def read_method(self):
        read_from_file = open(self.filename, 'rb')
        unpickling = pickle.load(read_from_file)
        read_from_file.close()
        return unpickling

    def write_method(self):
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