from pygame.locals import *
import pygame
from player import Player
from computer import Computer

class App:
    paddle_width = 10
    paddle_height = 30
    ball_size = 10

    def __init__(self):
        self.window_width = 600
        self.window_height = 400
        self.all_sprites_list = pygame.sprite.Group()
        self._running = True
        self._screen = None

    def init(self):
        pygame.init()
        pygame.key.set_repeat(100, 100)
        self.running = True
        self._screen = pygame.display.set_mode((self.window_width,
                                                self.window_height), pygame.HWSURFACE)
        pygame.display.set_caption("Pong")

        self.player = Player(self.window_width/10, self.window_height/2, 
                                self.paddle_width, self.paddle_height)
        self.computer = Computer(self.window_width - self.window_width/10, 
                            self.window_height/2, self.paddle_width, self.paddle_height)
        self.all_sprites_list.add(self.player.paddle)
        self.all_sprites_list.add(self.computer.paddle)
    
    def exit(self):
        self._running = False

    def render(self):
        self._screen.fill((0, 0, 0))
        self.all_sprites_list.draw(self._screen)
        pygame.display.flip()
    
    def cleanup(self):
        pygame.quit()
    
    def execute(self):
        if self.init() is False:
            self._running = False
        while self._running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        self.player.move_down()
                    if event.key == pygame.K_UP:
                        self.player.move_up()
            self.render()
        self.cleanup()

if __name__ == "__main__":
    app = App()
    app.execute()