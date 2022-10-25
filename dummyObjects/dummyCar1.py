from classes.car import Car


def create_car():
    make = "Tesla"
    model = "Model Y"
    year = 2022
    license_plate = "EL12345"
    fuel_source = "Electric"
    km = 1056
    is_take = False
    return Car(make, model, year, license_plate, fuel_source, km, is_take)