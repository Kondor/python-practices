import turtle


def draw_eye(colour, radius):
    turtle.pendown()
    turtle.fillcolor(colour)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()
    turtle.penup()


turtle.shape('turtle')
turtle.speed(1)
turtle.pensize(2)
turtle.color('black')

turtle.fillcolor('yellow')
turtle.begin_fill()
turtle.circle(100)
turtle.end_fill()
turtle.penup()

turtle.goto(-40, 110)
draw_eye('white', 20)
turtle.goto(-40, 110)
draw_eye('black', 14)

turtle.goto(40, 110)
draw_eye('white', 20)
turtle.goto(40, 110)
draw_eye('black', 14)

turtle.goto(-40, 80)
turtle.pendown()
turtle.right(90)
turtle.circle(30, 150)
turtle.penup()

turtle.goto(-10, -50)
turtle.done()
