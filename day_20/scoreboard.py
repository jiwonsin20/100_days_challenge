from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.create_scoreboard()
        self.score = 0
        self.high_score = 0

    def create_scoreboard(self):
        self.penup()
        self.goto(0, 270)
        self.color("white")
        self.write(arg="Score: 0", move=False, align="center", font=("Consoles", 12, "normal"))
        self.hideturtle()

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="Game Over", move=False, align="center", font=("Consoles", 30, "normal"))

    def update_score(self, lst):
        self.clear()
        self.write(arg=f"Score: {len(lst) -3}", move=False, align="center", font=("Consoles", 12, "normal"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
