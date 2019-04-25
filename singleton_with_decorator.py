def singleton(cls):
    instances = {}

    def wrapper():
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]
    return wrapper

@singleton
class MyClass:
    def func(self):
        pass

a = MyClass() #<__main__.MyClass object at 0x03B10810>
b = MyClass()#<__main__.MyClass object at 0x03B10810>
