import dearpygui.dearpygui as dpg

import main
from Booking import booking
from main import renter_list
from main import bookings_list


def dates_to():
    dict_dates_to = {}
    to_date = (dpg.get_value("to_date"))
    to_day = int(to_date["month_day"])
    to_month = (int(to_date["month"])) + 1
    to_year = (int(to_date["year"])) + 1900
    to_yearday = int(to_date["year_day"])

    dict_dates_to["Day"] = to_day
    dict_dates_to["Month"] = to_month
    dict_dates_to["Year"] = to_year
    dict_dates_to["Year_Day"] = to_yearday
    return dict_dates_to


def dates_from():
    dict_dates_from = {}
    from_date = (dpg.get_value("from_date"))
    from_day = int(from_date["month_day"])
    from_month = (int(from_date["month"])) + 1
    from_year = (int(from_date["year"])) + 1900
    from_yearday = int(from_date["year_day"])

    dict_dates_from["Day"] = from_day
    dict_dates_from["Month"] = from_month
    dict_dates_from["Year"] = from_year
    dict_dates_from["Year_Day"] = from_yearday
    return dict_dates_from


def create_book(from_date, to_date, renter_logged, car, no_day_crash):
    if from_date["Year_Day"] < to_date["Year_Day"]:
        if no_day_crash == 0:
            car_object = booking.Booking(renter_logged, from_date, to_date, car)
            bookings_list.append(car_object)
            main.save_system("booking_file", bookings_list)
            print("Now we are creating bookings")
        else:
            print("DATES DID CRASH")
    else:
        print("Choose again. from day is bigger then to day ")

def check_if_renter_is_logged_in():
    for renter in renter_list:
        if renter.is_logged_in is True:
            return renter

def check_if_booking_on_a_previously_booked_date():
    pass

#def check_if_booking_on_previously_booked_month():
#    if dates_from()["Month"] == dates_to()["Month"]:
#        return True

def booking_func(sender, app_data, user_data):
    print("\n--------------------------------------")
    print("--------------------------------------")
    print("--------------------------------------\n")
    dict_new_dates_from = dates_from()
    dict_new_dates_to = dates_to()
    chosen_car = user_data

    renter_logged_in = check_if_renter_is_logged_in()

    booking_list_number = 0

    if len(bookings_list) > 0:
        times_dates_crash = 0
        for old_booked in bookings_list:
            booking_list_number += 1
            if chosen_car.license_plate == old_booked.car.license_plate:
                if dict_new_dates_from["Year_Day"] < old_booked.date_from["Year_Day"] and dict_new_dates_to["Year_Day"] < old_booked.date_from["Year_Day"] or dict_new_dates_from["Year_Day"] > old_booked.date_to["Year_Day"] and dict_new_dates_to["Year_Day"] > old_booked.date_to["Year_Day"]:
                    if booking_list_number == len(bookings_list):
                        create_book(dict_new_dates_from, dict_new_dates_to, renter_logged_in, chosen_car, times_dates_crash)
                        return
                else:
                    times_dates_crash += 1
                    if booking_list_number == len(bookings_list):
                        create_book(dict_new_dates_from, dict_new_dates_to, renter_logged_in, chosen_car, times_dates_crash)
                        return
            else:
                if booking_list_number == len(bookings_list):
                    create_book(dict_new_dates_from, dict_new_dates_to, renter_logged_in, chosen_car, times_dates_crash)
                    return
    elif len(bookings_list) == 0:
        print(len(bookings_list))
        create_book(dict_new_dates_from, dict_new_dates_to, renter_logged_in, chosen_car, 0)
