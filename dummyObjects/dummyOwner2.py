from classes.renter import Renter
from dummyObjects import dummyCar3

def create_renter():
    name = "Nils Nordmann"
    sex = "Male"
    age = 26
    score = 50
    cars = {dummyCar3}
    return Renter(age, sex, name, score, cars)
