from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position, key_1, key_2):
        super().__init__()
        self.goto(position)
        self.color("white")
        self.penup()
        self.shape("square")
        self.shapesize(5, 1)
        self.screen.listen()
        self.screen.onkeypress(key=key_1, fun=self.move_up)
        self.screen.onkeypress(key=key_2, fun=self.move_down)

    def move_up(self):
        if self.ycor() < 240:
            new_y = self.ycor() + 20
            self.goto(self.xcor(), new_y)

    def move_down(self):
        if self.ycor() > -240:
            new_y = self.ycor() - 20
            self.goto(self.xcor(), new_y)
