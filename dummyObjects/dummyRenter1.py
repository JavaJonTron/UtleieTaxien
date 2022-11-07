from renter.renter import Renter

def create_renter():
    name = "Ola Nordmann"
    sex = "Male"
    age = 38
    score = 10
    return Renter(age, sex, name, score)
