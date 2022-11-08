import dearpygui.dearpygui as dpg
from main import renter_list
from classes import booking
from main import bookings_list


def caledar_booking(sender, app_data, user_data):

    from_date = (dpg.get_value("from_date"))
    from_day = int(from_date["month_day"])
    from_month = (int(from_date["month"])) + 1
    from_year = (int(from_date["year"])) + 1900



def dates_to():
    dict_dates_to = {}
    to_date = (dpg.get_value("to_date"))
    to_day = int(to_date["month_day"])
    to_month = (int(to_date["month"])) + 1
    to_year = (int(to_date["year"])) + 1900
    #dict_dates_to = {"To_day": to_day, to_month, to_year}

    return dict_dates_to


def dates_from():
    pass


def booking_func(sender, app_data, user_data):
    to_date = dates_to()
    chosen_car = user_data
    renter = renter_list[0]

    #car_object = booking.Booking(renter, from_year, from_month, from_day, to_year, to_month, to_day, chosen_car)
    #print(f"Bil objekt: {car_object}")
    #bookings_list.append(car_object)
    #print(f"Booking liste: {bookings_list}")