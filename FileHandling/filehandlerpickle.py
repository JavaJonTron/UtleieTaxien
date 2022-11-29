import pickle


class FileHandlerPickle:
    """
    Klasse for fil håndterer objekt
    """
    def __init__(self, filename, information):
        self.filename = filename
        self.information = information

    def read_method(self):
        """
        Leser fra fil med pickle (lar oss lagre objekter i tekst filer)
        :return: Innholdet fra filen
        """
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
        """
        Skriver til fil med pickle (lar oss lagre objekter i tekst filer)
        :return:
        """
        write_to_file = open(self.filename, 'wb')
        pickle.dump(self.information, write_to_file)
        write_to_file.close()
