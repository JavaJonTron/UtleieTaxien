import dearpygui.dearpygui as dpg
from dearpygui import dearpygui as dpg
from functions import delete_windows
from Booking import create_booking_file
from functions import get_todays_date as date
from functions import gui_main_menu_functions as gui_func
from functions import log_off_func
from functions import logged_in_status_file
from main import bookings_list
from main import renter_list
from main import car_list
from main import owner_list
dpg.create_context()

dpg.create_viewport(title='Utleie_app', width=600, height=600)


# with dpg.window(label="RENTER", tag="RENTER"):
# dpg.add_text("Dette er en test tekst")

def admin_Login():
    dpg.delete_item("Admin Login")
    dpg.delete_item("Main menu")
    #dpg.hide_item("Main menu")
    with dpg.window(label="Admin Login", tag="Admin Login", width=300, height=200):
        dpg.set_primary_window("Admin Login", True)
        dpg.add_text("Username:")
        dpg.add_input_text(tag="Admin username")
        dpg.add_text("Password:")
        dpg.add_input_text(tag="Admin password")
        dpg.add_button(label="Log in", tag="adminLogInButton", callback=log_in_accepted)

def owner_Login():
    dpg.delete_item("Owner Login")
    dpg.delete_item("Main menu")
    #dpg.hide_item("Main menu")
    with dpg.window(label="Owner Login", tag="Owner Login", width=300, height=200):
        dpg.set_primary_window("Owner Login", True)
        dpg.add_text("Username:")
        dpg.add_input_text(tag="Owner username")
        dpg.add_text("Password:")
        dpg.add_input_text(tag="Owner password")
        dpg.add_button(label="Owner 1 Log in", tag="owner1LogInButton", callback=log_in_accepted,
                       user_data=owner_list[0])
        dpg.add_button(label="Owner 2 Log in", tag="owner2LogInButton", callback=log_in_accepted,
                       user_data=owner_list[1])
        # dpg.add_button(label="Owner Log in with Google", tag="ownerLogInGoogleButton", callback=gui_owner_func.log_in_accepted)
        # dpg.add_button(label="Owner Log in with Vipps", tag="ownerLogInVippsButton", callback=gui_owner_func.log_in_accepted)

def renter_Login():
    dpg.delete_item("Renter Login")
    dpg.delete_item("Main menu")
    #dpg.hide_item("Main menu")
    with dpg.window(label="Renter Login", tag="Renter Login", width=300, height=200):
        dpg.set_primary_window("Renter Login", True)
        dpg.add_text("Username:")
        dpg.add_input_text(tag="Renter username")
        dpg.add_text("Password:")
        dpg.add_input_text(tag="Renter password")
        dpg.add_button(label="Renter 1 Log in", tag="renter1LogInButton", callback=log_in_accepted,
                       user_data=renter_list[0])
        dpg.add_button(label="Renter 2 Log in", tag="renter2LogInButton", callback=log_in_accepted,
                       user_data=renter_list[1])
        dpg.add_button(label="Renter Log in", tag="renterLogInButton")
        dpg.add_button(label="Renter Log in with Google", tag="renterLogInGoogleButton")
        dpg.add_button(label="Renter Log in with Vipps", tag="renterLogInVippsButton")


def main_menu():
    with dpg.window(label="Main menu", tag="Main menu"):
        dpg.add_text("Log in")
        dpg.add_button(label="Log in as renter", tag="renterLogin", callback=renter_Login)
        dpg.add_button(label="Log in as owner", tag="ownerLogin", callback=owner_Login)
        dpg.add_button(label="Log in as admin", tag="adminLogin", callback=admin_Login)
        dpg.set_primary_window("Main menu", True)


main_menu()


def log_out():
    delete_windows.delete_windows_func()
    log_off_func.log_off_human(renter_list)
    main_menu()

    # for renter in log_off_func(renter_list):
    #   renter.is_logged_in = False
    # dpg.hide_item("Main menu", False)


def log_in_accepted(sender, app_data, user_data):
    delete_windows.delete_windows_func()
    for renter in renter_list:
        renter.is_logged_in = False
    logged_in_user = user_data
    logged_in_user.is_logged_in = True
    with dpg.window(label="Renter Control Panel", tag="Renter Login Accepted", width=400, height=400):
        dpg.set_primary_window("Renter Login Accepted", True)
        dpg.add_text(f"Successfully logged in as {user_data.name}")
        dpg.add_button(label="Click me to continue", callback=renter_main_menu, user_data=logged_in_user)


def renter_main_menu(sender, app_data, user_data):
    delete_windows.delete_windows_func()
    logged_in_user = user_data
    with dpg.window(label="Renter Control Panel", tag="Renter Main", width=400, height=400):
        dpg.set_primary_window("Renter Main", True)
        with dpg.menu_bar(label="Menu Bar"):
            dpg.add_button(label="Home", callback=log_in_accepted)
            dpg.add_button(label="Rent a new car", callback=rent_new_car, user_data=logged_in_user)
            dpg.add_menu_item(label="Rented cars", callback=see_rented_cars, user_data=logged_in_user)
            dpg.add_menu_item(label="Options", callback=options)
            dpg.add_menu_item(label="Log Out", callback=log_out)
            dpg.add_button(label="Log Out", callback=log_out)

        dpg.add_text("Main menu", tag="renterMainMenuText")


def rent_new_car(sender, app_data, user_data):
    delete_windows.delete_windows_func()
    with dpg.window(label="Renter Control Panel", tag="Renter New Car", width=400, height=400):
        dpg.set_primary_window("Renter New Car", True)
        with dpg.menu_bar(label="Menu Bar"):
            # dpg.add_menu_item(label="Rent a new car")
            dpg.add_button(label="Home", callback=renter_main_menu, user_data=user_data)
        first_key = car_list[0]
        second_key = car_list[1]
        third_key = car_list[2]
        dpg.add_button(label=first_key.nickname(), callback=car, user_data=first_key)
        dpg.add_button(label=second_key.nickname(), callback=car, user_data=second_key)
        dpg.add_button(label=third_key.nickname(), callback=car, user_data=third_key)
        dpg.add_text("Rent new car")


def car(sender, app_data, user_data):
    logged_in_user = logged_in_status_file.logged_in_status(renter_list)
    avail_list = []
    delete_windows.delete_windows_func()
    with dpg.window(label="Renter Control Panel", tag="Renter Car", width=400, height=400):
        dpg.set_primary_window("Renter Car", True)
        with dpg.menu_bar(label="Menu Bar"):
            dpg.add_button(label="Home", callback=renter_main_menu, user_data=logged_in_user)
        dpg.add_text(user_data.nickname())
        dpg.add_text(f"Owner: {user_data.owner.name}")
        dpg.add_text(f"Fuel Source: {user_data.fuel_source}")
        dpg.add_text(f"Hourly Rate: {user_data.hourly_rate}kr")
        dpg.add_text(f"Daily Rate: {user_data.daily_rate}kr")
        dpg.add_text("FROM DATE:")
        dpg.add_date_picker(tag="from_date", default_value={'month_day': date.day, 'year': date.year, 'month': date.
                            month}, callback=create_booking_file.dates_from)
        dpg.add_text("TO DATE:")
        dpg.add_date_picker(tag="to_date", default_value={'month_day': date.day + 1, 'year': date.year, 'month': date.
                            month}, callback=create_booking_file.dates_to)
        dpg.add_button(label="Book", callback=create_booking_file.booking_func, user_data=user_data)
        dpg.add_text("Car is not available between:")
        for booking in bookings_list:
            if booking.car.license_plate == user_data.license_plate:
                date_from_day = booking.date_from["Day"]
                date_from_month = booking.date_from["Month"]
                date_from_year = booking.date_from["Year"]
                date_to_day = booking.date_to["Day"]
                date_to_month = booking.date_to["Month"]
                date_to_year = booking.date_to["Year"]
                avail_list.append(
                    f"{date_from_day}.{date_from_month}.{date_from_year} - {date_to_day}.{date_to_month}.{date_to_year}")
        dpg.add_listbox(tag="dates", items=avail_list)


def see_rented_cars(sender, app_data, user_data):
    temp_holder_user_data = user_data
    rented_cars = []
    delete_windows.delete_windows_func()
    with dpg.window(label="Renter Control Panel", tag="Renter See Cars", width=400, height=400):
        dpg.set_primary_window("Renter See Cars", True)
        with dpg.menu_bar(label="Menu Bar"):
            dpg.add_button(label="Home", callback=renter_main_menu, user_data=temp_holder_user_data)
        for booking in bookings_list:
            if booking.renter.name == user_data.name:
                rented_cars.append(f"{booking.car.nickname()}, {booking.date_from['Day']}.{booking.date_from['Month']}."
                                   f"{booking.date_from['Year']}-{booking.date_to['Day']}.{booking.date_to['Month']}."
                                   f"{booking.date_to['Year']}")
        dpg.add_listbox(tag="rented", items=rented_cars)
        dpg.add_text("See rented cars")


def options():
    delete_windows.delete_windows_func()
    with dpg.window(label="Renter Control Panel", tag="Renter Options", width=400, height=400):
        dpg.set_primary_window("Renter Options", True)
        with dpg.menu_bar(label="Menu Bar"):
            # dpg.add_menu_item(label="Rent a new car")
            dpg.add_button(label="Home", callback=renter_main_menu)

        dpg.add_text("Options")






















dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()


