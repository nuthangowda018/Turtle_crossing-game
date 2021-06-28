from turtle import  Turtle
FONT=("courier",24,"normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=1
        self.hideturtle()
        self.penup()
        self.goto(-280,260)
        self.show_score()

    def show_score(self):
        self.clear()
        self.write(f"level:{self.score}",align="left",font=FONT)

    def update_score(self):
        self.score+=1
        self.show_score()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER",align="center",font=FONT)

