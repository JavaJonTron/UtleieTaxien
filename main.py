from dummyObjects import dummyOwner1
from dummyObjects import dummyOwner2
from dummyObjects import dummyCar1
from dummyObjects import dummyCar2
from dummyObjects import dummyCar3
from functions import create_car_file
from functions import create_renter_file

owner_list = []

def owner_creation():
    dummyOwnerList = []
    dummyOwnerList.append(dummyOwner1)
    dummyOwnerList.append(dummyOwner2)

    for dummy in dummyOwnerList:
        owner = dummy.create_owner()
        owner_list.append(owner)
    for obj in owner_list:
        print(obj)
    print(owner_list)


owner_creation()

def car_creation():
    for owner in owner_list:
        if owner.is_logged_in == True:
            print("Test")
    #car_dictionary = {}
    car_list = []
    car = dummyCar1.create_car()
    nickname = str(car.year) + " " + str(car.make) + " " + str(car.model)

    # car_dictionary[nickname] = car
    car = dummyCar2.create_car()
    nickname = str(car.year) + " " + str(car.make) + " " + str(car.model)
    # car_dictionary[nickname] = car
    car = dummyCar3.create_car()
    nickname = str(car.year) + " " + str(car.make) + " " + str(car.model)
    # car_dictionary[nickname] = car
    # print(f"car dict: {car_dictionary}")






###################################
example = None
date_from = "01.01.23"
date_to = "03.01.23"
booking_dictionary = {}
bookings_list = []
renter_list = []

# renter = create_renter_file.create_renter()
# renter_list.append(renter)
# create_booking(renter, "21.08.23", "23.08.23")
for obj in renter_list:
    print("HER KOMMER OBJEKTER FRA RENTER_LIST")
    print(obj.name)

# print("Score: " + str(renter.score))


# cars = {}
# car = create_car_file.create_car()
# nickname = str(car.year) + " " + str(car.make) + " " + str(car.model)
# cars[nickname] = car

# print("License plate: " + str(car.license_plate))
# print("Fuel Source: " + str(car.fuel_source))
# print("Model: " + str(car.model))
# print("Make: " + str(car.make))
# print("Odometer: " + str(car.km))
# print("Year: " + str(car.year))
# print("Nickname: " + nickname)

# Kommenterte ut kode vi ikke har fått til å fungere ennå
# Koden under har vi ikke fått til å fungere ennå
def booking(renter1, date_from1, date_to1, car1):
    booking11 = {"renter": renter1, "date from": date_from1, "date to": date_to1, "car": car1}
    return booking11


# Kommenterte ut kode vi ikke har fått til å fungere ennå
testobjekt = "test booking"
# booking_dictionary[testobjekt] = booking(renter, date_from, date_to, car)
# bookings_list.append(booking_dictionary)

# for k, v in cars.items():
#    print(k, v)


# print (bookings_list[0])

def who_rents_what(renterp):
    print(renterp)

def booking_information():
    for element in bookings_list:
        for k, v in element.items():
            for o, e in v.items():
                if o == 'renter':
                    print("Personen som leier heter følgende")
                    print(e.name)
                    who_rents_what(e)
                if o == 'car':
                    print("Lisensnummeret er følgende")
                    print(e.make)
                    who_rents_what(e.license_plate)
                # print(o)
                # print(e)
            # print(v)
            # print(k=="test booking")
            # print(v == "car")
    return

# booking_information()
# print (eksempel)
