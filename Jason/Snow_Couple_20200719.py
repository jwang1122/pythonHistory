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
    # Snow Boy Upper Body
    pen1.color('black','white')
    pen1.begin_fill()
    drawCircle(pen1, bodyx, bodyy-115, bodyr+17)
    # Snow Boy Lower Lower Body
    pen1.color('black','white')
    pen1.begin_fill()
    drawCircle(pen1, bodyx, bodyy-275, bodyr+40)
    # Snow Girl Head
    pen1.color('black', 'white')
    pen1.begin_fill()
    drawCircle(pen1, bodyx+300, bodyy, bodyr)
    pen1.end_fill()
    # Snow Girl Upper Body
    pen1.color('black','white')
    pen1.begin_fill()
    drawCircle(pen1, bodyx+300, bodyy-115, bodyr+17)
    # Snow Girl Lower Lower Body
    pen1.color('black','white')
    pen1.begin_fill()
    drawCircle(pen1, bodyx+300, bodyy-275, bodyr+40)
    # Snow Boy Left Arm
    pen1.end_fill()
    pen1.color('brown')
    pen1.width(5)
    drawLine(pen1, bodyx+50, bodyy-40, -20, 100)
    # Snow Boy Right Arm
    pen1.end_fill()
    pen1.color('brown')
    pen1.width(5)
    drawLine(pen1, bodyx-40, bodyy-40, 185, 100)
    # Snow Girl Left Arm
    pen1.end_fill()
    pen1.color('brown')
    pen1.width(5)
    drawLine(pen1, bodyx+350, bodyy-40, 30, 100)
    # Snow Girl Right Arm Part1
    pen1.end_fill()
    pen1.color('brown')
    pen1.width(5)
    drawLine(pen1, bodyx+368, bodyy-130, -30, 80)
    # Snow Girl Right Arm Part2
    pen1.end_fill()
    pen1.color('brown')
    pen1.width(5)
    drawLine(pen1, bodyx+270, bodyy-40, 185, 110)
    # Snow Boy Hat
    pen1.width(1)
    pen1.color('brown')
    pen1.begin_fill()
    drawRectangle(pen1, bodyx-30, bodyy+140, 60, 70)
    pen1.end_fill()    
    pen1.end_fill()
    pen1.color('brown')
    pen1.width(5)
    drawLine(pen1, bodyx-50, bodyy+70, 90, 100)
    # Snow Girl Hat
    pen1.width(1)
    pen1.color('purple','yellow')
    pen1.begin_fill()
    drawTriangle(pen1, bodyx+260, bodyy+70, 30, 80)
    pen1.end_fill()

    # Snow Boy Buttons
    pen1.color('black', 'grey')
    pen1.begin_fill()
    drawCircle(pen1, bodyx, bodyy-20, 10)
    pen1.end_fill()

    pen1.color('black', 'grey')
    pen1.begin_fill()
    drawCircle(pen1, bodyx, bodyy-70, 10)
    pen1.end_fill()

    pen1.color('black', 'grey')
    pen1.begin_fill()
    drawCircle(pen1, bodyx, bodyy-150, 10)
    pen1.end_fill()

    pen1.color('black', 'grey')
    pen1.begin_fill()
    drawCircle(pen1, bodyx, bodyy-220, 10)
    pen1.end_fill()

    # Snow Girl Buttons
    pen1.color('black', 'yellow')
    pen1.begin_fill()
    drawCircle(pen1, bodyx+300, bodyy-20, 10)
    pen1.end_fill()

    pen1.color('black', 'purple')
    pen1.begin_fill()
    drawCircle(pen1, bodyx+300, bodyy-70, 10)
    pen1.end_fill()

    pen1.color('black', 'yellow')
    pen1.begin_fill()
    drawCircle(pen1, bodyx+300, bodyy-150, 10)
    pen1.end_fill()

    pen1.color('black', 'purple')
    pen1.begin_fill()
    drawCircle(pen1, bodyx+300, bodyy-200, 10)
    pen1.end_fill()

    # Snow Girl Hair
    pen1.end_fill()
    pen1.color('brown')
    pen1.width(3)
    drawLine(pen1, bodyx+270, 169, -70, 60)

    pen1.end_fill()
    pen1.color('brown')
    pen1.width(3)
    drawLine(pen1, bodyx+275, 169, -70, 30)

    pen1.end_fill()
    pen1.color('brown')
    pen1.width(3)
    drawLine(pen1, bodyx+330, 169, -110, 60)

    pen1.end_fill()
    pen1.color('brown')
    pen1.width(3)
    drawLine(pen1, bodyx+325, 169, -110, 30)

    eyeSize = 6
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
    # Snow Girl Eyes
    pen1.color('black', 'light green')
    pen1.begin_fill()
    drawCircle(pen1, 135, bodyy+50, eyeSize)
    pen1.end_fill()

    pen1.color('black', 'light green')
    pen1.begin_fill()
    drawCircle(pen1, 165, bodyy+50, eyeSize)
    pen1.end_fill()

    # Snow Boy Mouth
    pen1.end_fill()
    pen1.color('red')
    pen1.width(2)
    drawLine(pen1, -163, 117, 45, 14)
    drawLine(pen1, -138, 116, 0, 25)
    drawLine(pen1, -138, 116, 135, 14)

    # Snow Girl Mouth
    pen1.color('red', 'red')
    pen1.begin_fill()
    drawCircle(pen1, bodyx+300, bodyy+30, 8)
    pen1.end_fill()

    pen1.color('white')
    drawLine(pen1, -235, 120, -45, 15)
    
    exitonclick()
    
    