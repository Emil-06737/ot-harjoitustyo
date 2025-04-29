import os
import pygame

class Letter(pygame.sprite.Sprite):
    def __init__(self, letter, x, y, color="black"):
        super().__init__()
        self.image = pygame.image.load(
            os.path.join(os.path.dirname(__file__), "..", "assets", color + " " + letter + ".png")
        )
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
