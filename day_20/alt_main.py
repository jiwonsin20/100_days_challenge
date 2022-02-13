import turtle
from turtle import Turtle, Screen
import random as rnd

# Create Global variables
is_dead = False
tails = 2
max_x = 300
min_x = -300
max_y = 300
min_y = -300
staring_positions = [(0, 0), (-20, 0), (-40, 0)]

# Create Screen instance
snake_game_screen = Screen()
snake_game_screen.bgcolor(0, 0, 0)
snake_game_screen.setup(width=600, height=600)
snake_game_screen.title("Snake Game")
snake_game_screen.tracer(n=1, delay=50)

# List of snakes
snake_list = []

# Create snake body
snake_head = Turtle()
snake_head.penup()
snake_head.shape("square")
snake_head.color("white")

# Create initial snake body
for i in range(len(staring_positions)):
    new_turtle = Turtle()
    new_turtle.setposition()
    new_turtle.shape("square")
    snake_list.append(Turtle())

# Create random food object
food = Turtle()
food.penup()
food.shape("circle")
food.color("yellow")
food_coordinate = (round(rnd.randint(-280, 280)/20)*20, round(rnd.randint(-280, 280)/20)*20)
print(food_coordinate)
food.setpos(food_coordinate)


# Movement commands
def turn_left():
    current_angle = snake_head.heading()
    snake_head.setheading(current_angle+90)


def turn_right():
    current_angle = snake_head.heading()
    snake_head.setheading(current_angle-90)


def move():
    snake_head.forward(20)


def border_control():
    if snake_head.xcor() > max_x - 40 or snake_head.xcor() < min_x - 40 \
            or snake_head.ycor() > max_y - 40 or snake_head.ycor() < min_y - 40:
        return False
    return True


def create_default_tails():
    for i in range(2):
        snake_head.stamp()
        snake_head.forward(20)


def add_tails():
    snake_head.stamp()
    snake_head.forward(20)


# create_default_tails()
# while border_control():
#     add_tails()
#     snake_head.clearstamps(1)
#     snake_game_screen.listen()
#     snake_game_screen.onkey(fun=turn_left, key="q")
#     snake_game_screen.onkey(fun=turn_right, key="e")
#     snake_game_screen.onkey(fun=move, key="space")


snake_game_screen.exitonclick()
