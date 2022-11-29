import classes.wallet

class Human:
    """
    Klasse for Human
    """
    def __init__(self, age, sex, name, score, is_logged_in, starting_money):
        self.age = age
        self.sex = sex
        self.name = name
        self.score = score
        self.is_logged_in = is_logged_in
        self.wallet = classes.wallet.Wallet(starting_money)
