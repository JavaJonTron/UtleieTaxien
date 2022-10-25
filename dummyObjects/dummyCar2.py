from classes.car import Car


def create_car():
    make = "Volkswagen"
    model = "Golf"
    year = 2012
    license_plate = "AA12345"
    fuel_source = "Petrol"
    km = 89507
    is_taken = False
    return Car(make, model, year, license_plate, fuel_source, km, is_taken)