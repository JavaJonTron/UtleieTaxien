from renter.renter import Renter

def create_renter():
    name = "Kari Nordmann"
    sex = "Female"
    age = 26
    score = 40
    is_logged_in = False
    money = 500
    return Renter(age, sex, name, score, is_logged_in, money)
