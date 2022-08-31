from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)

    def finish_line_check(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False

    def starting_line_position(self):
        self.goto(STARTING_POSITION)


    def up(self):
        self.forward(MOVE_DISTANCE)
