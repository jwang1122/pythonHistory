# 6/1/2020-6/26/2020 homework and class notes 
Austin Python level 1 11:30 class

>Teacher emails: 
>wangqianjiang@gmail.com 

>send hw here: wangqianjiang@live.com

>Teacher phone number: 2818182512


>github link: https://github.com/jwang1122/python1-1130

## setting up
install python:
>Google Search: python download
>Use this result: Download Python | Python.org

>[Website](https://www.python.org/downloads/)

we used command prompt to set up python

cd = change directory
```sh
cd workspace
cd python
```
To check for version of aplication type the application and --version

EX:
```sh 
git --version
```
with this the computer will tell you the current version of github, or whatever you type, on your computer.

Install gihub:
>Google Search: github download
>Use this result: Git - Downloads - Git SCM

>[Website](https://git-scm.com/downloads)

setting up workspace

make the folders you dont have. you should have users and your computer name

go to users, then (your computer name) > workspace > python


## code things
to run pandas i have to use .\env\scripts\python

in python, ' and " are the same thing

we opened .env folder with python -m -venv env

Tuple: parentheses () including info seperated by commas. The information cannot be changed but can we overrided.

Ex:
```
(1,2,3,4,5,6,7,8,9)
```
```
(1,2,'hello',(5,6,7),3+2j)
```
```
t3 = t1 + t2
```
```
t1 = t1 + (9,)
```
List: a tuple but the info surrounded by square brackets []. It can also include other types of data like tuples or lists or etc. You can also change the list's value, unlike a tuple.

Set: a tuple but info is surrounded by curved brakets {}. Can add info to set, cannot add duplicate elements in set.

Dictionary: you set things to a 'definition'. You can also add new values to a dictionary through Ex: d1["k2"] = 2 You can also delete things through Ex: del d1["k2"]

Ex:
```
d = {"k1":"v1", "k2":4}
```

help(function) will give you help.

Ex:
```py
help(print)
```

type() will tell you the class of whatever is in the ()

if all your code is right but it says there are problems, then the editor has a setup issue.

In python numbers are automaticly set to integers.

In python you can out set mutiple pieces of information on one line seperated by commas:
```py
a,b, = 1,5
a,b,c,d, = 1,3,5,2
```
to put a website in markdown do this:

[description](website address)

Ex:
```md
[Website](https://git-scm.com/downloads)
```
Result:
[Website](https://git-scm.com/downloads)

to embed a picture in mark down do this:

![Description](image address)

Ex:
```md
![apple](https://th.bing.com/th/id/OIP.A1JjNu8jIRxaTJHbD_EtFwHaIJ?pid=Api&rs=1)
```
result:
 ![apple](https://th.bing.com/th/id/OIP.A1JjNu8jIRxaTJHbD_EtFwHaIJ?pid=Api&rs=1)

In python, you can use the terminal to test your code instead of running the enire thing.

In python, you comment things out with hashtags
```py
#this is a comment
```

>How to install freegames type this into terminal:
.\env\scripts\pip install freegames

### print
```py
print("hello, world!")
print("2","3","4")
```
more complex:
```py
print("4","3","2",end=' ', sep="; ")
```
here the it will print 4; 3; 2; because of sep=";". It will also put a space after the line it printed.

you can also set the things you print to letters:
```py
a = "joe"
b = "ham"
print(a,b)
```
when you run this script it will print joe ham. The above end=" " and sep="; " will also work with this.

You can also edit your printing:
```py
s = "this is a Test."
print("02:", s.capitalize())
print("03:", s.title())
print("04:", s.upper())
print("04:", s.lower())
print(s.center(80))
```
In the code above, ``` s.capitalize ``` is capitalize the first letter in the printing.

In the code above, ``` s.title ``` is capitalize the first letter of every word in the printing.

```s.upper``` will capitalize everything

```s.lower``` will make everything lowercase



### math

You can do math with python:

multiplication: * |
division: / |
addition: + |
subtraction: - |
```py
a = 2020
b = 20
print("%d-%d=%d" % (a, b, a-b))
```
you can also use functions to let the computer for you:
```py
from math import pi

def add(x,y):
    return x + y

def sub(a,b):
    return a + b

def mul(c,d):
    return c * d

def circlearea(r):
    return r * r * pi

print(__name__)
if __name__ == "__main__":
    print(add(10,20))
    print(sub(20,5))
    print(add(451,1435.34))
    print(sub(1323,234))
    print(mul(7,7))
    print(circlearea(9))
```
These lines of code defines what to do for adding subtracting and dividing:
```py
from math import pi

def add(x,y):
    return x + y

def sub(a,b):
    return a + b

def mul(c,d):
    return c * d

def circlearea(r):
    return r * r * pi
```
And here is the sample code to test out the code:
```py
print(__name__)
if __name__ == "__main__":
    print(add(10,20))
    print(sub(20,5))
    print(add(451,1435.34))
    print(sub(1323,234))
    print(mul(7,7))
    print(circlearea(9))
```
For example, in the first print add means add the numbers 10 and 20.
 
### turtle, drawing, and ball

basics of drawing

ball1
```py
from turtle import *

t1 = Turtle()
t1.dot(20)
mainloop()
```
pythonhas a thing called turtle built in to draw stuff.

Here we import turtle o python can draw stuff. t1 = Turtle() set the thing python is going to draw to t1. It can be set to anything except turtle or python will be confused. t1.dot(20) makes the dot's radius 20. mainloop() keeps a window open to show you the drawing. you will see a black triangle. That is the thing that draws whatever you input into python.

add stuff

ball2
```py
from turtle import *

t1 = Turtle()
t1.dot(20,'red')
t1.hideturtle()
mainloop()
```
here we have made the dot red. t1.dot(20,'red') Also we hid the black triangle so u cant see it anymore. :) t1.hideturtle()

now we add more

ball3
```py
from turtle import *

t1 = Turtle(visible=False)

def draw():
    t1.pu()
    tracer(False)
    t1.setpos(0, -180)
    t1.dot(20)

draw()
mainloop()
```
here we used another way to hide the turtle: t1 = Turtle(visible=False) draw() will tell python to run everything in def draw() As you can see there are lines of code that are indented by pressing the tab button. The indention is how python knows that is what to do when def draw(): is run. This code will tell python to draw the circle at (0,-180) instead of at (0,0)  t1.setpos(0, -180)

now this one is much more complex:

ball4
```py
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
```
Basically we just put pen up so it doesnt draw we we move the dot with left and right arrow keys with this:
```py
def west():
    pos.x -= 30


def east():
    pos.x += 30
```
these lines of code will tell python to execute the code above then right and left arrow key is pressed:
```py
onkey(west, 'Left')
onkey(east, 'Right')
```
we also made the ball move when fired

now lets Move the ball gradually on fire and addd some customization

ball5
```py
from turtle import *
from freegames import vector

t1 = Turtle(visible=False)
t1.penup()


def draw():
    t1.pu()
    t1.clear()
    t1.goto(pos.x, pos.y)
    t1.dot(20)

    if speed.y != 0:
        speed.y += 0.35
        pos.move(speed)

    ontimer(draw, 20) 

def west():
    pos.x -= 30


def east():
    pos.x += 30

def fire():
    speed.y = 25

pos = vector(0,-200)
speed = vector(0, 0)
tracer(False)
onkey(west, 'Left')
onkey(east, 'Right')
onkey(fire, "space")
listen()

draw()

exitonclick()
```
here is what we did to move the ball gradually on fire
```py
    if speed.y != 0:
        speed.y += 0.35
        pos.move(speed)
```
and we have a timer
```py
ontimer(draw, 20)
```
now lets make it so when the ball is out of the screen, python will put the ball back.

ball6
```py
from turtle import *
from freegames import vector

cannon = Turtle(visible=False)
cannon.pu()
cannon.screen.bgcolor("aqua")

def draw():
    cannon.pu()
    cannon.clear()
    cannon.goto(pos.x, pos.y)
    cannon.dot(20,'red')

    if speed.y != 0:
        speed.y += 0.35
        pos.move(speed)
        if pos.y > 300:
            speed.y = 0
            pos.y = -200
        

    ontimer(draw, 20) 

def west():
    pos.x -= 30


def east():
    pos.x += 30

def fire():
    speed.y = 10

pos = vector(0,-200)
speed = vector(0, 0)
tracer(False)
onkey(west, 'Left')
onkey(east, 'Right')
onkey(fire, "space")
listen()

draw()

exitonclick()
```
now after firing python will exevute this script:
```py
pos = vector(0,-200)
```
now draw() has been changed:
```py
def draw():
    cannon.pu()
    cannon.clear()
    cannon.goto(pos.x, pos.y)
    cannon.dot(20,'red')
```
as you can see, t1 is now named cannon and it's color has been change to red.

the background color has changed too:
```py
cannon = Turtle(visible=False)
cannon.pu()
cannon.screen.bgcolor("aqua")
```
we used cannon.screen.bgcolor("aqua") to change the bg color to aqua.

now we are going to add a new background and a bird to shoot at:

ball7
```py
from turtle import *
from freegames import vector

cannon = Turtle(visible=False)
cannon.pu()
cannon.screen.bgcolor("aqua")
bird_img = 'bird.gif'
screen = Screen()
bg_img = r'grassField.gif'
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
            pos.y = -200
        

    ontimer(draw, 20) 

def west():
    pos.x -= 30


def east():
    pos.x += 30

def fire():
    speed.y = 10


pos = vector(0,-200)
speed = vector(0, 0)
tracer(False)
onkey(west, 'Left')
onkey(east, 'Right')
onkey(fire, "space")
listen()

draw()

exitonclick()
```
using this code we used python's turtle to put a grassy plain and a bird in the game. All we had to do was download the pics and put it in the code:
```py
bird_img = 'bird.gif'
screen = Screen()
bg_img = r'grassField.gif'
screen.bgpic(bg_img)
screen.register_shape(bird_img)
bird = Turtle()
bird.shape(bird_img)
bird.pu()
bird.hideturtle()
bird.goto(100,200)
bird.showturtle()
```

Now we will learn to move the bird across the screen

ball8
```py
from turtle import *
from freegames import vector
from random import *

cannon = Turtle(visible=False)
cannon.pu()
#cannon.screen.bgcolor("aqua")
screen = Screen()
bg_img = r'grassField.gif'
screen.bgpic(bg_img)
bird_img = 'bird.gif'
screen.addshape(bird_img)

bird = Turtle()
bird.shape(bird_img)
bird.pu()
birdpos = vector(200,200)
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
    bird.goto(birdpos.x, 200)
    if(birdpos.x<-200):
        birdpos.x = 200

    if speed.y != 0:
        speed.y += 0.35
        pos.move(speed)
        if pos.y > 400:
            speed.y = 0
            pos.y = -200

    ontimer(draw, 30) 

def west():
    pos.x -= 30


def east():
    pos.x += 30

def fire():
    speed.y = 10

pos = vector(0,-200)
speed = vector(0, 0)
tracer(80, 50)
onkey(west, 'Left')
onkey(east, 'Right')
onkey(fire, "space")

listen()
draw()

exitonclick()
```
we used this script to move the bird from right to left and increase the bird's speed across the screen every milisecond. It also put the bird back after it goes to -200 x
```py
def draw():
    cannon.pu()
    cannon.clear()
    cannon.goto(pos.x, pos.y)
    cannon.dot(20)

    birdpos.x -= 0.5
    bird.clear()
    bird.goto(birdpos.x, 200)
    if(birdpos.x<-200):
        birdpos.x = 200

    if speed.y != 0:
        speed.y += 0.35
        pos.move(speed)
        if pos.y > 400:
            speed.y = 0
            pos.y = -200

    ontimer(draw, 30) 
```
now we will make the bird move back the the beginning when it is hit

ball9
```py
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
            pos.y = -200

    ontimer(draw, 30) 

def west():
    pos.x -= 30


def east():
    pos.x += 30

def fire():
    speed.y = 10

pos = vector(0,-200)
speed = vector(0, 0)
tracer(80, 50)
onkey(west, 'Left')
onkey(east, 'Right')
onkey(fire, "space")

listen()
draw()

exitonclick()
```
### loops

we started with this code that used a for loop to print a right triangle using numbers:
```py
"""
print a right triangle
1 
2 2 
3 3 3 
4 4 4 4 
"""
for i in range(1, 5):
    for j in range(i):
        print(i, end=' ')
    print()
```
After that the teacher told us to do something more complex
```py
"""
make this
    1 
   2 2
  3 3 3
 4 4 4 4 
"""
for i in range(1, 5):
    for k in range(5,i,-1):
        print(" ", end='')
    for j in range(i):
        print(i, end=' ')
    print()
```
we added for k in range(5,i,-1): to print spaces 5 times, then 4, 3, etc. before the numbers in order to shape the text into a equalateral triangle.
