import time
from turtle import Screen
from food import Food
from snake import Snake
from score import Score


screen = Screen()
snake = Snake()
food = Food()
score = Score()
play = True

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("SNAKE")
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
        snake.extend()
        score.count()

    # detect collision with wall
    if snake.head.xcor() > 400 or snake.head.xcor() < -400 or snake.head.ycor() > 300 or snake.head.ycor() < -300:
        play = False
        score.game_over()

    # detect collision with tail
    for segment in snake.segments[1:]:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            play = False
            score.game_over()


screen.exitonclick()