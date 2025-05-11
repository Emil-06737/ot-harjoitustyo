import pygame


class Loop():
    """Luokka, joka vastaa pelin käyttöliittymän silmukasta.
    """

    def __init__(self, displayer, occurence_sequence, cell_size, grid, timer):
        """Konstruktori, joka luo silmukan.

        Args:
            displayer: Näytön päivittäjä.
            occurence_sequence: Tapahtumien ylläpitäjä.
            cell_size: Solun koko.
            grid: Pelin sovelluslogiikka.
            timer: Ajastin.
        """

        self._displayer = displayer
        self._occurence_sequence = occurence_sequence
        self._cell_size = cell_size
        self._grid = grid
        self._timer = timer

    def _manage_occurences(self):
        """Käsittelee tapahtumat.

        Returns:
            False, jos peli on lopetettu, muulloin True.
        """

        for occurence in self._occurence_sequence.retrieve():
            if occurence.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                self._grid.add(pos[0] // self._cell_size,
                               pos[1] // self._cell_size)
            if occurence.type == pygame.KEYDOWN:
                if occurence.key == pygame.K_F1:
                    self._displayer.toggle_info()
                if occurence.key == pygame.K_F2:
                    self._grid.reset()
            if occurence.type == pygame.QUIT:
                return False
        return True

    def begin(self):
        """Käynnistää silmukan.
        """

        while True:
            if self._manage_occurences() is False:
                break
            self._displayer.display()
            self._timer.update()
