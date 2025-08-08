import string
import random

def indvKod():
    s=string.ascii_lowercase + string.digits + string.ascii_uppercase
    passw=''
    for i in range(5):
        passw += random.choice(s)
    return passw

print(indvKod())