import pytest
from pytest_mock import mocker

import renter.renter
from functions import log_off_func
import functions.get_average_of_list
from renter.renter import Renter
from owner.owner import Owner
from Booking import create_booking_file
from FileHandling import file_handler_pickle
from Car.car import Car
from functions import logged_in_status_file
from functions.checking_object_instance import checking_object_instance
from Booking.booking import Booking
from functions.approved_or_deny_booking import approved_or_deny_booking
from Booking.create_booking_file import check_if_renter_can_afford

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
    fuel_source = "Electric"  # input("Fuel source: ").upper()
    km = 20500  # int(input("Odometer: "))
    is_take = False
    hourly_rate = 150
    daily_rate = 3000
    car_object = Car(make, model, year, license_plate, fuel_source, km, is_take, hourly_rate, daily_rate, None, None)
    assert car_object.nickname() == f'{year} {make} {model}'


@pytest.fixture
def dates_from():
    dict_dates_from = {"Day": 1, "Month": 1, "Year": 2022, "Year_Day": 0}
    return dict_dates_from


@pytest.fixture
def dates_to():
    dict_dates_to = {"Day": 2, "Month": 1, "Year": 2022, "Year_Day": 1}
    return dict_dates_to


@pytest.fixture
def renters():
    renter1 = Renter(20, "Male", "Nils Nilselsen", 10, True, 100000)
    return renter1

@pytest.fixture
def renters2():
    renter2 = Renter(25, "Female", "Oda Odasen", 50, True, 1000)
    return renter2


@pytest.fixture
def owners():
    owner1 = Owner(30, "Female", "Nora Norasen", 10, True, 200,)
    return owner1


@pytest.fixture
def car(owners):
    car1 = Car("Tesla", "Model X", 2022, "EE12345", "Electric", 150, False, 300, 6000, owners, 0)
    return car1

@pytest.fixture
def booking(renters, dates_from, dates_to, car):
    approved = False
    booking1 = Booking(renters, dates_from, dates_to, car, approved)
    return booking1

def test_booking_created_with_correct_information(dates_from, dates_to, renters, car):
    no_day_crash = False
    booking_object = create_booking_file.create_book(dates_from, dates_to, renters, car, no_day_crash)
    assert booking_object.car.license_plate == "EE12345"
    assert booking_object.car.owner.age == 30
    assert booking_object.renter.name == "Nils Nilselsen"
    assert booking_object.date_from["Day"] == 1


def test_booking_created_not_with_correct_information(dates_from, dates_to, renters, car):
    no_day_crash = False
    booking_object = create_booking_file.create_book(dates_from, dates_to, renters, car, no_day_crash)
    assert booking_object.car.license_plate != "EE12346"
    assert booking_object.car.owner.age == 30
    assert booking_object.renter.name != "Nil Nilselsen"
    assert booking_object.date_from["Day"] != 0


def test_calculates_the_correct_average():
    list_of_numbers = [1, 2, 3, 4, 5]
    average = functions.get_average_of_list.average_list(list_of_numbers)
    assert average == 3


def test_calculates_the_wrong_average():
    list_of_numbers = [1, 2, 3, 4, 5]
    average = functions.get_average_of_list.average_list(list_of_numbers)
    assert average != 6


def test_logging_off_all_humans_successfully(owners, renters):
    list_of_humans = [owners, renters]
    log_off_func.log_off_human(list_of_humans)
    assert list_of_humans[0].is_logged_in == False
    assert list_of_humans[1].is_logged_in == False

def test_correct_person_logged_in(owners):
    list_of_owners = [owners]
    assert logged_in_status_file.logged_in_status(list_of_owners) == owners

def test_object_is_correct_instance(renters):
    assert checking_object_instance(renters, renter.renter.Renter) == True

def test_object_is_not_correct_instance(renters):
    assert checking_object_instance(owners, renter.renter.Renter) == False

def test_renter_can_afford(car, renters):
    can_afford = check_if_renter_can_afford(car, renters)
    assert can_afford == True

def test_renter_can_not_afford(car, renters2):
    can_not_afford = check_if_renter_can_afford(car, renters2)
    assert can_not_afford == False

def test_booking_approved(booking, car, renters):
    decision = True
    booking_list = [booking]
    approved_or_deny_booking(booking, decision, booking_list)
    assert booking.approved == decision

def test_booking_not_approved(booking, car, renters):
    decision = False
    booking_list = [booking]
    approved_or_deny_booking(booking, decision, booking_list)
    assert booking.approved == decision
