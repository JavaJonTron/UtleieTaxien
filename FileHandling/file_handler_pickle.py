import pickle

class File_handler_pickle:
    def __init__(self, filename, information):
        self.filename = filename
        self.information = information

    def find_filepath(self):
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