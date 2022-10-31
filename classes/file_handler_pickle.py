import pickle

class File_handler_pickle:
    def __init__(self, filename, information):
        self.filename = filename
        self.information = information

    def find_filepath(self):
        pass

    def read_method(self):
        read_from_file = open(self.filename, 'r')
        unpickling = pickle.load(read_from_file)
        unpickling
        pass

#import pickle
#filehandler = open(filename, 'r')
#object = pickle.load(filehandler)
#
#
#
#

    def write_method(self):
        pass
