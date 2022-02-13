from turtle import Turtle
import random as rand


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.create_food()

    def create_food(self):
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("yellow")
        self.speed("fastest")
        x_cor = round(rand.randint(-280, 280) / 20)
        y_cor = round(rand.randint(-280, 280) / 20)
        self.goto(x_cor*20, y_cor*20)
