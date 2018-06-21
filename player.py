from paddle import Paddle

class Player:
    def __init__(self, posX, posY, width, height):
        self.paddle = Paddle(posX, posY, width, height)

    def move_up(self):
        self.paddle.rect.y -= 10
    
    def move_down(self):
        self.paddle.rect.y += 10
