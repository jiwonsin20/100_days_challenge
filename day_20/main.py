from turtle import Screen
import time as time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

# Create Screen instance
screen = Screen()
screen.bgcolor(0, 0, 0)
screen.setup(width=600, height=600)
screen.title("Snake Game")
screen.tracer(0)

# Create Snake object
snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # Check whether wall collision occurred
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 \
            or snake.head.ycor() > 280 or snake.head.ycor() < -280\
            or snake.tail_collision():
        game_on = False
        scoreboard.game_over()

    if food.distance(snake.head.xcor(), snake.head.ycor()) < 1:
        food.clear()
        food.create_food()
        snake.increase()
        scoreboard.update_score(snake.snake_list)

screen.exitonclick()
