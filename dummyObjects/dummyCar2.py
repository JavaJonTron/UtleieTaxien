from classes.car import Car


def create_car():
    make = "Volkswagen"
    model = "Golf"
    year = 2012
    license_plate = "AA12345"
    fuel_source = "Petrol"
    km = 89507
    is_take = False
    hourly_rate = 80
    daily_rate = 1500
    return Car(make, model, year, license_plate, fuel_source, km, is_take, hourly_rate, daily_rate)