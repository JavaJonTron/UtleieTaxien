import dearpygui.dearpygui as dpg
from Car import create_car_file
from main import owner_list
import atexit


def avslutt():
    print("AVSLUTTES")


atexit.register(avslutt)


def log_in_accepted(sender, app_data, user_data):
    for owner in owner_list:
        owner.is_logged_in = False
    dpg.delete_item("Owner Login")
    user_data.is_logged_in = True
    dpg.delete_item("Owner Control Panel")
    with dpg.window(label="Owner Control Panel", tag="Owner Control Panel", width=400, height=400):
        with dpg.menu_bar(label="Menu Bar"):
            # dpg.add_menu_item(label="Rent a new car")
            dpg.add_button(label="Home", callback=log_in_accepted)
            dpg.add_button(label="Add a new car", callback=new_car)
            dpg.add_menu_item(label="See my cars", callback=see_cars)
            dpg.add_menu_item(label="Options", callback=options)
        dpg.add_text("TEST")


def new_car():
    # owner_list[user_data].is_logged_in = True
    dpg.delete_item("Owner Control Panel")
    with dpg.window(label="Owner Control Panel", tag="Owner Control Panel", width=400, height=400):
        with dpg.menu_bar(label="Menu Bar"):
            # dpg.add_menu_item(label="Rent a new car")
            dpg.add_button(label="Home", callback=log_in_accepted)
            dpg.add_button(label="Add a new car", callback=new_car)
            dpg.add_menu_item(label="See my cars", callback=see_cars)
            dpg.add_menu_item(label="Options", callback=options)
        dpg.add_text("TEST")
        dpg.add_input_text(hint="Make:", no_spaces=True, uppercase=True)
        dpg.add_input_text(hint="Model:", no_spaces=True, uppercase=True)
        dpg.add_input_text(hint="Year:", no_spaces=True, uppercase=True, )
        dpg.add_input_text(hint="License Plate", no_spaces=True, uppercase=True)
        dpg.add_input_text(hint="Fuel Source:", no_spaces=True, uppercase=True)
        dpg.add_input_text(hint="Odometer:", no_spaces=True, uppercase=True)
        dpg.add_input_text(hint="Hourly Rate:", no_spaces=True, uppercase=True)
        dpg.add_input_text(hint="Daily Rate:", no_spaces=True, uppercase=True)
        dpg.add_button(label="Publish")


def see_cars():
    # owner_list[user_data].is_logged_in = True
    dpg.delete_item("Owner Control Panel")
    with dpg.window(label="Owner Control Panel", tag="Owner Control Panel", width=400, height=400):
        with dpg.menu_bar(label="Menu Bar"):
            # dpg.add_menu_item(label="Rent a new car")
            dpg.add_button(label="Home", callback=log_in_accepted)
            dpg.add_button(label="Add a new car", callback=new_car)
            dpg.add_menu_item(label="See my cars", callback=see_cars)
            dpg.add_menu_item(label="Options", callback=options)
        dpg.add_text("TEST")


def options():
    # owner_list[user_data].is_logged_in = True
    dpg.delete_item("Owner Control Panel")
    with dpg.window(label="Owner Control Panel", tag="Owner Control Panel", width=400, height=400):
        with dpg.menu_bar(label="Menu Bar"):
            # dpg.add_menu_item(label="Rent a new car")
            dpg.add_button(label="Home", callback=log_in_accepted)
            dpg.add_button(label="Add a new car", callback=new_car)
            dpg.add_menu_item(label="See my cars", callback=see_cars)
            dpg.add_menu_item(label="Options", callback=options)
        dpg.add_text("TEST")
