from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(5, 1)
        self.penup()
        self.goto(position)

    def go_up(self):
        new_y = self.ycor() + 20
        if self.ycor() == 280:
            self.goto(self.xcor(), self.ycor() - 20)
        else:
            self.goto(self.xcor(), self.ycor() + 20)

    def go_down(self):
        new_y = self.ycor() - 20
        if self.ycor() == -280:
            self.goto(self.xcor(), self.ycor() + 20)
        else:
            self.goto(self.xcor(), self.ycor() - 20)
