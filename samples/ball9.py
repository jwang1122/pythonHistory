"""
Fire the ball hit the bird, make the bird back to start position.
"""
from turtle import *
from freegames import vector 
from random import *

cannon = Turtle(visible=False)
cannon.pu()
cannon.screen.bgcolor("lightblue")
screen = Screen()
bg_img = r'grassField.gif'
screen.bgpic(bg_img)
bird_img = 'bird.gif'
screen.addshape(bird_img)

bird = Turtle()
bird.shape(bird_img)
bird.pu()
birdstartx = 400
birdstarty = 200
birdpos = vector(birdstartx,birdstarty)
bird.hideturtle()
bird.goto(birdpos.x,birdpos.y)
bird.showturtle()


def draw():
    cannon.pu()
    cannon.clear()
    cannon.goto(pos.x, pos.y)
    cannon.dot(20)

    birdpos.x -= 0.5
    bird.clear()
    bird.goto(birdpos.x, birdstarty)
    if(birdpos.x<-200):
        birdpos.x = birdstarty
    if abs(birdpos-pos) < 15:
        birdpos.x = birdstartx

    if speed.y != 0:
        speed.y += 0.35
        pos.move(speed)
        if pos.y > 400:
            speed.y = 0
            pos.y = -300
        
    ontimer(draw, 30) 

def west():
    pos.x -= 30


def east():
    pos.x += 30

def fire():
    speed.y = 10

pos = vector(0,-300)
speed = vector(0, 0)
tracer(80, 50)
onkey(west, 'Left')
onkey(east, 'Right')
onkey(fire, "space")

listen()
draw()

exitonclick()
