from turtle import *

def drawCircle(pen1, x, y, r):
    """
    draw a circle with radius r and position (x, y)
    pen1: Turtle()
    x: horisontal pos on screen
    y: vertical pos on screen
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
    pen1.width(1)
    pen1.color('black','white')
    pen1.begin_fill()
    drawCircle(pen1,-150,53,40)
    pen1.end_fill()

    pen1.color('black','white')
    pen1.begin_fill()
    drawCircle(pen1,-150,-55,55)
    pen1.end_fill()

    pen1.color('black','white')
    pen1.begin_fill()
    drawCircle(pen1,-150,-190,68)
    pen1.end_fill()


    pen1.color('black','white')
    pen1.begin_fill()
    drawCircle(pen1,150,53,40)
    pen1.end_fill()

    pen1.color('black','white')
    pen1.begin_fill()
    drawCircle(pen1,150,-55,55)
    pen1.end_fill()

    pen1.color('black','white')
    pen1.begin_fill()
    drawCircle(pen1,150,-190,68)
    pen1.end_fill()


    pen1.color('black','black')
    pen1.begin_fill()
    drawRectangle(pen1,-168,195,40,60)
    pen1.end_fill()
    pen1.width(5)
    drawLine(pen1,-188,135,90,80)
    pen1.width(1)

    pen1.color('black','blue')
    pen1.begin_fill()
    drawCircle(pen1,-160,100,5)
    pen1.end_fill()

    pen1.color('black','blue')
    pen1.begin_fill()
    drawCircle(pen1,-130,100,5)
    pen1.end_fill()

    pen1.width(2)
    pen1.color('red','red')    
    drawLine(pen1,-170,80,135,10)

    pen1.color('red','red')    
    drawLine(pen1,-163,72,90,25)

    pen1.color('red','red')    
    drawLine(pen1,-137,72,45,10)

    pen1.width(1)
    pen1.color('black','gray')
    pen1.begin_fill()
    drawCircle(pen1,-143,28,7)
    pen1.end_fill()

    pen1.begin_fill()
    drawCircle(pen1,-143,-18,7)
    pen1.end_fill()

    pen1.begin_fill()
    drawCircle(pen1,-143,-88,7)
    pen1.end_fill()  


    pen1.begin_fill()
    drawCircle(pen1,-143,-148,7)
    pen1.end_fill()   
   
    pen1.color('black','yellow')
    pen1.begin_fill()
    drawCircle(pen1,158,28,7)
    pen1.end_fill()
   
    pen1.color('black','purple')
    pen1.begin_fill()
    drawCircle(pen1,158,-18,7)
    pen1.end_fill()

    pen1.color('black','yellow')
    pen1.begin_fill()
    drawCircle(pen1,158,-88,7)
    pen1.end_fill()

    pen1.color('black','purple')
    pen1.begin_fill()
    drawCircle(pen1,158,-148,7)
    pen1.end_fill()

    pen1.begin_fill()
    drawTriangle(pen1,122,133,30,60)
    pen1.end_fill()




    pen1.color('black','green')
    pen1.begin_fill()
    drawCircle(pen1,165,100,5)
    pen1.end_fill()

    pen1.begin_fill()
    drawCircle(pen1,135,100,5)
    pen1.end_fill()

    pen1.width(1)
    pen1.color('red','red')    
    pen1.begin_fill()
    drawCircle(pen1,150,85,7)
    pen1.end_fill()

    pen1.width(5)
    pen1.color('brown','brown')  
    drawLine(pen1,-100,25,225,125)

    drawLine(pen1,-200,25,315,125)

    drawLine(pen1,200,25,225,125)

    drawLine(pen1,100,25,315,125)


    exitonclick()