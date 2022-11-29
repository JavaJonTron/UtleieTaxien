from renter.renter import Renter


def create_renter():
    """
    Oppretter et dummy renter objekt
    :return: Leier objekt
    """
    name = "Ola Nordmann"
    sex = "Male"
    age = 38
    score = 10
    is_logged_in = False
    money = 500000
    return Renter(age, sex, name, score, is_logged_in, money)
