import pickle


def write_method(filename, information):
    write_to_file = open(filename, 'wb')
    pickle.dump(information, write_to_file)
    write_to_file.close()
