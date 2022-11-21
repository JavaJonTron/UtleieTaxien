class Human:
    def __init__(self, age, sex, name, score, is_logged_in, money):#id Forslag til at hver enkelt person kan ha en ID
        self.age = age
        self.sex = sex
        self.name = name
        self.score = score
        self.is_logged_in = is_logged_in
        self.money = money
        #self.id = id



    def wallet(self, income):
        self.money += income

