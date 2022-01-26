import turtle
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
# screen.colormode(255)
turtle.colormode(255)


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


def draw_spirograph(radius, circles, width, speed):
    heading = 0
    increment = 360 / circles
    tim.pensize(width)
    tim.speed(speed)
    for _ in range(circles):
        heading += increment
        tim.setheading(heading)
        tim.color(random_color())
        tim.circle(radius)


def draw_spirograph_spacing(radius, spacing, width, speed):
    heading = 0
    angle_to_increment = int(360 / spacing)
    tim.pensize(width)
    tim.speed(speed)
    for _ in range(angle_to_increment):
        tim.color(random_color())
        tim.circle(radius)
        tim.setheading(tim.heading()+spacing)


def random_walk(distance, pensize_width, speed):
    heading = choice([0, 90, 180, 270])
    tim.setheading(heading)
    tim.pensize(pensize_width)
    tim.speed(speed)
    tim.color(random_color())
    tim.forward(distance)


def multi_random_walk(number_of_sims, number_of_moves, distance, pensize_width, speed,dot_size):
    tim.pensize(pensize_width)
    tim.speed(speed)
    tim.shape("turtle")
    for _ in range(number_of_sims):
        tim.pendown()
        tim.color(random_color())
        for moves in range(number_of_moves):
            heading = choice([0, 90, 180, 270])
            tim.setheading(heading)
            tim.forward(distance)
        tim.dot(dot_size)
        tim.penup()
        tim.home()

# side_length = 100
# #
# for s in range(3, 10 + 1):
#     draw_shape(s, side_length)
#     print(s)
# a cor random podia ter sido feita pela escolha de uma cor numa lista com nomes das cores

# moves = 200
# steps = 20
# pen_width = 3
# turtle_speed = "fastest"
#
# for _ in range(moves):
#     random_walk(steps, pen_width, turtle_speed)


sims = 20
moves = 100
steps = 20
pen_width = 3
turtle_speed = 30
dot_size = 10
multi_random_walk(sims, moves, steps, pen_width, turtle_speed, dot_size)


# radius = 100
# number_circles = 90
# # draw_spirograph(radius, number_circles, pen_width, turtle_speed)
#
# spacing_between_circles = 5
# draw_spirograph_spacing(radius,spacing_between_circles, pen_width, turtle_speed)

screen.exitonclick()
