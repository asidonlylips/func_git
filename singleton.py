class Singleton:  
    def __new__(cls):
        if not hasattr(cls, 'instance'):
           cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance     


sing=Singleton() #<__main__.Singleton object at 0x03D3D810>
sing1=Singleton() #<__main__.Singleton object at 0x03D3D810>
