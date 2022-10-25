from dummyObjects import dummyCar3
from classes.owner import Owner

def create_owner():
    name = "Nils Nordmann"
    sex = "Male"
    age = 26
    score = 50
    cars_owned = {}
    is_logged_in = False
    return Owner(age, sex, name, score, cars_owned, is_logged_in)

