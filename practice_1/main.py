import turtle

# Количество углов в многоугольнике
n = 30

# Ф-ла правильного многоугольника
x = (n - 2) * 180 / n

# Задание х-к
turtle.shape('turtle')
turtle.penup()
turtle.goto(-20, 100)
turtle.pendown()
turtle.speed(1)
turtle.color('green')
turtle.pensize(2)

# Рисование окружности
for i in range(n):
    # Движение кисти вперёд
    turtle.forward(50)

    # Вращение по часовой стрелке
    turtle.right(180 - x)

turtle.done()