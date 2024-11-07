from turtle import Turtle, Screen
import time

# screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("Snake Game")

# snake body
starting_position = [(0, 0), (-20, 0), (-40, 0)]
segment = []

screen.tracer(0)

for position in starting_position:
    new_segment = Turtle(shape='square')
    new_segment.penup()
    new_segment.color('white')
    new_segment.setposition(position)
    segment.append(new_segment)

game_is_on = True
while game_is_on:
    time.sleep(0.2)
    screen.update()
    for seg_num in range((len(segment) - 1), 0, -1):
        x_cor = segment[seg_num - 1].xcor()
        y_cor = segment[seg_num - 1].ycor()
        segment[seg_num].setposition(x_cor, y_cor)
    segment[0].forward(20)



























screen.exitonclick()




