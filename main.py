from random import random, randrange, randint, choice
from turtle import Turtle, Screen

tim = Turtle()


# timmy_the_turtle.shape("turtle")
# timmy_the_turtle.color("blue")
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)

# for s in range(4):
#     tim.forward(100)
#     tim.right(90)

# for _ in range(15):
#     tim.color("blue")
#     tim.forward(5)
#     tim.color("white")
#     tim.forward(5)

# tim.pendown()
# for _ in range(15):
#     tim.forward(5)
#     tim.penup()
#     tim.forward(5)
#     tim.pendown()

# side = 100
# for sides_number in range(3,10):
#     for t in range(sides_number):
#         tim.forward(side)
#         angle = 360/sides_number
#         tim.right(angle)
screen = Screen()
screen.colormode(255)


def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return r, g, b


def draw_shape(number_of_sides, side_length):
    angle = 360 / number_of_sides
    # r = randint(0,255)
    # g = randint(0,255)
    # b = randint(0,255)
    tim.pencolor(random_color())
    for _ in range(number_of_sides):
        tim.forward(side_length)
        tim.right(angle)


def random_walk(distance, pensize_width, speed):
    heading = choice([0, 90, 180, 270])
    tim.setheading(heading)
    tim.pensize(pensize_width)
    tim.speed(speed)
    tim.color(random_color())
    tim.forward(distance)


# side_length = 100
#
# for s in range(3, 10 + 1):
#     draw_shape(s, side_length)
#     print(s)
# a cor random podia ter sido feita pela escolha de uma cor numa lista com nomes das cores

moves = 77
steps = 20
pen_width = 5
turtle_speed = 10
for _ in range(moves):
    print(_)
    random_walk(steps, pen_width, turtle_speed)

screen.exitonclick()
