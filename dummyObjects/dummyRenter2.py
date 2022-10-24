from classes.renter import Renter

def create_renter():
    name = "Kari Nordmann"
    sex = "Female"
    age = 26
    score = 40
    return Renter(age, sex, name, score)
