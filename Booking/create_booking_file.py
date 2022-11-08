import dearpygui.dearpygui as dpg

from Booking import booking
from main import renter_list
from main import bookings_list

def dates_to():
    dict_dates_to = {}
    to_date = (dpg.get_value("to_date"))
    to_day = int(to_date["month_day"])
    to_month = (int(to_date["month"])) + 1
    to_year = (int(to_date["year"])) + 1900
    dict_dates_to["Day"] = to_day
    dict_dates_to["Month"] = to_month
    dict_dates_to["Year"] = to_year
    return dict_dates_to


def dates_from():
    dict_dates_from = {}
    from_date = (dpg.get_value("to_date"))
    from_day = int(from_date["month_day"])
    from_month = (int(from_date["month"])) + 1
    from_year = (int(from_date["year"])) + 1900

    dict_dates_from["Day"] = from_day
    dict_dates_from["Month"] = from_month
    dict_dates_from["Year"] = from_year
    return dict_dates_from


def booking_func(sender, app_data, user_data):
    dates_from_dict = dates_from()
    dates_to_dict = dates_to()
    chosen_car = user_data
    renter_logged_in = None
    for renter in renter_list:
        if renter.is_logged_in is True:
            renter_logged_in = renter

    car_object = booking.Booking(renter_logged_in, dates_from_dict, dates_to_dict, chosen_car)
    bookings_list.append(car_object)
