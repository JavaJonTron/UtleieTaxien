class Renter:
    def __init__(self, age, sex, name, score):  # , score_list, , booked_car
        self.age = age
        self.sex = sex
        self.name = name
        self.score = score
        # self.score_list = score_list
        # self.booked_car = booked_car

    def __str__(self):
        str(self.age)
# str(self.age) + self.sex + self.name + str(self.score)
        return self.age + self.sex + self.name + self.score
