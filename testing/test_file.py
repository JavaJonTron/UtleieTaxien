import pytest
from pytest_mock import mocker

from Booking import create_booking_file
from FileHandling import file_handler_pickle
from Car.car import Car


def test_dates_dont_crash():
    from_day = {"Day": 1, "Month": 11, "Year": 2022, "Year_Day": 304}
    to_day = {"Day": 2, "Month": 11, "Year": 2022, "Year_Day": 305}
    old_from_day = {"Day": 4, "Month": 11, "Year": 2022, "Year_Day": 307}
    old_to_day = {"Day": 6, "Month": 11, "Year": 2022, "Year_Day": 309}
    assert create_booking_file.check_if_booking_date_crashes_with_previous_booking_date(to_day["Year_Day"],
                                                                                        from_day["Year_Day"],
                                                                                        old_from_day["Year_Day"],
                                                                                        old_to_day[
                                                                                            "Year_Day"]) is True


def test_dates_do_crash():
    from_day = {"Day": 1, "Month": 11, "Year": 2022, "Year_Day": 304}
    to_day = {"Day": 2, "Month": 11, "Year": 2022, "Year_Day": 306}
    old_from_day = {"Day": 4, "Month": 11, "Year": 2022, "Year_Day": 305}
    old_to_day = {"Day": 6, "Month": 11, "Year": 2022, "Year_Day": 309}
    assert create_booking_file.check_if_booking_date_crashes_with_previous_booking_date(to_day["Year_Day"],
                                                                                        from_day["Year_Day"],
                                                                                        old_to_day["Year_Day"],
                                                                                        old_from_day[
                                                                                            "Year_Day"]) is False


def test_from_day_is_lesser_than_to_day():
    from_day = {"Year_Day": 304}
    to_day = {"Year_Day": 306}
    assert create_booking_file.check_if_from_day_is_lesser_than_to_day(from_day, to_day) is True


def test_from_day_is_bigger_than_to_day():
    from_day = {"Year_Day": 307}
    to_day = {"Year_Day": 306}
    assert create_booking_file.check_if_from_day_is_lesser_than_to_day(from_day, to_day) is False


def test_read_and_write_to_and_from_file():
    write_to_Information = "TEST_INFORMATION"
    filskriving = file_handler_pickle.File_handler_pickle("Test_file", write_to_Information)
    filskriving.write_method()
    assert filskriving.read_method() == write_to_Information


def test_car_nickname():
    make = "Tesla"  # input("Make: ").upper()
    model = "Model Y"  # input("Model: ").upper()
    year = 2022  # int(input("Year: "))
    license_plate = "ED15421"  # input("License plate: ").upper()
    fuel_source = "Electric" # input("Fuel source: ").upper()
    km = 20500  # int(input("Odometer: "))
    is_take = False
    hourly_rate = 150
    daily_rate = 3000
    car_object = Car(make, model, year, license_plate, fuel_source, km, is_take, hourly_rate, daily_rate, None, None)
    assert car_object.nickname() == f'{year} {make} {model}'

def test_booking_created_succesfully():
    mocker.patch("")



# self, make, model, year, license_plate, fuel_source, km, is_take, hourly_rate, daily_rate, owner, earned_total
# Må lage en owner først fordi car objektet bruker en referanse til Owner
# Undersøk på mulig Integrasjons test?



# def test_write_to_file():
# FileHandling.file_handler_pickle.write_method("","")

# pass


# def read_from_file(
#    pass
