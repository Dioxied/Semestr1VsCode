class T:
    def __init__(self):
        self.__A = 0
        self.__B = 0
        self.__Q = 0
        self._res = 0

    def setA(self, new):
        self.__A = new
        self.calc()
    def setB(self, new):
        self.__B = new
        self.calc()
    def setQ(self, new):
        self.__Q = new
        self.calc()

    A = property(lambda self: self.__A, setA)
    B = property(lambda self: self.__B, setB)
    Q = property(lambda self: self.__Q, setQ)
    res = property(lambda self: self._res)

    def calc(self):
        raise NotImplementedError("Метод calc() должен быть реализован в дочернем классе.")
    
class TOr(T):
    def __init__(self):
        T.__init__(self)
    def calc(self):
        self._res = self.A or self.B

class TNot(T):
    def __init__(self):
        T.__init__(self)
    def calc(self):
        self._res = 1 - self.A

class TNAnd(T):
    def __init__(self):
        T.__init__(self)
    def calc(self):
        self._res = 1 - (self.A and self.B)

class TNOr(T):
    def __init__(self):
        T.__init__(self)
    def calc(self):
        self._res = 1 - (self.A or self.B)

class TXOr(T):
    def __init__(self):
        T.__init__(self)
    def calc(self):
        self._res = 0 if self.A == self.B else 1

class Tlmp(T):
    def __init__(self):
        T.__init__(self)
    def calc(self):
        self._res = 1 if self.A <= self.B else 0

class TTriger(T):
    def __init__(self):
        T.__init__(self)
    def calc(self):
        self._res = 0