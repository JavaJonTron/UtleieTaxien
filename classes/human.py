class Human:
    def __init__(self, age, sex, name, score, is_logged_in, wallet):  # id Forslag til at hver enkelt person kan ha en ID
        self.age = age
        self.sex = sex
        self.name = name
        self.score = score
        self.is_logged_in = is_logged_in
        self.wallet = wallet
        # self.id = id

    def remove_from_wallet(self, amount):
        self.wallet -= amount

    def add_to_wallet(self, income):
        self.wallet += income
