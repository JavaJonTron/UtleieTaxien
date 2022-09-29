class Renter:
    def __init__(self, age, sex, name, score):  # , score_list
        self.age = age
        self.sex = sex
        self.name = name
        self.score = score
        # self.score_list = score_list

    def __str__(self):
        return str(self.age) + self.sex + self.name + str(self.score)
