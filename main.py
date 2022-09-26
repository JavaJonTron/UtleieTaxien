from classes import owner
from classes import car
from classes import renter


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


cars = [
    {'make': "Tesla", 'model': "Model Y", 'year': 2022, 'km': 1000, 'reg': car.regnumber}
]


for car in cars:
    print(car)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
