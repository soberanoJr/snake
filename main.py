from turtle import Screen
from food import Food
from snake import Snake
import time


screen = Screen()
snake = Snake()
food = Food()
play = True

screen.setup(width=1.0, height=1.0)
screen.bgcolor("black")
screen.title("===+" * 5 + "===:> snake")
screen.tracer(0)
screen.listen()
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")


while play:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
