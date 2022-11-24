class Car:
    def __init__(self, make, model, year, license_plate, fuel_source, km, is_take, hourly_rate, daily_rate, owner, earned_total):
        self.make = make
        self.model = model
        self.year = year
        self.license_plate = license_plate
        self.fuel_source = fuel_source
        self.km = km
        self.is_take = is_take
        self.hourly_rate = hourly_rate
        self.daily_rate = daily_rate
        self.owner = owner
        self.earned_total = earned_total

    def price_calculation(self, rate):
        taxes = 0.25
        rate = rate - (rate * taxes)
        easy_car = 0.2
        rate = rate-(rate * easy_car)
        self.earned_total += rate
        return rate

    def nickname(self):
        return str(self.year) + " " + str(self.make) + " " + str(self.model)

    def __str__(self):
        return str(self.make) + str(self.model) + str(self.year) + str(self.license_plate) + str(self.fuel_source) + \
               str(self.km) + str(self.is_take) + str(self.hourly_rate) + str(self.daily_rate) + str(self.owner)
