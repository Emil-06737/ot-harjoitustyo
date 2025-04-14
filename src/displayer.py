import pygame

class Displayer:
    def __init__(self, grid, display):
        self._grid = grid
        self._display = display

    def display(self):
            self._grid.all_sprites.draw(self._display)
            pygame.display.update()