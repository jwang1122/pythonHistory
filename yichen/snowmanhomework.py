from turtle import *
from shapes import *

pen1 = Turtle()
#head
pen1.color('black','white')
pen1.begin_fill()
drawCircle(pen1, 180, 200, 30)
pen1.end_fill()
#yellow hat
pen1.color('hot pink','yellow')
pen1.begin_fill()
drawTriangle(pen1, 150, 250, 0, 60)
pen1.end_fill()

#middle circle
pen1.color('black','white')
pen1.begin_fill()
drawCircle(pen1, 180, 103, 48)
pen1.end_fill()
#biggest circle
pen1.color('black','white')
pen1.begin_fill()
drawCircle(pen1, 180, -36.5, 70)
pen1.end_fill()
#middle buttons
pen1.color('black','yellow')
pen1.begin_fill()
drawCircle(pen1, 180, 165, 9)
pen1.end_fill()
pen1.color('black','purple')
pen1.begin_fill()
drawCircle(pen1, 180, 125, 9)
pen1.end_fill()
#bottom circles
pen1.color('black','yellow')
pen1.begin_fill()
drawCircle(pen1, 180, 48, 10)
pen1.end_fill()
pen1.color('black','purple')
pen1.begin_fill()
drawCircle(pen1, 180, -4, 10)
pen1.end_fill()
#eyes
pen1.color('black','light green')
pen1.begin_fill()
drawCircle(pen1, 170, 228, 4)
pen1.end_fill()
pen1.color('black','light green')
pen1.begin_fill()
drawCircle(pen1, 190, 228, 4)
pen1.end_fill()
#mouth
pen1.color('red','red')
pen1.begin_fill()
drawCircle(pen1, 180, 208, 7)
pen1.end_fill()
pen1.width(2)
drawLine(pen1, 175, 212, 220, 12)
drawLine(pen1, 185, 212, 320, 12)
#arms
pen1.width(5)
pen1.color('brown')
drawLine(pen1, 150, 160, 188, 100)
drawLine(pen1, 220, 170, 40, 80)
drawLine(pen1, 280, 120, 150, 60)
#hair
pen1.width(3)
drawLine(pen1, 155, 250, 105, 40)
drawLine(pen1, 205, 250, 75, 40)
drawLine(pen1, 160, 250, 105, 20)
drawLine(pen1, 200, 250, 75, 20)



#snowman2head

pen1.width(1)
pen1.color('black','white')
pen1.begin_fill()
drawCircle(pen1, -100, 200, 30)
pen1.end_fill()
pen1.color('black','blue')
pen1.begin_fill()
#hat
pen1.color('brown','brown')
pen1.begin_fill()
drawRectangle(pen1, -122, 250, 45, 60)
pen1.end_fill()
# the edge of hat
pen1.width(5)
pen1.color('brown')
drawLine(pen1, -145, 250, 0, 90)
pen1.width(1)
#middle circle
pen1.color('black','white')
pen1.begin_fill()
drawCircle(pen1, -100, 103, 48)
pen1.end_fill()
#arms
pen1.width(5)
pen1.color('brown')
drawLine(pen1, -130, 170, 186, 90)
drawLine(pen1, -58, 165, 340, 90)
#mouth
pen1.width(3)
pen1.color('red')
drawLine(pen1, -108, 215, 0, 18)
drawLine(pen1, -115, 220, 32, 10)
drawLine(pen1, -92, 215, 328, 10)
#biggest circle
pen1.width(1)
pen1.color('black','white')
pen1.begin_fill()
drawCircle(pen1, -100, -36.5, 70)
pen1.end_fill()
#middle buttons
pen1.color('black','light gray')
pen1.begin_fill()
drawCircle(pen1, -100, 165, 9)
pen1.end_fill()
pen1.color('black','light gray')
pen1.begin_fill()
drawCircle(pen1, -100, 125, 9)
pen1.end_fill()
#bottom buttons
pen1.color('black','light gray')
pen1.begin_fill()
drawCircle(pen1, -100, 48, 10)
pen1.end_fill()
pen1.color('black','light gray')
pen1.begin_fill()
drawCircle(pen1, -100, -4, 10)
pen1.end_fill()
#eyes
pen1.color('black','blue')
pen1.begin_fill()
drawCircle(pen1, -110, 228, 4)
pen1.end_fill()
pen1.color('black','blue')
pen1.begin_fill()
drawCircle(pen1, -90, 228, 4)
pen1.end_fill()
pen1.hideturtle()



mainloop()