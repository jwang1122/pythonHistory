"""
Fire the ball hit the bird, drop the hitted bird down to the ground.
"""
from turtle import *
from freegames import vector 
from random import *
 
cannon = Turtle(visible=False)
cannon.pu()
cannon.screen.bgcolor("lightblue")
screen = Screen()
bg_img = './images/grassField.gif'
screen.bgpic(bg_img)
bird_img = './images/bird.gif'
bird_dead = "./images/upsidedownbird.gif"
screen.addshape(bird_img)
screen.addshape(bird_dead)

bird = Turtle()
bird.shape(bird_img)
bird.pu()
birdstartx = 300
birdstarty = 200
birdpos = vector(birdstartx,birdstarty)
bird.hideturtle()
bird.goto(birdpos.x,birdpos.y)
bird.showturtle()
birdspeed = vector(0,0)
birdhitted = False

def draw():
    global birdhitted
    cannon.pu()
    cannon.clear()
    cannon.goto(pos.x, pos.y)
    cannon.dot(20)
    if speed.y != 0:
        speed.y += 0.35
        pos.move(speed)
        if pos.y > 400:
            speed.y = 0
            pos.y = -200

    bird.clear()
    if birdhitted is False : 
        birdpos.x -= 0.5
        bird.goto(birdpos.x, birdstarty)
    if(birdpos.x<-200):
        birdpos.x = birdstartx
    if abs(birdpos-pos) < 15:
        birdhitted = True
    if birdhitted is True:
        bird.shape(bird_dead)
        birdspeed.y -= 0.35
        birdpos.move(birdspeed)
        bird.goto(birdpos.x, birdpos.y)
        if(birdpos.y < -250):
            birdpos.x = birdstartx
            birdpos.y = birdstarty
            birdhitted = False
            bird.shape(bird_img)

        
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
