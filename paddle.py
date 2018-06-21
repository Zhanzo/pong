from pygame.locals import *
import pygame

class Paddle(pygame.sprite.Sprite):
    def __init__(self, posX, posY, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill((255, 255, 255))

        # Make the top-left corner the passed-in location
        self.rect = self.image.get_rect()
        self.rect.x = posX
        self.rect.y = posY
    