from LogEl import *

print("A | B | A xOr B")
print("--------------------")
for a in range(2):
    for b in range(2):
        u = TXOr()
        u.A, u.B = a, b
        print(f"{a} | {b} | {u.res}")
print()

print("A | B | A -> B")
print("--------------------")
for a in range(2):
    for b in range(2):
        u = Tlmp()
        u.A, u.B = a, b
        print(f"{a} | {b} | {u.res}")