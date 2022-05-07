from turtle import Screen
from snake import Snake
import time


screen = Screen()
screen.setup(width=1.0, height=1.0)
screen.bgcolor("black")
screen.title("===+" * 5 + "===:> snake")
screen.tracer(0)
snake = Snake()
play = True


while play:
    screen.update()
    time.sleep(0.1)

    snake.move()