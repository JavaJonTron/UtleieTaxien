from classes.car import Car

cars = {}


def opprette_bil():
    make = input("Bil fabrikant: ")
    model = input("Modell: ")
    year = input("Års modell: ")
    regn = input("Registrerings nummer: ")
    drivstoff = input("Drivstoff type: ")
    km = input("Kilometerstand: ")
    bil_Objekt = Car(regn, drivstoff, model, make, km, year)
    kallenavn = year + " " + make + " " + model
    cars[kallenavn] = [bil_Objekt]


opprette_bil()
#opprette_bil()
#opprette_bil()

for car in cars:
    print(car.car_info(car))
