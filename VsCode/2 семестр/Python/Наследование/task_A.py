from animals import *

p = Dog("Шарик", 5)
p.gettingOlder()
print(p.name + ":", p.age, "Лет")
pets = [Cat("Мурка", 3), p]
for p in pets:
    p.say()