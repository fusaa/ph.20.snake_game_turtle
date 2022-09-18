from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.score = 0
        self.high_score = 0
        self.goto(-60, 280)
        self.message = "Score: " + str(self.score)
        self.write(self.message)

    def update(self):
        self.score += 1
        self.message = "Score: " + str(self.score)
        self.clear()
        self.write(self.message)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER")
    # def start_over(self):
    #     self.goto(0,0)

