from turtle import Screen, Turtle


STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP =90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:

    def __init__(self):
        self.segment = []
        self.create_snake()
        self.head = self.segment[0]

    def create_snake(self):

        for position in STARTING_POSITION:
            new_segment = Turtle(shape='square')
            new_segment.penup()
            new_segment.color('white')
            new_segment.setposition(position)
            self.segment.append(new_segment)
        return self.segment


    def move(self):
        for seg_num in range((len(self.segment) - 1), 0, -1):
            x_cor = self.segment[seg_num - 1].xcor()
            y_cor = self.segment[seg_num - 1].ycor()
            self.segment[seg_num].setposition(x_cor, y_cor)
        self.head.forward(MOVE_DISTANCE)


    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.segment[0].setheading(RIGHT)
