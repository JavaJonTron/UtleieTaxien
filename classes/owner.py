class Owner:
    def __init__(self, age, sex, name, score, owned_cars,):
        self.age = age
        self.sex = sex
        self.name = name
        self.score = score
        self.owned_cars = owned_cars

    def __str__(self):
        return str(self.age) + str(self.sex) + str(self.name) + str(self.score) + str(self.owned_cars)