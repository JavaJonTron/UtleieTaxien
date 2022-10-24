from classes.renter import Renter
from dummyObjects import dummyCar1
from dummyObjects import dummyCar2

def create_renter():
    name = "Eva Nordmann"
    sex = "Female"
    age = 58
    score = 70
    cars = {dummyCar1, dummyCar2}
    return Renter(age, sex, name, score, cars)
