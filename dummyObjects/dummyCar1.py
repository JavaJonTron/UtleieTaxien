from Car.car import Car


def create_car():
    make = "Tesla"
    model = "Model Y"
    year = 2022
    license_plate = "EL12345"
    fuel_source = "Electric"
    km = 1056
    is_take = False
    hourly_rate = 150
    daily_rate = 3000
    return Car(make, model, year, license_plate, fuel_source, km, is_take, hourly_rate, daily_rate)