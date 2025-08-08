from LogEl import *

print("A | B | not(A+B)")
print("--------------------")
for a in range(2):
    for b in range(2):
        u = TOr()
        u.A = a
        u.B = b
        u2 = TNot()
        u2.A = u.res
        print(f"{a} | {b} | {u2.res}")

