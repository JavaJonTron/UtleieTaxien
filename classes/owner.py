class Owner:
    def __init__(self, age, sex, name, score, cars_owned,):
        self.age = age
        self.sex = sex
        self.name = name
        self.score = score
        self.cars_owned

    def __str__(self):
        return str(self.age) + str(self.sex) + str(self.name) + str(self.score) + str(self.cars_owned)