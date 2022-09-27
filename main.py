from classes.car import Car

cars = {}
make=""
model=""
year = 0
regn = ""
fuel_source = ""
km = 0

def opprette_bil():
    make = input("Bil fabrikant: ")
    model = input("Modell: ")
    year = input("Års modell: ")
    regn = input("Registrerings nummer: ")
    fuel_source = input("Drivstoff type: ")
    km = input("Kilometerstand: ")


bil_Objekt = Car(regn, fuel_source, model, make, km, year)
kallenavn = "TEST"+make
cars[kallenavn] = [bil_Objekt]

opprette_bil()
#opprette_bil()
#opprette_bil()

print("REGGGGG"+bil_Objekt.regn)

for x in cars.values():
    print(x)


#for key,values in cars.items():
  #   for i in values:
        #  print(key," : ",i)

#for x, y in cars.items():
  #print(x, y)

#for car in cars:
  #  print(cars[car])
