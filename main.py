from classes.car import Car

cars = {}
# make = ""
# model = ""
# year = 0
# license_plate = ""
# fuel_source = ""
# km = 0

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


car = create_car()

nickname = str(car.year) + " " + str(car.make) + " " + str(car.model)
cars[nickname] = car

print("License plate: " + str(car.license_plate))
print("Fuel Source: " + str(car.fuel_source))
print("Model: " + str(car.model))
print("Make: " + str(car.make))
print("Odometer: " + str(car.km))
print("Year: " + str(car.year))
print("Nickname: " + nickname)

for k, v in cars.items():
    print(k, v)

# print(vars(bil))

# for x in cars.values():
    # print(x)

# for key,values in cars.items():
    # for i in values:
    # print(key," : ",i)

# for x, y in cars.items():
    # print(x, y)

# for car in cars:
    # print(cars[car])
