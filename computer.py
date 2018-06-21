from paddle import Paddle

class Computer:
    def __init__(self, posX, posY, width, height):
        self.paddle = Paddle(posX, posY, width, height)
        