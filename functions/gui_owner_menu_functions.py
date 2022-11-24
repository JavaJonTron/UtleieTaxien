from main import owner_list
import atexit
from main import save_system
from main import renter_list
from main import car_list
from main import bookings_list

def avslutt():
    save_system("owner_file", owner_list)
    save_system("renter_file", renter_list)
    save_system("car_file", car_list)
    save_system("booking_file", bookings_list)
    print("AVSLUTTES")

atexit.register(avslutt)
