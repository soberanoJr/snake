from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):

        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.75, stretch_wid=0.75)
        self.color("yellow")
        self.speed("fastest")
        self.refresh()

    def refresh(self):

        x = random.uniform(-380, 380)
        y = random.uniform(-280, 280)
        self.goto(x, y)
