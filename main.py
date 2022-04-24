import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

game_on = True
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=snake.move_up)
screen.onkey(key="Down", fun=snake.move_down)
screen.onkey(key="Left", fun=snake.turn_left)
screen.onkey(key="Right", fun=snake.turn_right)

while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.snake_body[0].distance(food) < 15:
        food.refresh()
        scoreboard.score_track()
        snake.extend()

    if snake.snake_body[0].xcor() > 290 or snake.snake_body[0].xcor() < -290:
        snake.reset()
        scoreboard.reset_game()
    elif snake.snake_body[0].ycor() > 290 or snake.snake_body[0].ycor() < -290:
        snake.reset()
        scoreboard.reset_game()

    for segment in snake.snake_body[1:]:
        if snake.snake_body[0].distance(segment) < 10:
            scoreboard.reset_game()


screen.exitonclick()
