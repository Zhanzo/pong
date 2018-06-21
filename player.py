from paddle import Paddle

class Player:
    #self.y_change = 0

    def __init__(self, posX, posY, width, height):
        self.paddle = Paddle(posX, posY, width, height)

    def update(self):
        #self.paddle.rect.y += self.y_change
        pass
    def move_up(self):
        #self.y_change = -10
        self.paddle.rect.y -= 10
    
    def move_down(self):
        #self.y_change = 10
        self.paddle.rect.y += 10
