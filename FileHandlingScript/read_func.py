import pickle


def read_method(filename):
    try:
        with open(filename, 'rb') as read_from_file:
            unpickling = pickle.load(read_from_file)
    except FileNotFoundError:
        print("File not found.")
    except FileExistsError:
        print("FileExistsError")
    except EOFError:
        print("EOFError")
    else:
        return unpickling
