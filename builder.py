class Vehicle:
    def __init__(self):
        self.wheel = None
        self.engine = None
        self.transmission = None
    
    def __str__(self):
        result = "Engine: {}, Number of wheels: {}, Transmission: {}".format(self.vehicle.engine, self.vehicle.wheel, self.vehicle. transmission)
        return result

class Vehiclebuilder(Vehicle):
    def __init__(self):
        self.vehicle = Vehicle()
    
    def add_wheels_car(self):
        self.vehicle.wheel = 4
        return self
    
    def add_wheels_motorcycle(self):
        self.vehicle.wheel = 2
        return self

    def add_engine_car(self):        
        self.vehicle.engine = "V8"
        return self

    def add_engine_motorcycle(self):
        self.vehicle.engine = "V4"
        return self
    
    def add_auto_transmission(self):
        self.vehicle.transmission = 'auto'
        return self

    def add_manual_transmission(self):
        self.vehicle.transmission = 'manual'
        return self
    
    def build(self):
        return self.vehicle


if __name__ == "__main__":
    my_car = Vehiclebuilder()
    my_car.add_auto_transmission()
    my_car.add_engine_car()
    my_car.add_wheels_car()
    my_car.build()
    print(my_car)
    my_motorcycle = Vehiclebuilder()
    my_motorcycle.add_manual_transmission()
    my_motorcycle.add_engine_motorcycle()
    my_motorcycle.add_wheels_motorcycle()
    my_motorcycle.build()
    print(my_motorcycle)
    