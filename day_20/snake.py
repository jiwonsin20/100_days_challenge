from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:

    def __init__(self):
        """Constructor for snake object"""
        self.snake_list = []
        self.create_snake()
        self.head = self.snake_list[0]

    def create_snake(self):
        """Creates a snake object with 3 sections"""
        for position in STARTING_POSITIONS:
            snake = Turtle()
            snake.shape("square")
            snake.penup()
            snake.goto(position)
            snake.color("white")
            self.snake_list.append(snake)

    def move(self):
        """Instructs how the snake should move"""
        for snake_num in range(len(self.snake_list) - 1, 0, -1):
            if snake_num > 0:
                previous_snake = self.snake_list[snake_num - 1]
                current_snake = self.snake_list[snake_num]
                new_x = previous_snake.xcor()
                new_y = previous_snake.ycor()
                current_snake.goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        """Moves the Snake upwards (90 degrees)"""
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        """Moves the Snake downwards"""
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        """Change Snake headings to left"""
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        """Change Snake headings to Right"""
        if self.head.heading() != 180:
            self.head.setheading(0)

    def tail_collision(self):
        for element in self.snake_list[1:]:
            if self.head.distance(element) < 1:
                return True

    def increase(self):
        """Increase length of snake"""
        new_element = Turtle("square")
        new_element.penup()
        new_element.color("white")
        predecessor = self.snake_list[-1]
        new_element.goto(predecessor.xcor(), predecessor.ycor())
        self.snake_list.append(new_element)

