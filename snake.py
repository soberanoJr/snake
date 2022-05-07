from turtle import Turtle


COORDINATES = [(0, 0), (-20, 0), (-40, 0)]
DISTANCE = 20

class Snake:

    def __init__(self):
        self.tail = []
        self.create_snake()

    def create_snake(self):
        for coordinate in COORDINATES:
            snake = Turtle(shape="square")
            snake.color("white")
            snake.penup()
            snake.goto(coordinate)
            self.tail.append(snake)


    def move(self):
        for _ in range(len(self.tail) -1, 0, -1):
            x = self.tail[_ - 1].xcor()
            y = self.tail[_ - 1].ycor()
            self.tail[_].goto(x, y)
        self.tail[0].forward(DISTANCE)