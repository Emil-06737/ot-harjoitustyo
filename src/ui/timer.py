import pygame


class Timer():
    """Luokka pelin ajoittamiseen.
    """

    def __init__(self):
        """Luokan konstruktori, joka luo ajastimen
        """

        self._timer = pygame.time.Clock()

    def update(self, framerate=60):
        """Päivittää ajastimen.

        Args:
            framerate (int, optional): Kuvataajuus. Defaults to 60.
        """

        self._timer.tick(framerate)
