from polymorphism.Car import Car


class SportsCar(Car):

    def __init__(self, spoiler_length, has_drilled_brakes, wheels, horsepower, brand):
        super().__init__(wheels, horsepower, brand)
        self.spoiler_length = spoiler_length
        self.has_drilled_brakes = has_drilled_brakes

