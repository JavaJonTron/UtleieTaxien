class Car:
    def __init__(self, regnumber, fuel_source, model, make, year, km):
        self.regnumber = regnumber
        self.fuel_source = fuel_source
        self.model = model
        self.make = make
        self.km = km
        self.year = year

    def car_info(self):
        return "Car is a: " + self.make + " " + self.model + "\nModel Year: " + self.year + "\nFuel type: " + self.fuel_source + \
               "\nOdometer: " + self.km + "\nRegistration number: " + self.regnumber
