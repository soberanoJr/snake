from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(width=1.0, height=1.0)
screen.bgcolor("black")
screen.tracer(0)
screen.title("===+" * 5 + "===:> snake")
coordinates = [(0, 0), (-20, 0), (-40, 0)]
tail = []
play = True

for coordinate in coordinates:
    snake = Turtle(shape="square")
    snake.color("white")
    snake.penup()
    snake.goto(coordinate)
    tail.append(snake)

while play:
    screen.update()
    time.sleep(0.1)

    for segment in range(len(tail) -1, 0, -1):
        x = tail[segment - 1].xcor()
        y = tail[segment - 1].ycor()
        tail[segment].goto(x, y)
    tail[0].forward(20)