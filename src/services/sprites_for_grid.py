from dataclasses import dataclass
import pygame


@dataclass
class SpritesForGrid:
    """Luokka, johon on tallennettu sovelluslogiikan käyttämät spritet.

    Attributes:
        empties: Tyhjien spritejen ryhmä.
        letters: Kirjain spritejen ryhmä.
        reds: Punaisten spritejen ryhmä.
        all_sprites: Kaikkien spritejen ryhmä.
    """

    empties: pygame.sprite.Group = pygame.sprite.Group()
    letters: pygame.sprite.Group = pygame.sprite.Group()
    reds: pygame.sprite.Group = pygame.sprite.Group()
    all_sprites: pygame.sprite.Group = pygame.sprite.Group()
