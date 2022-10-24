from classes.car import Car


def create_car():
    make = "Skoda"
    model = "Octavia"
    year = 2018
    license_plate = "AA23456"
    fuel_source = "Diesel"
    km = 40678
    return Car(make, model, year, license_plate, fuel_source, km)