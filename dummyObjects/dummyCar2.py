from Car.car import Car


def create_car(owner):
    make = "Volkswagen"
    model = "Golf"
    year = 2012
    license_plate = "AA12345"
    fuel_source = "Petrol"
    km = 89507
    is_take = False
    hourly_rate = 80
    daily_rate = 1500
    earned_total = 0
    return Car(make, model, year, license_plate, fuel_source, km, is_take, hourly_rate, daily_rate, owner, earned_total)