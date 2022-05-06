from turtle import Screen, Turtle


screen = Screen()
screen.setup(width=1.0, height=1.0)
screen.bgcolor("black")
screen.title("===+" * 5 +"===:> snake")
coordinates = [(0, 0), (-20, 0), (-40, 0)]

for coordinate in coordinates:
    snake = Turtle(shape="square")
    snake.color("white")
    snake.goto(coordinate)