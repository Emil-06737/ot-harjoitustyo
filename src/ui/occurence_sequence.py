import pygame

class OccurenceSequence:
    """Luokka tapahtumien hakemiseen.
    """

    def retrieve(self):
        """Hakee tapahtumalistan.

        Returns:
            Eventlist
        """

        return pygame.event.get()
