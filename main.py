from FileHandling import file_handler_pickle
from dummyObjects import dummyOwner1, dummyOwner2, dummyCar2, dummyCar3, dummyCar1, dummyRenter1, dummyRenter2, \
    dummyAdmin1

owner_list = []
car_list = []
renter_list = []
bookings_list = []
admin_list = []


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


def dummy_car_creation(owners):
    car = dummyCar1.create_car(owners[0])
    # filskriving = file_handler_pickle.File_handler_pickle("car_file", car)
    # filskriving.write_method()
    car_list.append(car)
    car = dummyCar2.create_car(owners[0])
    car_list.append(car)
    car = dummyCar3.create_car(owners[1])
    car_list.append(car)
    # del filskriving


def dummy_admin_creation():
    admin = dummyAdmin1.create_admin()
    admin_list.append(admin)
    # del filskriving


def dummy_owner_creation():
    dummyOwnerList = []
    dummyOwnerList.append(dummyOwner1)
    dummyOwnerList.append(dummyOwner2)
    for dummy in dummyOwnerList:
        print(dummy)
        owner = dummy.create_owner()
        owner_list.append(owner)
    # filskriving = file_handler_pickle.File_handler_pickle("owner_file", owner)
    # filskriving.write_method()
    # del filskriving


def dummy_renter_creation():
    dummyRenterList = []
    dummyRenterList.append(dummyRenter1)
    dummyRenterList.append(dummyRenter2)
    for dummy in dummyRenterList:
        renter = dummy.create_renter()
        renter_list.append(renter)
    # filskriving = file_handler_pickle.File_handler_pickle("renter_file", renter)
    # filskriving.write_method()
    # del filskriving


dummy_owner_creation()
dummy_renter_creation()
dummy_car_creation(owner_list)
dummy_admin_creation()

load_system('owner_file', owner_list)
load_system('renter_file', renter_list)
load_system('car_file', car_list)
load_system('booking_file', bookings_list)
load_system('admin_file', admin_list)

save_system('admin_file', admin_list)
save_system('owner_file', owner_list)
save_system('renter_file', renter_list)
save_system('car_file', car_list)
save_system('booking_file', bookings_list)


# load_system(r'Storage\owner_file', owner_list)
# load_system(r'Storage\renter_file', renter_list)
# load_system(r'Storage\car_file', car_list)
# load_system(r'Storage\booking_file', bookings_list)

# save_system(r'Storage\owner_file', owner_list)
# save_system(r'Storage\renter_file', renter_list)
# save_system(r'Storage\car_file', car_list)
# save_system(r'Storage\booking_file', bookings_list)
