from turtle import Turtle, Screen
import random as rand

tim = Turtle()
tim.speed(0)
tim.pensize(1)
screen = Screen()
screen.colormode(255)
screen.setup(width=1000, height=1000)


# Challenge 2
def draw_dotted():
    for _ in range(10):
        tim.pendown()
        tim.forward(10)
        tim.penup()
        tim.forward(10)


# Challenge 3
def draw_shapes():
    """Draw triangle, square, pentagon, hexagon, heptagon, octagon, nonagon and decagon"""
    for i in range(3, 11):
        angle = calculate_angle(i)
        r = rand.randint(1, 255)
        g = rand.randint(1, 255)
        b = rand.randint(1, 255)
        tim.pencolor(r, g, b)
        tim.fillcolor(r, g, b)
        for x in range(1, i+1):
            tim.right(180 - angle)
            tim.forward(100)


def calculate_angle(side):
    return (side-2) * 180 / side


def random_color():
    r = rand.randint(1, 255)
    g = rand.randint(1, 255)
    b = rand.randint(1, 255)
    return r, g, b


# Challenge 4
def random_walk():
    tim.hideturtle()
    directions = [0, 90, 180, 270]
    while True:
        tim.pencolor(random_color())
        direct_forward = rand.choice(directions)
        direct_backward = rand.choice(directions)

        tim.right(direct_forward)
        tim.forward(25)
        tim.pencolor(random_color())
        tim.right(direct_backward)
        tim.forward(25)


# Challenge 5
def draw_spirograph(number_of_circles):
    tim.hideturtle()
    for _ in range(number_of_circles):
        tim.color(random_color())
        angle = 360 / number_of_circles
        tim.left(angle)
        tim.circle(100)


# Run codes here
draw_spirograph(90)


# Happens only at the end of the code
screen.exitonclick()
