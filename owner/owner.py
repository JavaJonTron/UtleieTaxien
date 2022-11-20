from classes.human import Human


class Owner(Human):
    def __init__(self, age, sex, name, score, cars_owned, is_logged_in, money):
        super().__init__(age, sex, name, score, is_logged_in, money)
        self.cars_owned = cars_owned

    def __str__(self):
        return str(self.age) + str(self.sex) + str(self.name) + str(self.score) + str(self.cars_owned) + str(
            self.is_logged_in)
