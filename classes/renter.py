class Renter:
    def __init__(self, age, sex, name, score):  # , score_list, , booked_car
        self.age = age
        self.sex = sex
        self.name = name
        self.score = score
        # self.score_list = score_list
        # self.booked_car = booked_car

    def __str__(self):
        return str(self.age) + str(self.sex) + str(self.name) + str(self.score)

