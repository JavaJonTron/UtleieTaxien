from dummyObjects import dummyRenter1
from dummyObjects import dummyRenter2
from dummyObjects import dummyOwner1
from dummyObjects import dummyOwner2
from dummyObjects import dummyCar1
from dummyObjects import dummyCar2
from dummyObjects import dummyCar3

owner_list = []
car_list = []
renter_list = []
bookings_list = []


def dummy_owner_creation():
    dummyOwnerList = []
    dummyOwnerList.append(dummyOwner1)
    dummyOwnerList.append(dummyOwner2)
    for dummy in dummyOwnerList:
        owner = dummy.create_owner()
        owner_list.append(owner)
    for obj in owner_list:
        print(obj)
    print(owner_list)


dummy_owner_creation()


def dummy_car_creation(owners):
    car = dummyCar1.create_car(owners[0])
    car_list.append(car)
    car = dummyCar2.create_car(owners[0])
    car_list.append(car)
    car = dummyCar3.create_car(owners[1])
    car_list.append(car)


def dummy_renter_creation():
    dummyRenterList = []
    dummyRenterList.append(dummyRenter1)
    dummyRenterList.append(dummyRenter2)
    for dummy in dummyRenterList:
        renter = dummy.create_renter()
        renter_list.append(renter)
    for obj in renter_list:
        print(obj)
    print(renter_list)


dummy_renter_creation()

dummy_car_creation(owner_list)
