from turtle import Turtle
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_SPEED = 20
DIRECTIONS = [0, 90, 180, 270]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.squares = []
        self.create_snake()
        self.head = self.squares[0]

    def create_snake(self):
        """This function creates a full snake"""
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        """This function adds the square blocks to the snake body"""
        sq1 = Turtle()
        sq1.shape("square")
        sq1.color("white")
        sq1.penup()
        sq1.goto(position)
        self.squares.append(sq1)

    def s_reset(self):
        """This function resets the snake body on the screen"""
        for seg in self.squares:
            seg.goto(1000, 1000)
        self.squares.clear()
        self.create_snake()
        self.head = self.squares[0]

    def extend(self):
        """This function increases length of the snake"""
        self.add_segment(self.squares[-1].position())

    def move(self):
        """This function moves the snake block by block"""
        for seg_num in range(len(self.squares) - 1, 0, -1):
            new_x = self.squares[seg_num - 1].xcor()
            new_y = self.squares[seg_num - 1].ycor()
            self.squares[seg_num].goto(new_x, new_y)

        self.head.forward(MOVE_SPEED)

    def up(self):
        """Moves snake in up direction"""
        if self.head.heading() != DOWN:
            self.head.setheading(DIRECTIONS[1])

    def down(self):
        """Moves snake in down direction"""
        if self.head.heading() != UP:
            self.head.setheading(DIRECTIONS[3])

    def left(self):
        """Moves snake in left direction"""
        if self.head.heading() != RIGHT:
            self.head.setheading(DIRECTIONS[2])

    def right(self):
        """Moves snake in right direction"""
        if self.head.heading() != LEFT:
            self.head.setheading(DIRECTIONS[0])









