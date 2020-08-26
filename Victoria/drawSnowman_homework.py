from turtle import *
from shapes_old import *

pen1 = Turtle()

#body
drawCircle(pen1, -150, 150, 50)
drawCircle(pen1, -150, 0, 75)
drawCircle(pen1, -150, -200, 100)

#hat
pen1.color('brown')
pen1.width(5)
drawLine(pen1, -210, 235, 0, 120)
pen1.begin_fill()
drawRectangle(pen1, -180, 315, 60, 80)
pen1.end_fill()

#eyes
pen1.color('black','blue')
pen1.width(1)
pen1.begin_fill()
drawCircle(pen1, -170, 205, -5)
pen1.end_fill()
pen1.begin_fill()
drawCircle(pen1, -130, 205, 5)
pen1.end_fill()

#mouth
pen1.color('red')
pen1.width(5)
drawLine(pen1, -175, 185, 310, -10)
pen1.right(90)
drawLine(pen1, -165, 178, 0, 30)
drawLine(pen1, -135, 178, 320, 10)

#buttons
pen1.color('black','light gray')
pen1.width(1)
pen1.begin_fill()
drawCircle(pen1, -150, 100, 10)
pen1.end_fill()
pen1.begin_fill()
drawCircle(pen1, -150, 40, 10)
pen1.end_fill()
pen1.begin_fill()
drawCircle(pen1, -150, -70, 15)
pen1.end_fill()
pen1.begin_fill()
drawCircle(pen1, -150, -150, 15)
pen1.end_fill()

#arms
pen1.color('brown')
pen1.width(5)
drawLine(pen1, -200, 100, 7, -120)
drawLine(pen1, -85, 100, 340, 120)

#body
pen1.color('black')
pen1.width(1)
drawCircle(pen1, 150, 150, 50)
drawCircle(pen1, 150, 0, 75)
drawCircle(pen1, 150, -200, 100)

#hat
pen1.color('black','yellow')
pen1.begin_fill()
drawTriangle(pen1, 150, 315, 60, 100)
pen1.end_fill()

#hair
pen1.color('brown')
pen1.width(5)
drawLine(pen1, 105, 225, 345, -60)
drawLine(pen1, 115, 225, 345, -30)
pen1.left(45)
drawLine(pen1, 185, 225, 180, 30)
drawLine(pen1, 195, 225, 180, 60)

#eyes
pen1.color('black','light green')
pen1.width(1)
pen1.begin_fill()
drawCircle(pen1, 140, 205, 5)
pen1.end_fill()
pen1.begin_fill()
drawCircle(pen1, 170, 205, 5)
pen1.end_fill()

#mouth
pen1.color('red', 'red')
pen1.width(5)
drawLine(pen1, 137, 180, 330, -10)
pen1.right(105)
drawLine(pen1, 147, 173, 0, 10)
drawLine(pen1, 157, 173, 310, 10)
pen1.begin_fill()
drawCircle(pen1, 150, 170, 5)
pen1.end_fill()

#buttons
pen1.color('black','yellow')
pen1.width(1)
pen1.begin_fill()
drawCircle(pen1, 150, 100, 10)
pen1.end_fill()
pen1.color('black','purple')
pen1.begin_fill()
drawCircle(pen1, 150, 40, 10)
pen1.end_fill()
pen1.color('black','yellow')
pen1.begin_fill()
drawCircle(pen1, 150, -70, 15)
pen1.end_fill()
pen1.color('black','purple')
pen1.begin_fill()
drawCircle(pen1, 150, -150, 15)
pen1.end_fill()

#arms
pen1.color('brown')
pen1.width(5)
drawLine(pen1, 100, 100, 7, -120)
drawLine(pen1, 215, 100, 35, 100)
drawLine(pen1, 300, 40, 330, -90)

pen1.hideturtle()
mainloop()