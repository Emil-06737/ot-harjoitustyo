import os
import pygame

class O(pygame.sprite.Sprite):
    def __init__(self, x, y, color="black"):
        super().__init__()
        self.image = pygame.image.load(
            os.path.join(os.path.dirname(__file__), "..", "assets", color + " o.png")
        )
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
