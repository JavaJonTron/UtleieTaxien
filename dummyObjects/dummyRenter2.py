from renter.renter import Renter

def create_renter():
    """
    Oppretter et dummy renter objekt
    :return: Leier objekt
    """
    name = "Kari Nordmann"
    sex = "Female"
    age = 26
    score = 40
    is_logged_in = False
    money = 50000
    return Renter(age, sex, name, score, is_logged_in, money)
