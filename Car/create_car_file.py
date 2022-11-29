import functions.logged_in_status_file
from Car import car
from main import owner_list
from main import car_list
from main import save_system
import dearpygui.dearpygui as dpg


def create_car():
    """
    Oppretter bil objekter, henter inn informasjon fra GUI elementer i menu_main, legger disse inn i et objekt i en
    liste, og lagrer deretter listen.
    :return: Et bil objekt
    """
    make = (dpg.get_value("make")).upper()
    model = (dpg.get_value("model")).upper()
    year = int(dpg.get_value("year"))
    license_plate = (dpg.get_value("license_plate")).upper()
    fuel_source = (dpg.get_value("fuel_source")).upper()
    km = int(dpg.get_value("odometer"))
    hourly_rate = int(dpg.get_value("hourly"))
    daily_rate = int(dpg.get_value("daily"))
    is_take = False
    owner = functions.logged_in_status_file.get_user_logged_in_status(owner_list)
    earned_total = 0
    car_object = car.Car(make, model, year, license_plate, fuel_source, km, is_take, hourly_rate, daily_rate, owner,
                         earned_total)
    car_list.append(car_object)
    save_system('car_file', car_list)
    return car_object
