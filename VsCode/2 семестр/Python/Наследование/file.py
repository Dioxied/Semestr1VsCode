class TLogElement:
    def __init__(self):
        # Инициализация входных и выходных значений.
        # __in1 и __in2 - приватные переменные для хранения входных значений.
        # _res - защищенная переменная, хранящая результат вычислений.
        self.__in1 = 0
        self.__in2 = 0
        self._res = 0

    def __setIn1(self, newIn1):
        # Установка значения для In1 и вызов метода calc() для пересчета результата.
        self.__in1 = newIn1
        self.calc()

    def __setIn2(self, newIn2):
        # Установка значения для In2 и вызов метода calc() для пересчета результата.
        self.__in2 = newIn2
        self.calc()

    # Определение свойств для доступа к приватным переменным. 
    # Вместо прямого доступа к __in1 и __in2 используется свойство (property).
    In1 = property(lambda self: self.__in1, __setIn1)  # Свойство для In1
    In2 = property(lambda self: self.__in2, __setIn2)  # Свойство для In2
    Res = property(lambda self: self._res)  # Свойство для доступа к результату

    def calc(self):
        # Этот метод должен быть реализован в дочерних классах,
        # поскольку он не может быть определен в базовом классе TLogElement.
        raise NotImplementedError("Метод calc() должен быть реализован в дочернем классе.")

# Класс TNot - наследуется от TLogElement и реализует операцию логического отрицания.
class TNot(TLogElement):
    def __init__(self):
        TLogElement.__init__(self)

    def calc(self):
        """Логическое отрицание: результат есть 1 минус вход."""
        self._res = 1 - self.In1

class TAnd(TLogElement):
    def __init__(self):
        TLogElement.__init__(self)

    def calc(self):
        """Логическое "И": результат есть логическое "И" входов."""
        self._res = self.In1 and self.In2

class TOr(TLogElement):
    def __init__(self):
        TLogElement.__init__(self)

    def calc(self):
        """Логическое "ИЛИ": результат есть логическое "ИЛИ" входов."""
        self._res = self.In1 or self.In2

# Пример использования классов
n = TNot()  # Создание экземпляра класса TNot для логического отрицания
n.In1 = 0   # Установка входного значения In1 равным 0
print(n.Res)  # Вывод результата: 1 (логическое отрицание 0)

elNot = TNot()  # Создание еще одного экземпляра TNot
elAnd = TAnd()   # Создание экземпляра класса TAnd
elAnd.In1 = 0   # Установка входа In1 равным 0
elAnd.In2 = 1   # Установка входа In2 равным 1
elNot.In1 = elAnd.Res  # Установка входа In1 равным выходу elAnd
print(elNot.Res)  # Вывод результата: 1 (логическое отрицание результата 0 из elAnd)


# Как выделить классы в отдельный модуль?
# Создайте новый файл: Создайте файл с расширением .py, который будет вашим модулем. 
# Перенесите классы в новый файл: Скопируйте определения классов из вашего основного скрипта в новый файл.
# Импортируйте модуль в основной скрипт: Используйте команду import, чтобы загрузить ваш модуль в основной файл, где вы будете использовать классы.

# Пример

# logelement.py

class TLogElement:
    def __init__(self):
        self.__in1 = 0
        self.__in2 = 0
        self._res = 0

    def __setIn1(self, newIn1):
        self.__in1 = newIn1
        self.calc()

    def __setIn2(self, newIn2):
        self.__in2 = newIn2
        self.calc()

    In1 = property(lambda self: self.__in1, __setIn1)
    In2 = property(lambda self: self.__in2, __setIn2)
    Res = property(lambda self: self._res)

    def calc(self):
        raise NotImplementedError("Метод calc() должен быть реализован в дочернем классе.")

class TNot(TLogElement):
    def calc(self):
        self._res = 1 - self.In1

class TLog2In(TLogElement):
    def __init__(self):
        super().__init__()

class TAnd(TLog2In):
    def calc(self):
        self._res = self.In1 and self.In2

class TOr(TLog2In):
    def calc(self):
        self._res = self.In1 or self.In2

# Создайте или откройте файл main.py и импортируйте ваш модуль:

# main.py

# from logelement import TNot, TAnd, TOr  # Импортируем необходимые классы из модуля

# Пример использования классов
n = TNot()  # создание экземпляра класса TNot
n.In1 = 0   # установка входного значения In1
print(n.Res)  # вывод результата: 1 (логическое отрицание 0)

elNot = TNot()  # создание еще одного экземпляра TNot
elAnd = TAnd()   # создание экземпляра класса TAnd
elAnd.In1 = 0
elAnd.In2 = 1
elNot.In1 = elAnd.Res
print(elNot.Res)  # вывод результата: 1 (логическое отрицание результата 0 из elAnd)



# Сообщения между объектами

class TLogElement:
    def __init__(self):
        # Инициализация входных и выходных значений
        self.__in1 = 0      # Приватное входное значение 1
        self.__in2 = 0      # Приватное входное значение 2 (если нужно)
        self._res = 0       # Защищенное значение для хранения результата
        self.__nextEl = None  # Ссылка на следующий элемент цепочки
        self.__nextIn = 0   # Индекс, указывающий какой вход будет использован в следующем элементе

    def __setIn1(self, newIn1):
        self.__in1 = newIn1
        self.calc()  # Рассчет результата при установке нового входа
        self.sendSignal()  # Передача сигнала следующему элементу

    def __setIn2(self, newIn2):
        self.__in2 = newIn2
        self.calc()  # Рассчет результата при установке нового входа
        self.sendSignal()  # Передача сигнала следующему элементу

    # Свойства для управления доступом к входным данным
    In1 = property(lambda self: self.__in1, __setIn1)
    In2 = property(lambda self: self.__in2, __setIn2)
    Res = property(lambda self: self._res)

    def link(self, nextEl, nextIn):
        """Связка текущего элемента с следующим элементом.
            nextEl: Экземпляр следующего логического элемента.
            nextIn: Индекс входа следующего элемента (1 или 2).
        """
        self.__nextEl = nextEl
        self.__nextIn = nextIn

    def sendSignal(self):
        """Передача сигнала следующему элементу в цепочке."""
        if self.__nextEl is not None:
            # Отправка сигнала на следующий элемент вход по заданному индексу
            if self.__nextIn == 1:
                self.__nextEl.In1 = self.Res  # Передаем результат как In1 следующему элементу
            elif self.__nextIn == 2:
                self.__nextEl.In2 = self.Res  # Передаем результат как In2 следующему элементу

    def calc(self):
        """Метод должен быть переопределён в дочерних классах."""
        raise NotImplementedError("Метод calc() должен быть реализован в дочернем классе.")

class TNot(TLogElement):
    def __init__(self):
        TLogElement.__init__(self)

    def calc(self):
        """Логическое отрицание: результат есть 1 минус вход."""
        self._res = 1 - self.In1

class TAnd(TLogElement):
    def __init__(self):
        TLogElement.__init__(self)

    def calc(self):
        """Логическое "И": результат есть логическое "И" входов."""
        self._res = self.In1 and self.In2

class TOr(TLogElement):
    def __init__(self):
        TLogElement.__init__(self)

    def calc(self):
        """Логическое "ИЛИ": результат есть логическое "ИЛИ" входов."""
        self._res = self.In1 or self.In2


# Создаем элементы
not_gate = TNot()
and_gate = TAnd()
or_gate = TOr()

# Связываем элементы
not_gate.link(and_gate, 1)  # Связываем NOT с AND, передаем результат в In1
and_gate.link(or_gate, 1)    # Связываем AND с OR, передаем результат в In1

# Устанавливаем вход для NOT
not_gate.In1 = 0  # Установка входа в 0
print(f"NOT результат: {not_gate.Res}")  # Вывод результата NOT, ожидаем 1
print(f"AND результат (должен быть 0, так как вход для NOT = 0): {and_gate.Res}")  # Ожидаем 0 из AND

# Устанавливаем вход для AND
and_gate.In2 = 1  # Установка второго входа в 1
print(f"AND результат (должен быть 1 + 1): {and_gate.Res}")  # Второй вход активен, результат 0