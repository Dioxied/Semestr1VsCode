print("_______________Задание A_______________")
class LampRow:
    def __init__(self):
        self.__state = "00000000"
    def show(self):
        for i in self.__state:
            if i == '0':
                print("-", end='')
            elif i == '1':
                print("*", end='')
        print()
    def __setState(self, new):
        if len(new) == 8:
            self.__state = new
        else:
            self.__state = "00000000"
    def __getState(self):
        return self.__state
    state = property(__getState, __setState)

lamps = LampRow()
lamps.show()
lamps.state = "10101010"
print(lamps.state)
lamps.show()

print("_______________Задание B_______________")
class LampRow:
    def __init__(self, count):
        self.__state = "0"*count
        self.count = count
    def show(self):
        for i in self.__state:
            if i == '0':
                print("-", end='')
            elif i == '1':
                print("*", end='')
        print()
    def __setState(self, new):
        if len(new) == self.count:
            self.__state = new
        else:
            self.__state = "0"*self.count
            print("Ошибка")
    def __getState(self):
        return self.__state
    state = property(__getState, __setState)

lamps = LampRow(6)
lamps.show()
lamps.state = "101010"
print(lamps.state)
lamps.show()
lamps.state = "10101010"
print(lamps.state)
lamps.show()

print("_______________Задание C_______________")
class LampRow:
    def __init__(self, count):
        self.__state = "0"*count
        self.count = count
    def show(self):
        for i in self.__state:
            if i == '0':
                print("-", end='')
            elif i == '1':
                print("*", end='')
            elif i == '2':
                print("o", end='')
        print()
    def __setState(self, new):
        if len(new) == self.count:
            self.__state = new
        else:
            self.__state = "0"*self.count
            print("Ошибка")
    def __getState(self):
        return self.__state
    state = property(__getState, __setState)

lamps = LampRow(6)
lamps.show()
lamps.state = "102102"
print(lamps.state)
lamps.show()
lamps.state = "10201010"
print(lamps.state)
lamps.show()

print("_______________Задание D______________")
class LampRow:
    def __init__(self, count):
        self.__state = int('1'+"0"*count)
        self.count = count
    def show(self):
        for i in str(self.__state)[1:]:
            if i == '0':
                print("-", end='')
            elif i == '1':
                print("*", end='')
            elif i == '2':
                print("o", end='')
        print()
    def __setState(self, new):
        if len(new) == self.count:
            self.__state = int('1'+new)
        else:
            self.__state = int('1'+"0"*self.count)
            print("Ошибка")
    def __getState(self):
        return str(self.__state)[1:]
    state = property(__getState, __setState)

lamps = LampRow(6)
lamps.show()
lamps.state = "102102"
print(lamps.state)
lamps.show()
lamps.state = "10101010"
print(lamps.state)
lamps.show()