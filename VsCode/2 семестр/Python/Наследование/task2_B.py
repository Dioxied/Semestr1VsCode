from LogEl import *

print("A | B | A nAnd B")
print("--------------------")
for a in range(2):
    for b in range(2):
        u = TNAnd()
        u.A, u.B = a, b
        print(f"{a} | {b} | {u.res}")
print()

print("A | B | A nOr B")
print("--------------------")
for a in range(2):
    for b in range(2):
        u = TNOr()
        u.A, u.B = a, b
        print(f"{a} | {b} | {u.res}")