from functions import create_car_file
from functions import create_renter_file
eksempel = None
date_from = "01.01.23"
date_to = "03.01.23"
booking_dictionary = {}
bookings_list = []
renter_list = []
owner_list = []
renter = create_renter_file.create_renter()
renter_list.append(renter)
# create_booking(renter, "21.08.23", "23.08.23")
for obj in renter_list:
    print("HER KOMMER OBJEKTER FRA RENTER_LIST")
    print(obj.name)

print("Score: " + str(renter.score))


cars = {}

car = create_car_file.create_car()

nickname = str(car.year) + " " + str(car.make) + " " + str(car.model)
cars[nickname] = car

print("License plate: " + str(car.license_plate))
print("Fuel Source: " + str(car.fuel_source))
print("Model: " + str(car.model))
print("Make: " + str(car.make))
print("Odometer: " + str(car.km))
print("Year: " + str(car.year))
print("Nickname: " + nickname)

#Kommenterte ut kode vi ikke har fått til å fungere ennå
#Koden under har vi ikke fått til å fungere ennå
def booking(renter1, date_from1, date_to1, car1):
   booking11 = {"renter": renter1, "date from": date_from1, "date to": date_to1, "car": car1}
   return booking11

#Kommenterte ut kode vi ikke har fått til å fungere ennå
testobjekt = "test booking"
booking_dictionary[testobjekt] = booking(renter, date_from, date_to, car)
bookings_list.append(booking_dictionary)
#booking_dictionary.clear()
for k, v in cars.items():
    print(k, v)

print ("HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH")
print (bookings_list[0])
#for objx in bookings_list:
    #booking_information
# print(objx)
# print(renter)
def who_rents_what(renterp):
    print (renterp)

def booking_information():
    for obs in bookings_list:
        for k, v in obs.items():
            for o, e in v.items():
                if (o=='renter'):
                    print("Personen som leier heter følgende")
                    print (e.name)
                    who_rents_what(e)
                if (o=='car'):
                    print("Lisensnummeret er følgende")
                    print (e.make)
                    who_rents_what(e.license_plate)
                #print(o)
                #print(e)
            #print(v)
            #print(k=="test booking")
            #print(v == "car")
    return

booking_information()




print (eksempel)
#def print_booked_car():
#    return

#for k, v in bookings_list.items():
#   print(k, v)

#print(bookings[0])

#for x in bookings[0]:
    #for k, v in booking1.items():
       # print(k, v)

#for x in bookings:
    #print(x)

# booking1 = booking(renter, date_from, date_to, car)


# booking1 = create_booking_file.create_booking(renter, date_from, date_to, car)

# print(booking1.renter.name)



# print(vars(bil))

# for x in cars.values():
    # print(x)

# for key,values in cars.items():
    # for i in values:
    # print(key," : ",i)

# for x, y in cars.items():
    # print(x, y)

# for car in cars:
    # print(cars[car])
