from turtle import *
from shapes import *

pen1 = Turtle()

bodyx = -50
bodyy = 150
bodyr = 40
# Head 1
pen1.color('black', 'white')
pen1.begin_fill()
drawCircle(pen1, bodyx, bodyy, bodyr)
pen1.end_fill()
# Body 1
pen1.color('black','white')
pen1.begin_fill()
drawCircle(pen1, bodyx, bodyy-115, bodyr+17)
# Lower Body 1
pen1.color('black','white')
pen1.begin_fill()
drawCircle(pen1, bodyx, bodyy-275, bodyr+40)
# Head 2
pen1.color('black', 'white')
pen1.begin_fill()
drawCircle(pen1, bodyx+300, bodyy, bodyr)
pen1.end_fill()
# Body 2
pen1.color('black','white')
pen1.begin_fill()
drawCircle(pen1, bodyx+300, bodyy-115, bodyr+17)
# Lower Body 2
pen1.color('black','white')
pen1.begin_fill()
drawCircle(pen1, bodyx+300, bodyy-275, bodyr+40)
# Arm 1a
pen1.end_fill()
pen1.color('brown')
pen1.width(5)
drawLine(pen1, bodyx+50, bodyy-40, -20, 100)
# Arm 1b
pen1.end_fill()
pen1.color('brown')
pen1.width(5)
drawLine(pen1, bodyx-40, bodyy-40, 185, 100)
# Arm 2a
pen1.end_fill()
pen1.color('brown')
pen1.width(5)
drawLine(pen1, bodyx+350, bodyy-40, 30, 100)
# Arm 2aa
pen1.end_fill()
pen1.color('brown')
pen1.width(5)
drawLine(pen1, bodyx+368, bodyy-130, -30, 80)
# Arm 2b
pen1.end_fill()
pen1.color('brown')
pen1.width(5)
drawLine(pen1, bodyx+270, bodyy-40, 185, 110)
# Hat 1
pen1.width(1)
pen1.color('brown')
pen1.begin_fill()
drawRectangle(pen1, bodyx-30, bodyy+140, 60, 70)
pen1.end_fill()

pen1.end_fill()
pen1.color('brown')
pen1.width(5)
drawLine(pen1, bodyx-50, bodyy+70, 90, 100)
# Hat 2
pen1.width(1)
pen1.color('purple','yellow')
pen1.begin_fill()
drawTriangle(pen1, bodyx+260, bodyy+70, 30, 80)
pen1.end_fill()
# Dots 1
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
# Dots 2
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
drawCircle(pen1, bodyx+300, -70, 10)
pen1.end_fill()
# Hair 2
pen1.end_fill()
pen1.color('brown')
pen1.width(3)
drawLine(pen1, bodyx+270, 219, -70, 60)

pen1.end_fill()
pen1.color('brown')
pen1.width(3)
drawLine(pen1, bodyx+275, 219, -70, 30)

pen1.end_fill()
pen1.color('brown')
pen1.width(3)
drawLine(pen1, bodyx+330, 219, -110, 60)

pen1.end_fill()
pen1.color('brown')
pen1.width(3)
drawLine(pen1, bodyx+325, 219, -110, 30)

eyeSize = 3
eyey = 200
# Eyes 1
pen1.color('black', 'blue')
pen1.begin_fill()
drawCircle(pen1, -65, bodyy+50, eyeSize)
pen1.end_fill()

pen1.color('black', 'blue')
pen1.begin_fill()
drawCircle(pen1, -35, bodyy+50, eyeSize)
pen1.end_fill()
# Eyes 2
pen1.color('black', 'light green')
pen1.begin_fill()
drawCircle(pen1, 235, bodyy+50, eyeSize)
pen1.end_fill()

pen1.color('black', 'light green')
pen1.begin_fill()
drawCircle(pen1, 265, bodyy+50, eyeSize)
pen1.end_fill()

mainloop()
