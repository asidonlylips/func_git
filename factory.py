class Vehicle:
    def __init__(self):
        self.wheels = None
        self.engine = None
        self.transmission = None

    def vehicle_type(self, wheels):
        self.vehicle = Car()
        if wheels == 2:
            self.vehicle = Motorcycle()
        return self.vehicle

    def __str__(self):
        return ("It's vehicle with {} wheels, {} engine, {} transmission".format(self.wheels, self.engine, self.transmission))


class Car(Vehicle):
    def __init__(self):
        self.wheels = 4
        self.engine = 'V8'
        self.transmission = "auto"


class Motorcycle(Vehicle):
    def __init__(self):
        self.wheels = 2
        self.engine = 'V4'
        self.transmission = "manual"


if __name__ == "__main__":
    car = Vehicle().vehicle_type(4)
    motorcycle = Vehicle().vehicle_type(2)
    print(car)
    print(motorcycle)
