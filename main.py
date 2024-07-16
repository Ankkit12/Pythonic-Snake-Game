from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

"""This is screen setup"""
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)


snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # To detect collision with the food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # detect collision with the wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.s_reset()

    # detect collision with the tail
    # if snake head collides with its tail
    # trigger game over
    new = snake.squares[1:]
    for square in new:
        if square == snake.head:
            pass
        elif snake.head.distance(square) < 10:
            scoreboard.reset()
            snake.s_reset()




screen.exitonclick()
