import dearpygui.dearpygui as dpg
import payment.paymentorder
from main import save_system
from Booking import booking
from main import renter_list
from main import bookings_list
from functions import logged_in_status_file


def dates_to():
    """
    Ikke testbar
    Henter til datoene fra date picker i menu_main.
    :return: En dictionary med til datoer.
    """
    dict_dates_to = {}
    to_date = dpg.get_value("to_date")
    to_day = int(to_date["month_day"])
    to_month = int(to_date["month"]) + 1
    to_year = int(to_date["year"]) + 1900
    to_yearday = int(to_date["year_day"])

    dict_dates_to["Day"] = to_day
    dict_dates_to["Month"] = to_month
    dict_dates_to["Year"] = to_year
    dict_dates_to["Year_Day"] = to_yearday
    return dict_dates_to


def dates_from():
    """
    Ikke testbar
    Henter fra datoene fra date picker i menu_main
    :return: En dictionary med fra datoer.
    """
    dict_dates_from = {}
    from_date = dpg.get_value("from_date")
    from_day = int(from_date["month_day"])
    from_month = int(from_date["month"]) + 1
    from_year = int(from_date["year"]) + 1900
    from_yearday = int(from_date["year_day"])

    dict_dates_from["Day"] = from_day
    dict_dates_from["Month"] = from_month
    dict_dates_from["Year"] = from_year
    dict_dates_from["Year_Day"] = from_yearday
    return dict_dates_from


def creating_payment_order(amount):
    """
    Legger hvor mye prisen koster i en parameter og returnerer dette.
    :param amount: Hvor mye bilen koster å leie
    :return: Kostnad for bilen
    """
    order = payment.paymentorder.PaymentOrder(amount)
    return order


def check_if_renter_can_afford(car, renter_logged, year_day_to, year_day_from):
    """
    Sjekker om renter har råd til å leie bilen
    :param car: Bil objekt
    :param renter_logged: Leier som er innlogget
    :param year_day_to: Dagen i året til dato
    :param year_day_from: Dagen i året fra dato
    :return: True eller False ut ifra om leier har råd eller ikke
    """
    rental_price = car.price_calculation(year_day_to - year_day_from + 1, hours=None)
    if renter_logged.wallet.money >= rental_price:
        return True
    else:
        return False


def create_book(from_date, to_date, renter_logged, car, no_day_crash):
    """
    Oppretter et booking object, legger det til i listen over booking objekter og lagrer booking listen
    :param from_date: Fra datoer
    :param to_date: Til datoer
    :param renter_logged: Innlogget leier
    :param car: Bil objekt
    :param no_day_crash: Int som er 0 om ingen andre har booket bilen på disse datoene
    :return: Booking objektet
    """
    rental_price = car.price_calculation(to_date["Year_Day"] - from_date["Year_Day"] + 1, hours=None)
    if check_if_from_day_is_lesser_than_to_day(from_date, to_date):
        if no_day_crash == 0:
            if check_if_renter_can_afford(car, renter_logged, to_date["Year_Day"], from_date["Year_Day"]):
                booking_object = booking.Booking(renter_logged, from_date, to_date, car, False, creating_payment_order(rental_price))
                booking_object.order.booking = booking_object
                booking_object.order.payment_reservation()
                bookings_list.append(booking_object)
                save_system('booking_file', bookings_list)
                return booking_object


def check_if_from_day_is_lesser_than_to_day(from_date, to_date):
    """
    Sjekker om fra dagen er mindre enn til dato
    :param from_date: Fra datoer i booking request
    :param to_date: Til datoer i booking request
    :return: True eller False utifra om fra dagen er mindre eller større enn til dag
    """
    if from_date["Year_Day"] < to_date["Year_Day"]:
        return True
    else:
        return False


def check_if_booking_date_crashes_with_previous_booking_date(new_to_date, new_from_date, old_to_date, old_from_date):
    """
    Sjekker om bookingen krasjer med en tidligere booking på datoer
    :param new_to_date: Til dag for ny booking
    :param new_from_date: Fra dag for ny booking
    :param old_to_date:Fra dag for eksisterende booking
    :param old_from_date: Til ag for eksisterende booking
    :return: True eller False utifra om datoene krasjer eller ikke
    """
    if new_from_date < old_from_date and new_to_date < old_from_date or new_from_date > old_to_date and new_to_date > \
            old_to_date:
        return True
    else:
        return False


def compare_car_license_plate(new_car_booking_license_plate, previous_car_booking_license_plate):
    """
    Sammenlikner om skiltnummer i ny booking er lik som i tidligere bookinger
    :param new_car_booking_license_plate: Skiltnummer på bil i ny booking
    :param previous_car_booking_license_plate: SKiltnummer på biler i eldre bookinger
    :return: True eller False utifra om skiltnummer krasjer eller ikke
    """
    if new_car_booking_license_plate == previous_car_booking_license_plate:
        return True
    else:
        return False


def list_have_reached_end(end_list, obj):
    """
    Sjekker om vi har nådd bunnen av en liste
    :param end_list: En liste
    :param obj: Et objekt i listen
    :return: True eller Flase utifra om slutten på listen er nådd
    """
    if end_list.index(obj) + 1 == len(end_list):
        return True
    else:
        return False


def list_bigger_then_0(list_to_check):
    """
    Sjekker om listen er større enn 0
    :param list_to_check: Listen som skal sjekke
    :return: True eller False utifra om listen er større enn 0 eller ikke
    """
    if len(list_to_check) > 0:
        return True
    else:
        return False


def booking_func(sender, app_data, user_data):
    """
    Denne funksjonen kalles når man trykker på Book knappen når man skal leie en ny bil.
    Denne samler inn all data og bruker funksjoner over til å sørge for at ingenting krasjer og om bilen er ledig på
    datoene leier ber om kaller denne på create_book().
    :param sender: Ikke i bruk
    :param app_data: Ikke i bruk
    :param user_data: Ikke i bruk
    :return:
    """
    chosen_car = user_data
    dict_new_dates_from = dates_from()
    dict_new_dates_to = dates_to()
    renter_logged_in = logged_in_status_file.get_user_logged_in_status(renter_list)
    if list_bigger_then_0(bookings_list):
        times_dates_crash = 0
        for old_booked in bookings_list:
            if compare_car_license_plate(chosen_car.license_plate, old_booked.car1.license_plate):
                if check_if_booking_date_crashes_with_previous_booking_date(dict_new_dates_to["Year_Day"],
                                                                            dict_new_dates_from["Year_Day"],
                                                                            old_booked.date_to["Year_Day"],
                                                                            old_booked.date_from["Year_Day"]):
                    if list_have_reached_end(bookings_list, old_booked):
                        create_book(dict_new_dates_from, dict_new_dates_to, renter_logged_in, chosen_car,
                                    times_dates_crash)
                        return
                else:
                    times_dates_crash += 1
            elif not compare_car_license_plate(chosen_car.license_plate, old_booked.car1.license_plate):
                if list_have_reached_end(bookings_list, old_booked):
                    create_book(dict_new_dates_from, dict_new_dates_to, renter_logged_in, chosen_car, times_dates_crash)
                    return
    elif not list_bigger_then_0(bookings_list):
        create_book(dict_new_dates_from, dict_new_dates_to, renter_logged_in, chosen_car, 0)
