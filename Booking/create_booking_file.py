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
    dict_dates_to["Day"] = to_day
    dict_dates_to["Month"] = to_month
    dict_dates_to["Year"] = to_year
    return dict_dates_to


def dates_from():
    dict_dates_from = {}
    from_date = (dpg.get_value("from_date"))
    from_day = int(from_date["month_day"])
    from_month = (int(from_date["month"])) + 1
    from_year = (int(from_date["year"])) + 1900

    dict_dates_from["Day"] = from_day
    dict_dates_from["Month"] = from_month
    dict_dates_from["Year"] = from_year
    return dict_dates_from


def booking_func(sender, app_data, user_data):
    dict_new_dates_from = dates_from()
    dict_new_dates_to = dates_to()
    chosen_car = user_data
    renter_logged_in = object
    for renter in renter_list:
        if renter.is_logged_in is True:
            renter_logged_in = renter
    if len(bookings_list) > 0:
        for old_booked in bookings_list:
            print(f"old_booked:{old_booked}")
            if chosen_car.license_plate == old_booked.car.license_plate:
                print(f"chosen_car.license_plate{chosen_car.license_plate}")
                print(f"old_booked.car.license_plate{old_booked.car.license_plate}")
                if dict_new_dates_from["Month"] == old_booked.date_from["Month"]:
                    print("Before previous booking:")
                    print(dict_new_dates_from["Day"] < old_booked.date_from["Day"])
                    print(dict_new_dates_to["Day"] < old_booked.date_from["Day"])
                    print("After previous booking:")
                    print(dict_new_dates_from["Day"] > old_booked.date_to["Day"])
                    print(dict_new_dates_to["Day"] > old_booked.date_to["Day"])
                    if dict_new_dates_from["Day"] < old_booked.date_from["Day"] & dict_new_dates_to["Day"] < old_booked.date_from["Day"] or dict_new_dates_from["Day"] > old_booked.date_to["Day"] & dict_new_dates_to["Day"] > old_booked.date_to["Day"]:
                        car_object = booking.Booking(renter_logged_in, dict_new_dates_from, dict_new_dates_to, chosen_car)
                        bookings_list.append(car_object)
                        main.save_system("booking_file", bookings_list)
                    else:
                        print("BZZZZ; CHOOSE AGAIN DUMBASS!")
    elif len(bookings_list) == 0:
        car_object = booking.Booking(renter_logged_in, dict_new_dates_from, dict_new_dates_to, chosen_car)
        bookings_list.append(car_object)
        main.save_system("booking_file", bookings_list)


#date_from_day = booking.date_from["Day"]
#date_from_month = booking.date_from["Month"]

#SÅ lenge man booker bil på samme måned som en tidligere booking har  SÅ:
	#NY FRA DAG kan ikke være lik eller større en GAMMEL FRA DAG og samtidig ikke mindre eller lik GAMMEL TIL DAG
	#NY TIL DAG kan ikke være lik eller større en GAMMEL FRA DAG og samtidig ikke mindre eller lik GAMMEL TIL DAG
