from classes.human import Human


class Admin(Human):
    def __init__(self, age, sex, name, is_logged_in):
        super().__init__(age, sex, name, is_logged_in)

    def __str__(self):
        return str(self.age) + str(self.sex) + str(self.name) + str(self.is_logged_in)
