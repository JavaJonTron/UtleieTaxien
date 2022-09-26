class Owner:
    # I min mening, begrenset hva leietaker trenger å vite om utleier bortsett fra generisk info
    def __init__(self, age, name, cars):
        self.age = age
        self.name = name
        self.cars = cars
