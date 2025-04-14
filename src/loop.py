import pygame

class Loop():
    def __init__(self, displayer, occurence_sequence, cell_size, grid):
        self._displayer = displayer
        self._occurence_sequence = occurence_sequence
        self._cell_size = cell_size
        self._grid = grid

    def _display(self):
        self._displayer.display()

    def _manage_occurences(self):
        for occurence in self._occurence_sequence.retrieve():
            if occurence.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                self._grid.add(pos[0] // self._cell_size, pos[1] // self._cell_size)
            if occurence.type == pygame.QUIT:
                return False
        return True

    def begin(self):
        while True:
            if self._manage_occurences() is False:
                break
            self._display()
