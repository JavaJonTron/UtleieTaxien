import dearpygui.dearpygui as dpg

from main import save_system
from Booking import booking
from main import renter_list
from main import bookings_list
from functions import logged_in_status_file

# Not testable
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

# Not testable
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

def check_if_renter_can_afford(car, renter_logged):
    rental_price = car.price_calculation(2, hours=None)
    print(f'før betaling{renter_logged.money}')
    if renter_logged.money >= rental_price:

        renter_logged.wallet(-rental_price)
        print(f'etter betaling{renter_logged.money}')
        print("JA DETTE HAR VI RÅD TIL")
        return True
    else:
        print("TAPER DETTE HADDE DU IKKE RÅD TIL")
        return False



def create_book(from_date, to_date, renter_logged, car, no_day_crash):
    if check_if_from_day_is_lesser_than_to_day(from_date, to_date):
        if no_day_crash == 0:
            if check_if_renter_can_afford(car, renter_logged):
                booking_object = booking.Booking(renter_logged, from_date, to_date, car, False)
                bookings_list.append(booking_object)
                save_system('booking_file', bookings_list)
                return booking_object


def check_if_from_day_is_lesser_than_to_day(from_date, to_date):
    if from_date["Year_Day"] < to_date["Year_Day"]:
        return True
    else:
        return False


def check_if_booking_date_crashes_with_previous_booking_date(new_to_date, new_from_date, old_to_date, old_from_date):
    if new_from_date < old_from_date and new_to_date < old_from_date or new_from_date > old_to_date and new_to_date > old_to_date:
        return True
    else:
        return False



def booking_func(sender, app_data, user_data):
    dict_new_dates_from = dates_from()
    dict_new_dates_to = dates_to()
    chosen_car = user_data
    renter_logged_in = logged_in_status_file.logged_in_status(renter_list)
    booking_list_number = 0
    if len(bookings_list) > 0:
        times_dates_crash = 0
        for old_booked in bookings_list:
            booking_list_number += 1
            if chosen_car.license_plate == old_booked.car.license_plate:
                if check_if_booking_date_crashes_with_previous_booking_date(dict_new_dates_to["Year_Day"],
                                                                            dict_new_dates_from["Year_Day"],
                                                                            old_booked.date_to["Year_Day"],
                                                                            old_booked.date_from["Year_Day"]):
                    if booking_list_number == len(bookings_list):
                        create_book(dict_new_dates_from, dict_new_dates_to, renter_logged_in, chosen_car,
                                    times_dates_crash)
                        return
                else:
                    times_dates_crash += 1
                    if booking_list_number == len(bookings_list):
                        create_book(dict_new_dates_from, dict_new_dates_to, renter_logged_in, chosen_car,
                                    times_dates_crash)
                        return
            else:
                if booking_list_number == len(bookings_list):
                    create_book(dict_new_dates_from, dict_new_dates_to, renter_logged_in, chosen_car, times_dates_crash)
                    return
    elif len(bookings_list) == 0:
        print(len(bookings_list))
        create_book(dict_new_dates_from, dict_new_dates_to, renter_logged_in, chosen_car, 0)
