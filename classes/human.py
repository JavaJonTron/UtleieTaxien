import classes.wallet


class Human:
    def __init__(self, age, sex, name, score, is_logged_in, starting_money):  # id Forslag til at hver enkelt person kan ha en ID
        self.age = age
        self.sex = sex
        self.name = name
        self.score = score
        self.is_logged_in = is_logged_in
        self.wallet = classes.wallet.Wallet(starting_money)



        #self.wallet = wallet
        # self.id = id


