from turtle import Turtle


ALIGNMENT = "center"
FONT = ("Arial", 64, "normal")


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("yellow")
        self.penup()
        self.goto(0,0)
        self.hideturtle()
        self.update()

    def update(self):
        self.write(self.score, 
                   align=ALIGNMENT, 
                   font=FONT
        )
    
    def count(self):
        self.score += 1
        self.clear()
        self.update()


    def game_over(self):
        self.clear()
        self.write("GAME OVER", 
                   align=ALIGNMENT, 
                   font=FONT
        )