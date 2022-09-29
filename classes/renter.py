class Renter:
    def __init__(self, age, sex, name, rented, score, score_list):
        self.age = age
        self.sex = sex
        self.name = name
        self.rented = rented
        self.score = score
        self.score_list = score_list

    def __str__(self):
        return self.age + self.sex + self.name + self.rented + self.score
