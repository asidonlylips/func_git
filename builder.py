class Control:

    def __init__(self):
        self._builder = None

    def construct(self, builder):
        self.__builder = builder

    def getcar(self):
        car = Car()
        name = self.__builder.getname()
        car.set_name(name)
        wheel = self.__builder.getwheel()
        car.set_wheel(wheel)
        engine = self.__builder.getengine()
        car.set_engine(engine)
        transmission = self.__builder.gettransmission()
        car.set_transmission(transmission)
        return car


class Car:
    def __init__(self):
        self.__name = None
        self.__wheel = None
        self.__engine = None
        self.__transmission = None

    def set_name(self, name):
        self.__name = name

    def set_wheel(self, numbers):
        self.__wheel = numbers

    def set_engine(self, engine):
        self.__engine = engine

    def set_transmission(self, transmission):
        self.__transmission = transmission

    def carinfo(self):
        print('Vehicle name: {}'.format(self.__name))
        print('{} engine with {} horsepower'.format(self.__engine.type_engine, self.__engine.horsepower))
        print('Number of wheels: {}'.format(self.__wheel))
        print('Transmission type: {}'.format(self.__transmission))


class Builder:
    def getname(self): pass

    def getengine(self): pass

    def gettransmission(self): pass

    def getwheel(self): pass


class Name:
    name = None


class Wheel:
    number = None


class Engine:
    type_engine = None
    horsepower = None


class Transmission:
    transmission_type = None


class MuscleCar(Builder):
    def getname(self):
        name = Name()
        name = 'DIABLO'
        return name

    def getengine(self):
        engine = Engine()
        engine.type_engine = 'V8'
        engine.horsepower = 800
        return engine

    def getwheel(self):
        wheel = Wheel()
        wheel = 4
        return wheel

    def gettransmission(self):
        transmission = Transmission()
        transmission = 'auto'
        return transmission


class Motorcycle(Builder):
    def getname(self):
        name = Name()
        name = 'Hellish chariot'
        return name

    def getengine(self):
        engine = Engine()
        engine.type_engine = 'V4'
        engine.horsepower = 300
        return engine

    def getwheel(self):
        wheel = Wheel()
        wheel = 2
        return wheel

    def gettransmission(self):
        transmission = Transmission()
        transmission = 'manual'
        return transmission


def main():
    carbuilder = MuscleCar()
    control = Control()
    control.construct(carbuilder)
    my_car = control.getcar()
    my_car.carinfo()
    motobuilder = Motorcycle()
    control.construct(motobuilder)
    my_moto = control.getcar()
    my_moto.carinfo()


if __name__ == "__main__":
    main()
