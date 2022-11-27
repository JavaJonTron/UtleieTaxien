class Wallet:
    def __init__(self, money):
        self.money = money

    def remove_from_wallet(self, amount):
        self.wallet -= amount

    def add_to_wallet(self, income):
        self.wallet += income


