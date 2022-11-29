from classes import human


class Renter(human.Human):
    """
    Klasse for Leiere.
    """
    def __init__(self, age, sex, name, score, is_logged_in, starting_money):
        super().__init__(age, sex, name, score, is_logged_in, starting_money)

    def __str__(self):
        """
            Gjør det mulig å skrive ut objekt attributter på en fin måte
            :return: String
            """
        return str(self.age) + str(self.sex) + str(self.name) + str(self.score) + str(self.is_logged_in)
