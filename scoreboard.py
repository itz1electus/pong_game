from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score1 = 0
        self.score2 = 0
        self.update_score()

    def update_score(self):
        self.goto(-100, 200)
        self.write(self.score2, align='center', font=("Arial", 80, "normal"))
        self.goto(100, 200)
        self.write(self.score1, align='center', font=("Arial", 80, "normal"))
        self.goto(0, 222)
        self.write("Score", align='center', font=("Courier", 40, "normal"))

    def point2(self):
        self.score2 += 1
        self.clear()
        self.update_score()

    def point1(self):
        self.score1 += 1
        self.clear()
        self.update_score()
