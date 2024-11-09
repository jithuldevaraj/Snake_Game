from turtle import Screen
import time
from snake import Snake

# screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("Snake Game")

# create snake class
screen.tracer(0)
snake = Snake()


game_is_on = True
while game_is_on:
    time.sleep(0.2)
    screen.update()
    snake.move()




























screen.exitonclick()




