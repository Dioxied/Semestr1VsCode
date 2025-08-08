from LogEl import *
print("При Q = 0")
print("A | B | Q")
print("--------------------")
for a in range(2):
    for b in range(2):
        u = TTriger()
        u.A, u.B, u.Q = a, b, 0
        print(f"{a} | {b} | {u.res}")
print()

print("При Q = 1")
print("A | B | Q")
print("--------------------")
for a in range(2):
    for b in range(2):
        u = TTriger()
        u.A, u.B, u.Q = a, b, 1
        print(f"{a} | {b} | {u.res}")