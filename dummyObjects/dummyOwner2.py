from owner.owner import Owner


def create_owner():
    name = "Nils Nordmann"
    sex = "Male"
    age = 26
    score = 50
    is_logged_in = False
    money = 45000
    return Owner(age, sex, name, score, is_logged_in, money)
