from turtle import *
from shapes import *

pen1 = Turtle()

pen1.color('black','red')
pen1.begin_fill()
drawCircle(pen1, 0, 0, 30)
pen1.end_fill()
pen1.color('black','blue')
pen1.begin_fill()
drawRectangle(pen1, 40, 40, 50, 30)
pen1.end_fill()
pen1.color('dark red')
pen1.width(5)
drawLine(pen1, 0, 0, 45, 150)
pen1.width(1)
pen1.color('black','yellow')
pen1.begin_fill()
drawTriangle(pen1, 150, 150, 30, 100)
pen1.end_fill()

mainloop()