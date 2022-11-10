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


def booking_func(sender, app_data, user_data):
    print("\n--------------------------------------")
    print("--------------------------------------")
    print("--------------------------------------\n")
    dict_new_dates_from = dates_from()
    dict_new_dates_to = dates_to()
    chosen_car = user_data
    renter_logged_in = object
    car_object = object
    for renter in renter_list:
        if renter.is_logged_in is True:
            renter_logged_in = renter

    car_licenseplates = []
    car_from_dates = []
    car_to_dates = []

    car_object = booking.Booking(renter_logged_in, dict_new_dates_from, dict_new_dates_to, chosen_car)
    bookings_list.append(car_object)
    main.save_system("booking_file", bookings_list)

    #    for old_booked_cars in bookings_list:
    #        car_licenseplates.append(old_booked_cars.car.license_plate)

    for old_booked_dates_from in bookings_list:
        car_from_dates.append(old_booked_dates_from.date_from["Year_Day"])
        print(car_from_dates)

    for old_booked_dates_to in bookings_list:
        car_to_dates.append(old_booked_dates_to.date_to["Year_Day"])
        print(car_to_dates)



    #if chosen_car.license_plate in car_licenseplates:
        #if dict_new_dates_from["Year_Day"]:






#date_from_day = booking.date_from["Day"]
#date_from_month = booking.date_from["Month"]

#SÅ lenge man booker bil på samme måned som en tidligere booking har  SÅ:
	#NY FRA DAG kan ikke være lik eller større en GAMMEL FRA DAG og samtidig ikke mindre eller lik GAMMEL TIL DAG
	#NY TIL DAG kan ikke være lik eller større en GAMMEL FRA DAG og samtidig ikke mindre eller lik GAMMEL TIL DAG
