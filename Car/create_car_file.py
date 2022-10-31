from Car.car import Car


def create_car():
    make = "Tesla"  # input("Make: ").upper()
    model = "Model Y"  # input("Model: ").upper()
    while True:
        try:
            year = 2022  # int(input("Year: "))
            break
        except ValueError:
            print("Please enter the year the cars was manufactured!")
            continue
    license_plate = "ED15421"  # input("License plate: ").upper()
    fuel_source = "Electric"  # input("Fuel source: ").upper()
    while True:
        try:
            km = 20500  # int(input("Odometer: "))
            break
        except ValueError:
            print("Please enter how far the car has driven!")
            continue
    is_take = False
    hourly_rate = 150
    daily_rate = 3000
    return Car(make, model, year, license_plate, fuel_source, km, is_take,hourly_rate, daily_rate)
