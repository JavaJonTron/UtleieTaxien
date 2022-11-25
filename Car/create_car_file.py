import functions.logged_in_status_file
from Car import car
from main import owner_list
from main import car_list
from main import save_system
import dearpygui.dearpygui as dpg

def create_car():
    make = (dpg.get_value("make")).upper()
    print(make)
    model = (dpg.get_value("model")).upper()
    print(model)
    while True:
        try:
            year = int(dpg.get_value("year"))
            print(year)
            break
        except ValueError:
            print("Please enter the year the cars was manufactured!")
            continue
    license_plate = (dpg.get_value("license_plate")).upper()
    print(license_plate)
    fuel_source = (dpg.get_value("fuel_source")).upper()
    print(fuel_source)
    while True:
        try:
            km = int(dpg.get_value("odometer"))
            break
        except ValueError:
            print("Please enter how far the car has driven!")
            continue
    while True:
        try:
            hourly_rate = int(dpg.get_value("hourly"))
            break
        except ValueError:
            print("Please enter hourly rate!")
            continue
    while True:
        try:
            daily_rate = int(dpg.get_value("daily"))
            break
        except ValueError:
            print("Please enter daily rate!")
            continue
    is_take = False
    owner = functions.logged_in_status_file.logged_in_status(owner_list)
    earned_total = 0
    car_object = car.Car(make, model, year, license_plate, fuel_source, km, is_take, hourly_rate, daily_rate, owner, earned_total)
    car_list.append(car_object)
    save_system('car_file', car_list)
    return car_object
