import pygame

class Input(object):
    def __int__(self):
        self.quit = False
        def update(self):
            if event.type == pygame.QUIT:
                self.quit = True