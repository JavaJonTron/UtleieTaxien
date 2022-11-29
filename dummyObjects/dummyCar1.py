from Car.car import Car


def create_car(owner):
    """
    Oppretter et dummy bil object
    :param owner: Eier av bil (objekt)
    :return: Bil objekt
    """
    make = "Tesla"
    model = "Model Y"
    year = 2022
    license_plate = "EL12345"
    fuel_source = "Electric"
    km = 1056
    is_take = False
    hourly_rate = 150
    daily_rate = 3000
    earned_total = 0
    return Car(make, model, year, license_plate, fuel_source, km, is_take, hourly_rate, daily_rate, owner, earned_total)





