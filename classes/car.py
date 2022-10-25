class Car:
    def __init__(self, make, model, year, license_plate, fuel_source, km, is_taken):
        self.make = make
        self.model = model
        self.year = year
        self.license_plate = license_plate
        self.fuel_source = fuel_source
        self.km = km
        self.is_taken = is_taken

    def __str__(self):
        return str(self.make) + str(self.model) + str(self.year) + str(self.license_plate) + str(self.fuel_source) + str(self.km) + str(self.is_taken)
