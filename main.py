from turtle import Screen
import time
from snake import Snake
from food import Food

# screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("Snake Game")
screen.tracer(0)

# create objects
snake = Snake()
food = Food()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    time.sleep(0.2)
    screen.update()
    snake.move()

    #Ditect food collision
    if snake.head.distance(food) < 15 :
        food.refresh()





























screen.exitonclick()




