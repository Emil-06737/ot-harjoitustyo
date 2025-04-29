import pygame

class Displayer:
    """Luokka, joka vastaa näytön päivittämisestä.
    """

    def __init__(self, grid, display):
        """Luokan konstruktori, joka luo näytön päivittäjän.

        Args:
            grid: Pelin sovelluslogiikasta vastaava luokka.
            display: Näyttö.
        """

        self._grid = grid
        self._display = display

    def display(self):
        """Päivittää näytön.
        """

        self._grid.all_sprites.draw(self._display)
        pygame.display.update()
