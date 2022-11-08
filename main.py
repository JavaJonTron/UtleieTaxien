from FileHandling import file_handler_pickle
from dummyObjects import dummyOwner1, dummyOwner2, dummyCar2, dummyCar3, dummyCar1, dummyRenter1, dummyRenter2

owner_list = []
car_list = []
renter_list = []
bookings_list = []


def save_system(file, current_list):
    filskriving = file_handler_pickle.File_handler_pickle(file, current_list)
    filskriving.write_method()
    del filskriving


def load_system(file, li):
    filskriving = file_handler_pickle.File_handler_pickle(file, None)
    listen = filskriving.read_method()
    if listen is not None:
        for xx in listen:
            li.append(xx)
        del filskriving


load_system("owner_file", owner_list)
load_system("renter_file", renter_list)
load_system("car_file", car_list)
load_system("booking_file", bookings_list)







save_system("owner_file", owner_list)
save_system("renter_file", renter_list)
save_system("car_file", car_list)
save_system("booking_file", bookings_list)
