def drawCircle(pen1, x, y, r):
    """
    draw a circle with radius r and position (x, y)
    """
    pen1.penup()
    pen1.goto(x,y)
    pen1.down()
    pen1.circle(r)
    pen1.penup()

def drawRectangle(pen1, x, y, width, height):
    """
    draw a circle with radius r and position (x, y)
    """
    pen1.up()
    pen1.goto(x, y)
    pen1.down()
    pen1.fd(width)
    pen1.left(90)
    pen1.fd(height)
    pen1.left(90)
    pen1.fd(width)
    pen1.left(90)
    pen1.fd(height)
    pen1.left(90)

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
    pen1.left(angle)
    pen1.fd(side)
    pen1.left(120)
    pen1.fd(side)
    pen1.left(120)
    pen1.fd(side)
    pen1.left(120)
    

