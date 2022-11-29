from owner.owner import Owner


def create_owner():
    """
    Oppretter et dummy eier objekt
    :return: Eier objekt
    """
    name = "Eva Nordmann"
    sex = "Female"
    age = 58
    score = 70
    is_logged_in = False
    money = 20000
    return Owner(age, sex, name, score, is_logged_in, money)
