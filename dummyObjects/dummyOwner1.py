from classes.owner import Owner
from dummyObjects import dummyCar1
from dummyObjects import dummyCar2

def create_owner():
    name = "Eva Nordmann"
    sex = "Female"
    age = 58
    score = 70
    owned_cars = {}
    return Owner(age, sex, name, score, owned_cars)
