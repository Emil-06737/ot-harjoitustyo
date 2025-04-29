import os
import pygame

class Letter(pygame.sprite.Sprite):
    """Luokka, jolla luodaan spritejä, jotka vastaavat pelaajien merkkejä.

    Args:
        pygame: Pygame.

    Attributes:
        image: Spriten kuva.
        rect: Pygamen Rect olio, jossa on koordinaatit.
    """

    def __init__(self, letter, x, y, color="black"):
        """Luokan konstruktori, jolla luodaan ruutu, jossa on kirjain.

        Args:
            letter: Kirjain.
            x: X-koordinaatti
            y: Y-koordinaatti
            color (str, optional): Kirjaimen väri. Defaults to "black".
        """

        super().__init__()
        self.image = pygame.image.load(
            os.path.join(os.path.dirname(__file__), "..", "assets", color + " " + letter + ".png")
        )
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
