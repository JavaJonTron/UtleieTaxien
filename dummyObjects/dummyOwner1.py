from owner.owner import Owner


def create_owner():
    name = "Eva Nordmann"
    sex = "Female"
    age = 58
    score = 70
    is_logged_in = False
    return Owner(age, sex, name, score, is_logged_in)
