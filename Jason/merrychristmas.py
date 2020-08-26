import turtle

pen = turtle.Turtle()
def jason_circle(color, radius, x, y):
    pen.penup()
    pen.goto(x,y)
    pen.pendown()
    pen.fillcolor(color)
    pen.begin_fill()
    pen.circle(radius)
    pen.end_fill()

# 3 circles for snowman body
jason_circle("#ffffff", 30, 0, -40)
jason_circle("#ffffff", 40, 0, -100)
jason_circle("#ffffff", 60, 0, -200)

# Eyes and Nose
jason_circle("#ffffff", 2, -10, -10) 
jason_circle("#ffffff", 2, 10, -10) 
jason_circle("#FF6600", 3, 0, -15) 

# Buttons
jason_circle("#ffffff", 2, 0, -35)
jason_circle("#ffffff", 2, 0, -45)
jason_circle("#ffffff", 2, 0, -55)

# Two arms
pen.penup()
pen.goto(-15,-35)
pen.pendown()
pen.pensize(5)
pen.goto(-75, -50)

pen.penup()
pen.goto(15,-35)
pen.pendown()
pen.pensize(5)
pen.goto(75, -50)

# Hat
pen.penup()
pen.goto(-35, 8)
pen.color("black")
pen.pensize(6)
pen.pendown()
pen.goto(35, 8)
 
pen.goto(30, 8)
pen.fillcolor("black")
pen.begin_fill()
pen.left(90)
pen.forward(15)
pen.left(90)
pen.forward(60)
pen.left(90)
pen.forward(15)
pen.end_fill()

#exit()
print('Jason finishes here')