class Car:
    def __init__(self, wheels, horsepower, brand):
        self.wheels = wheels
        self.horsepower = horsepower
        self.brand = brand

    def info(self):
        print("I have " + self.wheels + " wheels, " + self.horsepower + " horsepower and " + self.brand + " brand")
