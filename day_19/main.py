from turtle import Turtle, Screen
import random as rand

red_turtle = Turtle()
blue_turtle = Turtle()
black_turtle = Turtle()
green_turtle = Turtle()
grey_turtle = Turtle()

list_turtle = [
    red_turtle,
    blue_turtle,
    black_turtle,
    green_turtle,
    grey_turtle,
]

LANE_COORDINATES = [
    (-230, 100),
    (-230, 50),
    (-230, 0),
    (-230, -50),
    (-230, -100),
]

COLOUR_COORDINATES = [
    (128, 0, 0),
    (0, 0, 128),
    (0, 0, 0),
    (0, 82, 33),
    (72, 72, 72),
]

is_race_on = True
winning_turtle = Turtle()

screen = Screen()
screen.colormode(255)
screen.setup(width=500, height=400)


user_guess = screen.textinput(title="Make your bet", prompt="Who will win the race? Enter a colour")


# Setting attributes of each turtles

for index, turtle in enumerate(list_turtle):
    turtle.shape(name="turtle")
    turtle.color(COLOUR_COORDINATES[index])
    turtle.penup()
    turtle.goto(LANE_COORDINATES[index])


while is_race_on:
    for turtle in list_turtle:
        turtle_speed = rand.randint(0, 10)
        turtle.forward(turtle_speed)
        if turtle.xcor() > 230:
            winning_turtle = turtle
            if winning_turtle.color() == user_guess.lower():
                print("Correct!")
            else:
                print("Incorrect!")
            is_race_on = False
            break


screen.exitonclick()
