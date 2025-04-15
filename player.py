from turtle import Turtle
PLAYER_SPAWN_Y_COORDINATE = -215
FINISH_Y_COORDINATE = 270


# This creates the player
class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("arrow")
        self.speed(2)
        self.setheading(90)
        self.penup()
        self.setpos(x=0, y=-300)
        self.color("white")
        self.goto(x=0, y=PLAYER_SPAWN_Y_COORDINATE)
        self.current_player_y_position = PLAYER_SPAWN_Y_COORDINATE

    def move_up(self):
        new_y_position = self.ycor() + 5
        self.setpos(x=0, y=new_y_position)
        self.current_player_y_position = new_y_position

    def take_player_to_start(self):
        self.goto(x=0, y=PLAYER_SPAWN_Y_COORDINATE)



# This creates the finish line
# FINISH_LINE = x: from -300 -> 300, y: 270
class Finish(Turtle):
    def __init__(self):
        super().__init__()
        self.finishline_coordinate = FINISH_Y_COORDINATE
        self.hideturtle()
        self.speed(3)
        self.pendown()
        self.setpos(x=300, y=FINISH_Y_COORDINATE)
        self.color("white")
        self.goto(x=-300, y=FINISH_Y_COORDINATE)

    def blinkred(self):
        for i in range(2):
            self.color("red")
            self.color("white")
