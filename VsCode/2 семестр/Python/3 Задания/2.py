# A
print("TASK1")

# Класс, представляющий ряд из 8 ламп
class LampRow:
    def __init__(self):
        # Инициализация состояния ламп (все выключены)
        self.__state = "00000000"

    # Метод для получения состояния ламп
    def __getState(self):
        return self.__state

    # Метод для установки состояния ламп
    def __setState(self, nu):
        # Проверка, что длина строки состояния равна 8
        if len(nu) == 8:
            self.__state = nu
        else:
            # Если длина неправильная, сбрасываем состояние на "00000000"
            nu = '00000000'

    # Свойство для доступа к состоянию
    state = property(__getState, __setState)

    # Метод для отображения состояния ламп
    def show(self):
        for i in self.__state:
            if i == "0":
                print("-", end="")  # Выключенная лампа
            else:
                print("*", end="")  # Включенная лампа
        print()

# Создаем объект класса LampRow и отображаем его состояние
lamps = LampRow()
lamps.show()  # Печатает: --------
lamps.state = "10101010"  # Устанавливаем новое состояние
print(lamps.state)  # Печатает: 10101010
lamps.show()  # Печатает: *-*-*-*-

# B
print("TASK2")

# Класс, представляющий ряд ламп произвольной длины
class LampRow2:
    def __init__(self, num = 0):
        self.__num = num  # Количество ламп
        self.__state = ""  # Инициализация состояния
        for i in range(num):
            self.__state += "0"  # Все лампы изначально выключены

    # Метод для получения состояния
    def __getState2(self):
        return self.__state

    # Метод для установки состояния
    def __setState2(self, nu):
        # Проверка, что длина строки состояния совпадает с количеством ламп
        if len(nu) == self.__num:
            self.__state = nu
        else:
            print("Ошибка")  # Сообщение об ошибке
            self.__state = ""  # Сбрасываем состояние
            for i in range(self.__num):
                self.__state += "0"  # Заполняем нулями

    # Свойство для доступа к состоянию
    state2 = property(__getState2, __setState2)

    # Метод для отображения состояния
    def show2(self):
        for i in self.__state:
            if i == "0":
                print("-", end="")  # Выключенная лампа
            else:
                print("*", end="")  # Включенная лампа
        print()

# Создаем объект класса LampRow2 с 6 лампами и отображаем его состояние
lamps2 = LampRow2(6)
lamps2.show2()  # Печатает: ------
lamps2.state2 = "101010"  # Устанавливаем новое состояние
print(lamps2.state2)  # Печатает: 101010
lamps2.show2()  # Печатает: *-*-*-
lamps2.state2 = "10101010101"  # Устанавливаем некорректное состояние
print(lamps2.state2)  # Печатает: (ошибка, состояние сбрасывается)
lamps2.show2()  # Печатает: ------

# C
print("TASK3")

# Класс, представляющий ряд ламп с проверкой на корректные символы
class LampRow3:
    def __init__(self, num = 0):
        self.__num = num  # Количество ламп
        self.__state = ""  # Инициализация состояния
        for i in range(num):
            self.__state += "0"  # Все лампы изначально выключены

    # Метод для получения состояния
    def __getState3(self):
        return self.__state

    # Метод для установки состояния
    def __setState3(self, nu):
        # Проверка, что длина строки состояния совпадает с количеством ламп
        if len(nu) == self.__num:
            self.__state = nu
        else:
            print("Ошибка")  # Сообщение об ошибке
            self.__state = ""  # Сбрасываем состояние
            for i in range(self.__num):
