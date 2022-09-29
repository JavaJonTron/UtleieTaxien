from classes.car import Car


def create_car():
    make = input("Make: ").upper()
    model = input("Model: ").upper()
    while True:
        try:
            year = int(input("Year: "))
            break
        except ValueError:
            print("Please enter the year the cars was manufactured!")
            continue
    license_plate = input("License plate: ").upper()
    fuel_source = input("Fuel source: ").upper()
    while True:
        try:
            km = int(input("Odometer: "))
            break
        except ValueError:
            print("Please enter how far the car has driven!")
            continue
    return Car(make, model, year, license_plate, fuel_source, km)