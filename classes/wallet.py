class Wallet:
    """
    Klasse for lommebok
    """
    def __init__(self, money):
        self.money = money

    def remove_from_wallet(self, amount):
        """
        Mengde penger som skal fjernes fra lommebok
        :param amount: Pris for leie av bil
        :return:
        """
        self.money -= amount

    def add_to_wallet(self, income):
        """
        Mengde penger som skal legges til i lommebok
        :param income: Pris for leie av bil etter firmaets andel
        :return:
        """
        self.money += income
