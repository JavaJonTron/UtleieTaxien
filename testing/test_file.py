from Booking import create_booking_file

def test_create_booking_function():
    from_day = {"Day":1, "Month":11, "Year":2022, "Year_Day":304}
    to_day = {"Day":2, "Month":11, "Year":2022, "Year_Day":305}
    old_from_day = {"Day":4, "Month":11, "Year":2022, "Year_Day":307}
    old_to_day = {"Day":6, "Month":11, "Year":2022, "Year_Day":309}

    assert create_booking_file.check_if_booking_date_crashes_with_previous_booking_date(to_day, from_day, old_to_day, old_from_day) is True