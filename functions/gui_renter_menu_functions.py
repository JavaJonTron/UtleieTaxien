import dearpygui.dearpygui as dpg
from main import car_list
from functions import get_todays_date as date
from functions import delete_windows
from functions import log_out as lg


def log_in_accepted():
    dpg.delete_item("Renter Login")
    delete_windows.delete_windows_func()
    with dpg.window(label="Renter Control Panel", tag="Renter Main", width=400, height=400):
        dpg.set_primary_window("Renter Main", True)
        with dpg.menu_bar(label="Menu Bar"):
            dpg.add_button(label="Home", callback=log_in_accepted)
            dpg.add_button(label="Rent a new car", callback=rent_new_car)
            dpg.add_menu_item(label="Rented cars", callback=see_rented_cars)
            dpg.add_menu_item(label="Options", callback=options)
            # dpg.add_button(label="Log Out", callback=lg.log_out)

        dpg.add_text("Main menu", tag="renterMainMenuText")


def rent_new_car():
    delete_windows.delete_windows_func()
    with dpg.window(label="Renter Control Panel", tag="Renter New Car", width=400, height=400):
        dpg.set_primary_window("Renter New Car", True)
        with dpg.menu_bar(label="Menu Bar"):
            # dpg.add_menu_item(label="Rent a new car")
            dpg.add_button(label="Home", callback=log_in_accepted)
            dpg.add_button(label="Rent a new car", callback=rent_new_car)
            dpg.add_menu_item(label="Rented cars", callback=see_rented_cars)
            dpg.add_menu_item(label="Options", callback=options)
        first_key = car_list[0]
        second_key = car_list[1]
        third_key = car_list[2]
        dpg.add_button(label=first_key.nickname(), callback=car, user_data=first_key)
        dpg.add_button(label=second_key.nickname(), callback=car, user_data=second_key)
        dpg.add_button(label=third_key.nickname(), callback=car, user_data=third_key)
        dpg.add_text("Rent new car")


def car(sender, app_data, user_data):
    delete_windows.delete_windows_func()
    with dpg.window(label="Renter Control Panel", tag="Renter Car", width=400, height=400):
        dpg.set_primary_window("Renter Car", True)
        with dpg.menu_bar(label="Menu Bar"):
            dpg.add_button(label="Home", callback=log_in_accepted)
            dpg.add_button(label="Rent a new car", callback=rent_new_car)
            dpg.add_menu_item(label="Rented cars", callback=see_rented_cars)
            dpg.add_menu_item(label="Options", callback=options)
        dpg.add_text(user_data.nickname())
        dpg.add_text(f"Owner: {user_data.owner.name}")
        dpg.add_text(f"Fuel Source: {user_data.fuel_source}")
        dpg.add_text(f"Hourly Rate: {user_data.hourly_rate}kr")
        dpg.add_text(f"Daily Rate: {user_data.daily_rate}kr")
        dpg.add_text("SELECT DATE/DATES HERE")
        dpg.add_date_picker(tag="from_date", default_value={'month_day': date.day, 'year': date.year, 'month': date.
                            month}, callback=booking)
        dpg.add_date_picker(tag="to_date", default_value={'month_day': date.day + 1, 'year': date.year, 'month': date.
                            month}, callback=booking)
        dpg.add_button(label="Book")

        # dpg.add_button(label="RENT", callback=rentCar, user_data=)


def booking():
    from_date = (dpg.get_value("from_date"))
    to_date = (dpg.get_value("to_date"))
    print(from_date)
    print(to_date)


def see_rented_cars():
    delete_windows.delete_windows_func()
    with dpg.window(label="Renter Control Panel", tag="Renter See Cars", width=400, height=400):
        dpg.set_primary_window("Renter See Cars", True)
        with dpg.menu_bar(label="Menu Bar"):
            # dpg.add_menu_item(label="Rent a new car")
            dpg.add_button(label="Home", callback=log_in_accepted)
            dpg.add_button(label="Rent a new car", callback=rent_new_car)
            dpg.add_menu_item(label="Rented cars", callback=see_rented_cars)
            dpg.add_menu_item(label="Options", callback=options)

        dpg.add_text("See rented cars")


def options():
    delete_windows.delete_windows_func()
    with dpg.window(label="Renter Control Panel", tag="Renter Options", width=400, height=400):
        dpg.set_primary_window("Renter Options", True)
        with dpg.menu_bar(label="Menu Bar"):
            # dpg.add_menu_item(label="Rent a new car")
            dpg.add_button(label="Home", callback=log_in_accepted)
            dpg.add_button(label="Rent a new car", callback=rent_new_car)
            dpg.add_menu_item(label="Rented cars", callback=see_rented_cars)
            dpg.add_menu_item(label="Options", callback=options)

        dpg.add_text("Options")
