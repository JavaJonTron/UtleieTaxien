from classes.car import Car
from functions import create_car_file

cars = {}
# make = ""
# model = ""
# year = 0
# license_plate = ""
# fuel_source = ""
# km = 0

car = create_car_file.create_car()

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
