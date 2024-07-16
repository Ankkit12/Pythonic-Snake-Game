from turtle import Turtle
ALIGNMENT = "center"
FONT = ('courier', 15, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.High_score = int(data.read())
        self.color("red")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        """This function updates the scores"""
        self.clear()
        self.write(f"Score = {self.score}, High Score = {self.High_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        """This function sets the High score and resets new score"""
        if self.score > self.High_score:
            self.High_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.High_score}")
        self.score = 0
        self.update_score()

    def increase_score(self):
        """This function increases the score"""
        self.score += 1
        self.update_score()

