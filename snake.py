from turtle import Turtle


COORDINATES = [(0, 0), (-20, 0), (-40, 0)]
DISTANCE = 20
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270


class Snake:

    def __init__(self):
        
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        
        for position in COORDINATES:
            self.add_segment(position)

    def add_segment(self, position):
        
        snake = Turtle(shape="square")
        snake.color("white")
        snake.penup()
        snake.goto(position)
        self.segments.append(snake)

    def extend(self):
        
        self.add_segment(self.segments[-1].position())
        
    def move(self):
        
        for _ in range(len(self.segments) - 1, 0, -1):
            x = self.segments[_ - 1].xcor()
            y = self.segments[_ - 1].ycor()
            self.segments[_].goto(x, y)
        self.head.forward(DISTANCE)

    def right(self):
        
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)    
    
    def up(self):
        
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def left(self):
        
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
        
    def down(self):

        if self.head.heading() != UP:
            self.head.setheading(DOWN)
