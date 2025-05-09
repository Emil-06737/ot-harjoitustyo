import os
import pygame


class Empty(pygame.sprite.Sprite):
    """Luokka, jolla luodaan spritejä, jotka vastaavat tyhjiä ruutuja.

    Args:
        pygame: Pygame.

    Attributes:
        image: Spriten kuva.
        rect: Pygamen Rect olio, jossa on koordinaatit.
    """

    def __init__(self, x, y):
        """Luokan konstruktori, jolla luodaan tyhjä ruutu.

        Args:
            x: X-koordinaatti
            y: Y-koordinaatti
        """

        super().__init__()
        self.image = pygame.image.load(
            os.path.join(os.path.dirname(__file__),
                         "..", "assets", "empty.png")
        )
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
