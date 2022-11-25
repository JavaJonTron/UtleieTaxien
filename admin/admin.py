class Admin:
    def __init__(self, name, is_logged_in):
        self.name = name
        self.is_logged_in = is_logged_in

    def __str__(self):
        return str(self.name) + str(self.is_logged_in)
