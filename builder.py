class Control:

    def __init__(self):
        self._builder = None
    
    def construct(self, builder):
        self.__builder = builder

    def getcar(self):
        car = Car()
        wheel = self.__builder.getwheel()
        car.set_wheel(wheel)
        engine = self.__builder.getengine()
        car.set_engine(engine)
        transmission = self.__builder.gettransmission()
        car.set_transmission(transmission)
        return car
    
    def carinfo(self):
        print "engine: %s" % self.__engine
        print "wheel: %s" % self.__wheel
        print "transmission: %s" % self.__transmission


class Car:
    def __init__(self):
        self.__wheel = None
        self.__engine = None
        self.__transmission = None

    def set_wheel(self, numbers):
        self.__wheel = numbers
    
    def set_engine(self, engine):
        self.__engine = engine
    
    def set_transmission(self, transmission):
        self.__transmission = transmission
    
class Builder:
    def getengine(self): pass
    def gettransmission(self): pass
    def getwheel(self): pass


class Wheel:
    number = None

class Engine:
    type_engine = None

class Transmission:
    transmission_type = None
    
    

if __name__ == "__main__":
    build = Builder()
    control = Control()
    



