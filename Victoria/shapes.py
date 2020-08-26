from turtle import *

def drawCircle(pen1, x, y, r):
    """
    draw a circle with radius r and position (x, y)

    pen1: Turtle()
    x: horisontal position on screen
    y: vertical position on screen
    r: radius of the circle
    """
    pen1.up()
    pen1.goto(x,y)
    pen1.down()
    pen1.circle(r)

def drawRectangle(pen1, x, y, width, height):
    """
    draw a circle with radius r and position (x, y)
    """
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
    pen1 = Turtle()
    drawCircle(pen1,100,100, 50)
    drawRectangle(pen1,0,0,200,100)
    drawLine(pen1,-100, 100, 45, 100)
    drawTriangle(pen1, -100,-100,-45, 50)
    exitonclick()
