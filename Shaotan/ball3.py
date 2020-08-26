from turtle import *

t1 = Turtle(visible=False)

def draw():
    t1.pu()
    tracer(False)
    t1.setpos(0, -180)
    t1.dot(20)

draw()
mainloop()
from turtle import *
from freegames import vector

t1 = Turtle(visible=False)
t1.pu()

def draw():
    t1.clear()
    t1.goto(pos.x, pos.y)
    t1.dot(20)

    ontimer(draw, 20)

def west():
    pos.x -= 30


def east():
    pos.x += 30

pos = vector(0,-200)
tracer(False)
onkey(west, 'Left')
onkey(east, 'Right')
listen()

draw()

exitonclick()

