from classes.human import Human

class Owner(Human):
    def __init__(self, age, sex, name, score, is_logged_in, money):
        super().__init__(age, sex, name, score, is_logged_in, money)

    def __str__(self):
        return str(self.age) + str(self.sex) + str(self.name) + str(self.score) + str(
            self.is_logged_in)
