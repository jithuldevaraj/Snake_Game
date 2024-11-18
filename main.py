from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

# screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("Snake Game")
screen.tracer(0)

# create objects
snake = Snake()
food = Food()
scoreboard = ScoreBoard()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    snake.move()

    #Ditect food collision
    if snake.head.distance(food) < 15 :
        food.random_food()
        scoreboard.increase_score()
        snake.extend()

    #Ditect collisions with the wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    #Ditect collision with Tail
    for segment in snake.segment:
        if segment == snake.head:
            pass

        elif snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()






























screen.exitonclick()




