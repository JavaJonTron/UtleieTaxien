class Car:
    def __init__(self, make, model, year, license_plate, fuel_source, km):
        self.make = make
        self.model = model
        self.year = year
        self.license_plate = license_plate
        self.fuel_source = fuel_source
        self.km = km

    def __str__(self):
        return self.make + self.model + str(self.year) + self.license_plate + self.fuel_source + str(self.km)
