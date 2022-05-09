from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(
            stretch_len=1, 
            stretch_wid=1
        )
        self.color("yellow")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        x = random.uniform(-300, 300)
        y = random.uniform(-300, 300)
        self.goto(x, y)