from turtle import *

t1 = Turtle(visible=False)

def draw():
    t1.pu()
    tracer(False)
    t1.setpos(0, -180)
    t1.dot(20)

draw()
mainloop()

