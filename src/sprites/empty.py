import pygame
import os

class Empty(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load(
            os.path.join(os.path.dirname(__file__), "..", "assets", "empty.png")
        )
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
