import dearpygui.dearpygui as dpg
from main import car_list
from functions import get_todays_date as date


def log_in_accepted():
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
        first_key = car_list[0].nickname()
        second_key = car_list[1].nickname()
        third_key = car_list[2].nickname()
        dpg.add_button(label=first_key, callback=car, user_data=first_key)
        dpg.add_button(label=second_key, callback=car, user_data=second_key)
        dpg.add_button(label=third_key, callback=car, user_data=third_key)
        dpg.add_text("Rent new car")


def car(sender, app_data, user_data):
    dpg.delete_item("Renter Control Panel")
    with dpg.window(label="Renter Control Panel", tag="Renter Control Panel", width=400, height=400):
        with dpg.menu_bar(label="Menu Bar"):
            dpg.add_button(label="Home", callback=log_in_accepted)
            dpg.add_button(label="Rent a new car", callback=rent_new_car)
            dpg.add_menu_item(label="Rented cars", callback=see_rented_cars)
            dpg.add_menu_item(label="Options", callback=options)
        dpg.add_text(user_data)
        dpg.add_text("Car info")
        dpg.add_text("SELECT DATE/DATES HERE")
        dpg.add_date_picker(tag="from_date", default_value={'month_day': date.day, 'year': date.year, 'month': date.
                            month}, callback=fromdate)
        dpg.add_date_picker(tag="to_date", default_value={'month_day': date.day + 1, 'year': date.year, 'month': date.
                            month})
        # dpg.add_button(label="Book")

        # dpg.add_button(label="RENT", callback=rentCar, user_data=)


def fromdate():
    from_date = (dpg.get_value("from_date"))


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
