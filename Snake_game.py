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

for position in starting_position:
    new_segment = Turtle(shape='square')
    new_segment.penup()
    new_segment.color('white')
    new_segment.setposition(position)
    segment.append(new_segment)

game_is_on = True
while game_is_on:
    for seg in segment:
        seg.forward(20)
        time.sleep(0.1)








screen.exitonclick()