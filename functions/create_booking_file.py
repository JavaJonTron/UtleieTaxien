from classes.booking import Booking

def create_booking(renter1, year_from, month_from, day_from, year_to, month_to, day_to, car):
    renter = renter1
    return Booking(renter, year_from, month_from, day_from, year_to, month_to, day_to, car)


