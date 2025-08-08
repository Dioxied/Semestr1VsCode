class Pet:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    name = property(lambda self: self.__name)
    age = property(lambda self: self.__age)

    def gettingOlder(self):
        self.__age += 1

    def say(self):
        raise NotImplementedError("Метод say() должен быть реализован в дочернем классе.")

class Mammal(Pet):
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        Pet.__init__(self, self.__name, self.__age)
    def run(self):
        print(f"{self.__name} побежал...")
    
class Reptilia(Pet):
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        Pet.__init__(self, self.__name, self.__age)
    def crawl(self):
        print(f"{self.__name} пополз...")


class Cat(Mammal):
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        Mammal.__init__(self, self.__name, self.__age)

    def say(self):
        print(f"{self.__name}: Мяу!")
    
class Dog(Mammal):
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        Mammal.__init__(self, self.__name, self.__age)

    def say(self):
        print(f"{self.__name}: Гав!")

class Turtle(Reptilia):
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        Reptilia.__init__(self, self.__name, self.__age)
    def say(self):
        print(f"{self.__name}: ...")
    
class Snake(Reptilia):
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        Reptilia.__init__(self, self.__name, self.__age)
    def say(self):
        print(f"{self.__name}: ш-ш-ш-ш...")