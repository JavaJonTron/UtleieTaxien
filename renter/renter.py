from classes import human

class Renter(human.Human):
    def __init__(self, age, sex, name, score, is_logged_in, money):  # , score_list, , booked_car
        super().__init__(age, sex, name, score, is_logged_in, money)


    def __str__(self):
        return str(self.age) + str(self.sex) + str(self.name) + str(self.score) + str(self.is_logged_in)

