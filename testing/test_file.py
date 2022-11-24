import pytest
from pytest_mock import mocker
from renter.renter import Renter
from owner.owner import Owner
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
def renter():
    renter1 = Renter(20, "Male", "Nils Nilselsen", 10, True, 100)
    return renter1
@pytest.fixture
def owner():
    owner1 = Owner(30, "Female", "Nora Norasen", 10, True, 200)
    return owner1
@pytest.fixture
def car():
    car1 = Car("Tesla", "Model X", 2022, "EE12345", "Electric", 150, False, 300, 6000, owner, 0)
    return car1


def test_booking_created_succesfully(dates_from, dates_to, renter, car):
    no_day_crash = False
    booking_object = create_booking_file.create_book(dates_from, dates_to, renter, car, no_day_crash)
    assert booking_object.car.license_plate == "EE12345"
    #mocker.patch("src.Booking.create_booking_file.create_book", return_value=X)



# self, make, model, year, license_plate, fuel_source, km, is_take, hourly_rate, daily_rate, owner, earned_total
# Må lage en owner først fordi car objektet bruker en referanse til Owner
# Undersøk på mulig Integrasjons test?



# def test_write_to_file():
# FileHandling.file_handler_pickle.write_method("","")

# pass


# def read_from_file(
#    pass
