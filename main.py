from classes import owner
from classes import car
from classes import renter
from classes.car import Car


# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    # print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    # commit -test, fra Jon
    # Press the green button in the gutter to run the script.
    if __name__ == '__main__':
        print_hi('PyCharm')


ownerCar1 = Car("ED12345", "Electric", "Model Y", "Tesla", "2022", "6332")

print(ownerCar1.car_info())

# /*cars = [
    #    {'make': "Tesla", 'model': "Model Y", 'year': 2022, 'km': 1000, 'reg': car.regnumber}
# ]


# bilObjekt = car(3,"elektrisk", "eks","eksempel")


# cars = [
 #   {'EksempelBil1': bilObjekt, 'EksempelBil2': bilObjekt, 'EksempelBil3': bilObjekt}
# ]


# for car in cars:
#   print(car)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
