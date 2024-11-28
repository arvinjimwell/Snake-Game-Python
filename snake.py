from turtle import Turtle, Screen

UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake(Turtle):
    def __init__(self, parent:'Snake'=None):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.parent = parent
        if type(self.parent) is Snake:
            self.goto(x=parent.pos()[0], y=parent.pos()[1])
            self.child = None
        else:
            self.child = Snake(parent=self)
            self.child.make_child()

    def make_child(self):
        self.child = Snake(parent=self)

    def extend(self):
        tmp_child = self.child
        while type(tmp_child.child) is Snake:
            tmp_child = tmp_child.child

        tmp_child.make_child()


    def move(self):
        if type(self.child) == Snake:
            self.child.move()

        if type(self.parent) != Snake:
            self.forward(20)
        else:
            self.goto(self.parent.pos()[0], self.parent.pos()[1])

    def eat_self(self):
        tmp_child = self.child
        while type(tmp_child ) is Snake:
            if self.distance(tmp_child) < 10:
                return True

            tmp_child = tmp_child.child

        return False


    def move_up(self):
        if self.heading() != DOWN:
            self.setheading(UP)

    def move_right(self):
        if self.heading() != LEFT:
            self.setheading(RIGHT)

    def move_left(self):
        if self.heading() != RIGHT:
            self.setheading(LEFT)

    def move_down(self):
        if self.heading() != UP:
            self.setheading(DOWN)