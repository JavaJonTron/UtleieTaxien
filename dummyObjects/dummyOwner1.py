from dummyObjects import dummyCar1
from dummyObjects import dummyCar2
from classes.owner import Owner

def create_owner():
    name = "Eva Nordmann"
    sex = "Female"
    age = 58
    score = 70
    cars_owned = {}
    return Owner(age, sex, name, score, cars_owned)
