class Admin:
    """
    Klasse for Admin brukere.
    """
    def __init__(self, name, is_logged_in):
        self.name = name
        self.is_logged_in = is_logged_in

    def __str__(self):
        """
        Gjør det mulig å skrive ut objekt attributter på en fin måte
        :return: String
        """
        return str(self.name) + str(self.is_logged_in)
