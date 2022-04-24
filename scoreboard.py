from turtle import Turtle

FONT_SIZE = 18
FONT = ('Courier', FONT_SIZE, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        with open("highest_score.txt", mode="r") as file:
            self.high_score = file.read()
        self.high_score = int(self.high_score)
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 260)
        self.points = 0
        self.write(f"Score: {self.points}", align="center", font=FONT)

    def reset_game(self):
        if self.points > self.high_score:
            self.high_score = self.points
            with open("highest_score.txt", mode="w") as file:
                file.write(str(self.high_score))
        self.points = 0
        self.update_score_board()

    def update_score_board(self):
        self.clear()
        self.write(f"Score:{self.points}. Highest score: {self.high_score}", align="center", font=FONT)

    def score_track(self):
        self.points += 1
        self.update_score_board()
