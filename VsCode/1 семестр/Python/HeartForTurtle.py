from threading import Thread
import turtle
import math



def heart():
    t = turtle.Turtle()
    # t.screen.setup(300, 300)
    t.speed(1000)
    t.color('red')

    def corazon(n):
        x = 16 * math.sin(n) ** 3
        y = 13 * math.cos(n) - 5 * \
            math.cos(2*n) - 2*math.cos(3*n) - \
            math.cos(4*n)
        return x, y

    t.penup()
    for i in range(5):
        t.goto(0, 0)
        t.pendown()
        for n in range(0, 100, 2):
            x, y = corazon(n/10)
            t.goto(x*i, y*i)
        t.penup()
    t.hideturtle()
    turtle.done()





if __name__ == '__main__':
    for i in range(3):
        Thread(target = heart).start()
    