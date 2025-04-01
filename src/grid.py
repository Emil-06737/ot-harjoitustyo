import pygame
from sprites.empty import Empty
from sprites.x import X
from sprites.o import O

class Grid:
    def __init__(self, size, cell_size):
        self.x_turn = True
        self.size = size
        self.cell_size = cell_size
        self.empties = pygame.sprite.Group()
        self.xs = pygame.sprite.Group()
        self.os = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()
        self._init_grid()
        self._add_empties()
        self._update_all_sprites()

    def add(self, x, y):
        if self.x_turn:
            self._add_x(x, y)
        else:
            self._add_o(x, y)

    def _add_x(self, x, y):
        if not self.grid[y][x]:
            new = X(x*self.cell_size, y*self.cell_size)
            self.xs.add(new)
            self._update_all_sprites()
            self.grid[y][x] = 1
            self.x_turn = False

    def _add_o(self, x, y):
        if not self.grid[y][x]:
            new = O(x*self.cell_size, y*self.cell_size)
            self.os.add(new)
            self._update_all_sprites()
            self.grid[y][x] = 2
            self.x_turn = True

    def _add_empties(self):
        for y in range(self.size):
            for x in range(self.size):
                self.empties.add(Empty(x*self.cell_size, y*self.cell_size))

    def _init_grid(self):
        self.grid = []
        for _ in range(self.size):
            self.grid.append(self.size*[0])

    def _update_all_sprites(self):
        self.all_sprites.empty()
        self.all_sprites.add(
            self.empties,
            self.xs,
            self.os
        )
