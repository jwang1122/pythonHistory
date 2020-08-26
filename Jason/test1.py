from turtle import *
pen1 = Turtle()
bodyx = -150
bodyy = 100
bodyr = 40

def drawCircle(pen1, x, y, r):
    pen1.up()
    pen1.goto(x,y)
    pen1.down()
    pen1.circle(r)

def drawRectangle(pen1, x, y, width, height):
    pen1.up()
    pen1.goto(x, y)
    pen1.down()
    pen1.fd(width)
    pen1.right(90)
    pen1.fd(height)
    pen1.right(90)
    pen1.fd(width)
    pen1.right(90)
    pen1.fd(height)

def drawLine(pen1, x,y,angle,length):
    pen1.up()
    pen1.goto(x,y)
    pen1.down()
    pen1.right(angle)
    pen1.fd(length)
    pen1.left(angle)

def drawTriangle(pen1, x, y,angle,side):
    pen1.up()
    pen1.goto(x,y)
    pen1.down()
    pen1.right(angle)
    pen1.fd(side)
    pen1.right(120)
    pen1.fd(side)
    pen1.right(120)
    pen1.fd(side)

if __name__ == '__main__':
    # Snow Boy Head
    pen1.color('black', 'white')
    pen1.begin_fill()
    drawCircle(pen1, bodyx, bodyy, bodyr)
    pen1.end_fill()

    eyeSize = 3
    eyey = 200
    # Snow Boy Eyes
    pen1.color('black', 'blue')
    pen1.begin_fill()
    drawCircle(pen1, -165, bodyy+50, eyeSize)
    pen1.end_fill()

    pen1.color('black', 'blue')
    pen1.begin_fill()
    drawCircle(pen1, -135, bodyy+50, eyeSize)
    pen1.end_fill()

    # Snow Boy Mouth
    pen1.end_fill()
    pen1.color('red')
    pen1.width(2)
    drawLine(pen1, -165, 120, 45, 14)
    drawLine(pen1, -150, 110, 0, 25)
    drawLine(pen1, -135, 110, -45, 14)
    
    pen1.color('white')
    drawLine(pen1, -235, 120, -45, 15)

    exitonclick()