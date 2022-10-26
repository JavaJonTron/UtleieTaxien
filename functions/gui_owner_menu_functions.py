import dearpygui.dearpygui as dpg
import dummyObjects.dummyOwner1 as dummy1
from functions import writing_to_file as write
from functions import read_from_file as read
from functions import create_car_file
from main import owner_list


def log_in_accepted(sender, app_data, user_data):
    for owner in owner_list:
        owner.is_logged_in = False
    dpg.delete_item("Owner Login")
    if user_data == 0 or 1:
        owner_list[user_data].is_logged_in = True
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
    print ("HER SKAL DET EGENTLIG OPPRETTES EN JÆVLA BIL")
    car = create_car_file.create_car()
    print(car)
    #Her burde vi heller legge til bilen i en liste over alle biler i hele verden.
    #Så burde vi legge til listen over alle biler under for å skrive listen til Json
    write.writing("CAR.json", car)




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
    read.reading("CAR.JSON")


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
