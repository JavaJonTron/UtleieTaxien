import dearpygui.dearpygui as dpg
import dummyObjects.dummyCar1
import dummyObjects.dummyCar2
import dummyObjects.dummyCar3

cars = {}

def log_in_accepted():

    car = dummyObjects.dummyCar1.create_car()
    nickname = str(car.year) + " " + str(car.make) + " " + str(car.model)
    cars[nickname] = car
    car = dummyObjects.dummyCar2.create_car()
    nickname = str(car.year) + " " + str(car.make) + " " + str(car.model)
    cars[nickname] = car
    car = dummyObjects.dummyCar3.create_car()
    nickname = str(car.year) + " " + str(car.make) + " " + str(car.model)
    cars[nickname] = car
    for k,v in cars.items():
        print(k,v)
    dpg.delete_item("Renter Control Panel")
    with dpg.window(label="Renter Control Panel", tag="Renter Control Panel", width=400, height=400):
        dpg.hide_item("Renter Login")
        with dpg.menu_bar(label="Menu Bar"):
            # dpg.add_menu_item(label="Rent a new car")
            dpg.add_button(label="Home", callback=log_in_accepted)
            dpg.add_button(label="Rent a new car", callback=rent_new_car)
            dpg.add_menu_item(label="Rented cars", callback=see_rented_cars)
            dpg.add_menu_item(label="Options", callback=options)

        dpg.add_text("Main menu", tag="renterMainMenuText")


def rent_new_car():
    dpg.delete_item("Renter Control Panel")
    with dpg.window(label="Renter Control Panel", tag="Renter Control Panel", width=400, height=400):
        dpg.hide_item("Renter Login")
        with dpg.menu_bar(label="Menu Bar"):
            # dpg.add_menu_item(label="Rent a new car")
            dpg.add_button(label="Home", callback=log_in_accepted)
            dpg.add_button(label="Rent a new car", callback=rent_new_car)
            dpg.add_menu_item(label="Rented cars", callback=see_rented_cars)
            dpg.add_menu_item(label="Options", callback=options)
        with dpg.table():
            first_key = list(cars.keys())[0]
            second_key = list(cars.keys())[1]
            third_key = list(cars.keys())[2]
            dpg.add_table_column(label=first_key)
            dpg.add_table_column(label=second_key)
            dpg.add_table_column(label=third_key)

        dpg.add_text("Rent new car")

def see_rented_cars():
    dpg.delete_item("Renter Control Panel")
    with dpg.window(label="Renter Control Panel", tag="Renter Control Panel", width=400, height=400):
        dpg.hide_item("Renter Login")
        with dpg.menu_bar(label="Menu Bar"):
            # dpg.add_menu_item(label="Rent a new car")
            dpg.add_button(label="Home", callback=log_in_accepted)
            dpg.add_button(label="Rent a new car", callback=rent_new_car)
            dpg.add_menu_item(label="Rented cars", callback=see_rented_cars)
            dpg.add_menu_item(label="Options", callback=options)

        dpg.add_text("See rented cars")

def options():
    dpg.delete_item("Renter Control Panel")
    with dpg.window(label="Renter Control Panel", tag="Renter Control Panel", width=400, height=400):
        dpg.hide_item("Renter Login")
        with dpg.menu_bar(label="Menu Bar"):
            # dpg.add_menu_item(label="Rent a new car")
            dpg.add_button(label="Home", callback=log_in_accepted)
            dpg.add_button(label="Rent a new car", callback=rent_new_car)
            dpg.add_menu_item(label="Rented cars", callback=see_rented_cars)
            dpg.add_menu_item(label="Options", callback=options)

        dpg.add_text("Options")
