import dearpygui.dearpygui as dpg
import dummyObjects.dummyCar1
import dummyObjects.dummyCar2
import dummyObjects.dummyCar3

cars = {}
carsNickname = []

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
        with dpg.menu_bar(label="Menu Bar"):
            # dpg.add_menu_item(label="Rent a new car")
            dpg.add_button(label="Home", callback=log_in_accepted)
            dpg.add_button(label="Rent a new car", callback=rent_new_car)
            dpg.add_menu_item(label="Rented cars", callback=see_rented_cars)
            dpg.add_menu_item(label="Options", callback=options)
        first_key = list(cars.keys())[0]
        carsNickname.append(first_key)
        second_key = list(cars.keys())[1]
        carsNickname.append(second_key)
        third_key = list(cars.keys())[2]
        carsNickname.append(third_key)
        dpg.add_button(label=first_key, callback=car, user_data=(carsNickname[0]))
        dpg.add_button(label=second_key, callback=car, user_data=(carsNickname[1]))
        dpg.add_button(label=third_key, callback=car, user_data=(carsNickname[2]))

        dpg.add_text("Rent new car")

def car(nickname):
    dpg.delete_item("Renter Control Panel")
    with dpg.window(label="Renter Control Panel", tag="Renter Control Panel", width=400, height=400):
        with dpg.menu_bar(label="Menu Bar"):
            dpg.add_button(label="Home", callback=log_in_accepted)
            dpg.add_button(label="Rent a new car", callback=rent_new_car)
            dpg.add_menu_item(label="Rented cars", callback=see_rented_cars)
            dpg.add_menu_item(label="Options", callback=options)
        dpg.add_text(nickname)
        dpg.add_text("Car info")
        dpg.add_text("SELECT DATE/DATES HERE")
        dpg.add_button(label="RENT")

def see_rented_cars():
    dpg.delete_item("Renter Control Panel")
    with dpg.window(label="Renter Control Panel", tag="Renter Control Panel", width=400, height=400):
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
        with dpg.menu_bar(label="Menu Bar"):
            # dpg.add_menu_item(label="Rent a new car")
            dpg.add_button(label="Home", callback=log_in_accepted)
            dpg.add_button(label="Rent a new car", callback=rent_new_car)
            dpg.add_menu_item(label="Rented cars", callback=see_rented_cars)
            dpg.add_menu_item(label="Options", callback=options)

        dpg.add_text("Options")
