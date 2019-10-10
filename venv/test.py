from turtle import Turtle, Screen

### CONSTANTS ###
# Definition of constant values
WINSIZE_WIDTH = 1920
WINSIZE_HEIGHT = 1024
GAMESIZE_WIDTH = int(WINSIZE_WIDTH * 0.9)
GAMESIZE_HEIGHT = int(WINSIZE_HEIGHT * 0.9)
GAMEMARGIN_WIDTH = (WINSIZE_WIDTH - GAMESIZE_WIDTH) / 2
GAMEMARGIN_HEIGHT = (WINSIZE_HEIGHT - GAMESIZE_HEIGHT) / 2

### CLASSES ###
class GameItem(Turtle):
    "This class is the main class for all objects"
    # Constructor (by now it just call the parent's constructor
    def __init__(self):
        Turtle.__init__(self)


    def move(self):
        self.forward(int(self.sp))
        if self.xcor() > (WINSIZE_WIDTH - GAMEMARGIN_WIDTH):
            self.setx(WINSIZE_WIDTH - GAMEMARGIN_WIDTH)
            self.setheading(180-self.heading())
        if self.xcor() < (GAMEMARGIN_WIDTH):
            self.setx(GAMEMARGIN_WIDTH)
            self.setheading(180-self.heading())
        if self.ycor() > (WINSIZE_HEIGHT - GAMEMARGIN_HEIGHT):
            self.sety(WINSIZE_HEIGHT - GAMEMARGIN_HEIGHT)
            self.setheading(360 - self.heading())
        if self.ycor() < (GAMEMARGIN_HEIGHT):
            self.sety(GAMEMARGIN_HEIGHT)
            self.setheading(360 - self.heading())
    # Speed value can range from 0 to 10, with 1 the lowest and 10 the highest

    def turnLeft(self):
        self.setheading(self.heading()+10)
        if self.sp != 0:
            self.move()

    def turnRight(self):
        self.setheading(self.heading()-10)
        if self.sp != 0:
            self.move()

    def increaseSpeed(self):
        if self.sp < 10:
            self.sp = self.sp+1


    def decreaseSpeed(self):
        if self.sp > -10:
            self.sp = self.sp-1

    def stopIncreaseSpeed(self):
        self.released = True
    released = False
    sp = 0

class SpaceShip(GameItem):
    "This class defines a Space Ship and its properties"
    # Constructor
    def __init__(self, param_color="White"):
        Turtle.__init__(self)
        #self.color(param_color)
    #pass
    #self.shape("Triangle")


### MAIN ###
window = Screen()
window.setup(0.5,0.75,0,0)
window.screensize(WINSIZE_WIDTH,WINSIZE_HEIGHT,"White")
window.setworldcoordinates(0,0,WINSIZE_WIDTH,WINSIZE_HEIGHT)
window.title("Chasers")

spaceShip = SpaceShip()

window.onkeypress(spaceShip.turnLeft, "Left")
window.onkeypress(spaceShip.turnRight,"Right")
window.onkeypress(spaceShip.increaseSpeed,"Up")
window.onkeypress(spaceShip.decreaseSpeed,"Down")
window.listen()

spaceShip.setpos(GAMEMARGIN_WIDTH, GAMESIZE_HEIGHT)
while True:
    spaceShip.move()