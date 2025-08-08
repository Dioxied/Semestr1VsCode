from turtle import *
color('black')
left(90)
forward(100)
left(180)
forward(200)
left(180)
forward(100)
left(90)
forward(100)
left(180)
forward(200)
left(180)
forward(100)
x=-10
while x != 10:
    goto(x,2-x**2)
    x=x+0.1
done()