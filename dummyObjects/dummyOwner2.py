from classes.owner import Owner
from dummyObjects import dummyCar3

def create_owner():
    name = "Nils Nordmann"
    sex = "Male"
    age = 26
    score = 50
    owned_cars = []
    return Owner(age, sex, name, score, owned_cars)
