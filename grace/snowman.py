from shapes import *

class Snowman:
    """
    Draw a snowman
    """
    def __init__(self, bottomX, bottomY, head, body, leg, male):
        """
        bottomX: snowman leg horizontal position
        bottomY: snowman leg vertical position
        head: snowman head radius
        body: snowman body radius
        leg: snowman leg radius
        """
        self.bottomX = bottomX
        self.bottomY = bottomY
        self.head = head
        self.body = body
        self.leg = leg
        self.male = male

    def drawBody(self, pen1):
        """
        Use given pen1 = Turtle() draw a circle with radius = self.body
        as snowman body. After the drawing,
        the turtle point to right direction.
        """
        drawCircle(pen1,self.bottomX, self.bottomY+2*self.leg, self.body)
        if self.male:
            pen1.color('black','gray')
            pen1.begin_fill()
            drawCircle(pen1, self.bottomX, self.bottomY+1*self.leg + 20, 5)
            pen1.end_fill()
            pen1.color('black','gray')
            pen1.begin_fill()
            drawCircle(pen1, self.bottomX, self.bottomY+1*self.leg - 20, 5)
            pen1.end_fill()
            pen1.color('black','gray')
            pen1.begin_fill()
            drawCircle(pen1, self.bottomX, self.bottomY+2.5*self.leg, 5)
            pen1.end_fill()
        else:
            pen1.color('black','yellow')
            pen1.begin_fill()
            drawCircle(pen1, self.bottomX, self.bottomY+1*self.leg + 20, 5)
            pen1.end_fill()
            pen1.color('black','purple')
            pen1.begin_fill()
            drawCircle(pen1, self.bottomX, self.bottomY+1*self.leg - 20, 5)
            pen1.end_fill()
            pen1.color('black','purple')
            pen1.begin_fill()
            drawCircle(pen1, self.bottomX, self.bottomY+1*self.leg + 105, 5)
            pen1.end_fill()

    def drawHead(self, pen1):
        """
        Use given pen1 = Turtle draw a circle with radius = self.head
        after the drawing, turtle point to right.
        """
        headBottomY = self.bottomY + 2*self.leg+2*self.body
        headBottomX = self.bottomX + self.head*1/4
        drawCircle(pen1,self.bottomX, headBottomY, self.head)
        pen1.pu()
        pen1.goto(headBottomX, headBottomY + self.head*3/5)
        pen1.left(30)
        pen1.down()
        pen1.circle(self.head*2/3, -60)
        pen1.up()
        pen1.left(30)
        pen1.color('black','blue')
        pen1.begin_fill()
        drawCircle(pen1,headBottomX - int(self.head*3/5), headBottomY + int(self.head*4/5), int(self.head*1/5))
        pen1.end_fill()
        pen1.color('black','blue')
        pen1.begin_fill()
        drawCircle(pen1,headBottomX + int(self.head*1/5), headBottomY + int(self.head*4/5), int(self.head*1/5))
        pen1.end_fill()
#        pen1.circle(headBottomX + self.head*1/5, headBottomY + self.head*4/5, self.head*1/5)

    def drawLeg(self, pen1):
        """
        Use given pen1 = Turtle() draw a circle with radius = self.leg
        as snowman leg, after the drawing, turtle point to right.
        """
        pen1.pu()
        pen1.goto(self.bottomX, self.bottomY)
        pen1.down()
        pen1.circle(self.leg)

    def drawArms(self, pen1):
        x = self.bottomX-self.body
        y = (self.bottomY+2*self.leg+self.body)
        pen1.width(5)
        pen1.color("darkred")
        # right arm
        drawLine(pen1, x, y, 145, self.body)
        pen1.left(120)
        pen1.fd(self.body)
        pen1.right(120)

        pen1.penup()
        pen1.goto(x+2*self.body, y)
        pen1.right(45)
        pen1.down()
        # left arm
        pen1.fd(self.body)
        pen1.left(45)
        if self.male:
            pen1.right(30)
            pen1.fd(self.body)
            pen1.left(30)
        else:
            pen1.right(120)
            pen1.fd(self.body)
            pen1.left(120)
        pen1.color("black")
        pen1.width(1)

    def drawHat(self, pen1):
        if self.male:
            x = self.bottomX-self.head
            y = self.bottomY + 2*self.body + 2*self.leg + 2*self.head - self.head/5
            pen1.color('black','darkred')
            pen1.begin_fill()
            drawRectangle(pen1, x, y, 2*self.head, 3*self.head)
            pen1.end_fill()
            pen1.width(5)
            pen1.bk(self.head*1/5)
            pen1.fd(2.3*self.head)
            pen1.width(1)
        else:
            x = self.bottomX-1*self.head
            y = self.bottomY + 2*self.body + 2*self.leg + 2*self.head - self.head/5
            pen1.color('black','yellow')
            pen1.begin_fill()
            drawTriangle(pen1, x, y, 0, 2*self.head)
            pen1.end_fill()
            pen1.width(1)
            
            x = (self.bottomX-1*self.head)+5
            y = self.bottomY + 2*self.body + 2*self.leg + 2*self.head - self.head/5
            pen1.color('black')
            drawLine(pen1, x, y, 110, 2*self.head)
            pen1.width(1)

            x = (self.bottomX-1*self.head)+35
            y = self.bottomY + 2*self.body + 2*self.leg + 2*self.head - self.head/5
            pen1.color('black')
            drawLine(pen1, x, y, 70, 2*self.head)
            pen1.width(1)

            pass

    def draw(self, pen1):
        """
        Draw a snowman.
        """
        self.drawLeg(pen1)
        self.drawBody(pen1)
        self.drawArms(pen1)
        self.drawHead(pen1)
        self.drawHat(pen1)
        pen1.hideturtle()

