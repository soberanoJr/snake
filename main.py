from turtle import Screen
from food import Food
from snake import Snake
from score import Score
import time


screen = Screen()
snake = Snake()
food = Food()
score = Score()
play = True

screen.setup(width=700, height=500)
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

    # detect collision with food
    if snake.head.distance(food) < 20:
        food.refresh()
        score.count()


    # detect collision with wall
    if snake.head.xcor() > 350 or snake.head.xcor() < -350 or snake.head.ycor() > 250 or snake.head.ycor() < -250:
        play = False
        score.game_over()