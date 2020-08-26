"""
Display bird and background.
"""
from turtle import *
from freegames import vector

cannon = Turtle(visible=False)
cannon.pu()
#cannon.screen.bgcolor("aqua")
bird_img = './images/bird.gif'
screen = Screen()
bg_img = './images/grassField.gif'
screen.bgpic(bg_img)
screen.register_shape(bird_img)
bird = Turtle()
bird.shape(bird_img)
bird.pu()
bird.hideturtle()
bird.goto(100,200)
bird.showturtle()

def draw()  :   
    cannon.pu()
    cannon.clear()
    cannon.goto(pos.x, pos.y)
    cannon.dot(20)

    if speed.y != 0:
        speed.y += 0.35
        pos.move(speed)
        if pos.y > 400:
            speed.y = 0
            pos.y = -300
        

    ontimer(draw, 20) 

def west():
    pos.x -= 30


def east():
    pos.x += 30

def fire():
    speed.y = 10


pos = vector(0,-300)
speed = vector(0, 0)
tracer(False)
onkey(west, 'Left')
onkey(east, 'Right')
onkey(fire, "space")
listen()

draw()

exitonclick()

