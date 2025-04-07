import pygame
from sprites.empty import Empty
from sprites.x import X
from sprites.o import O

class Grid:
    def __init__(self, size, cell_size, victory_requirement=3):
        self.victory_requirement = victory_requirement
        self.game_over = False
        self.x_turn = True
        self.size = size
        self.cell_size = cell_size
        self.empties = pygame.sprite.Group()
        self.xs = pygame.sprite.Group()
        self.os = pygame.sprite.Group()
        self.reds = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()
        self._init_grid()
        self._add_empties()
        self._update_all_sprites()

    def add(self, x, y):
        unnormalized_x, unnormalized_y = self._unnormalize(x, y)
        unnormalized_x = min(unnormalized_x, self.size - 1)
        unnormalized_y = min(unnormalized_y, self.size - 1)
        if self.x_turn:
            self._add_x(unnormalized_x, unnormalized_y)
        else:
            self._add_o(unnormalized_x, unnormalized_y)

    def _add_x(self, x, y):
        if not self.grid[y][x] and not self.game_over:
            new = X(x*self.cell_size, y*self.cell_size)
            self.xs.add(new)
            self._update_all_sprites()
            self.grid[y][x] = 1
            self.x_turn = False
            self._check_victory()

    def _add_o(self, x, y):
        if not self.grid[y][x] and not self.game_over:
            new = O(x*self.cell_size, y*self.cell_size)
            self.os.add(new)
            self._update_all_sprites()
            self.grid[y][x] = 2
            self.x_turn = True
            self._check_victory()

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
            self.os,
            self.reds
        )

    def _unnormalize(self, x, y):
        return (x // self.cell_size, y // self.cell_size)

    def _check_victory(self):
        if self._check_vertical_victory():
            return
        if self._check_horizontal_victory():
            return
        self._check_diagonal_victory()

    def _check_vertical_victory(self):
        for x in range(self.size):
            previous = self.grid[0][x]
            counter = 1
            current_line = [(x, 0)]
            for y in range(1, self.size):
                current_coordinates = (x, y)
                current = self.grid[current_coordinates[1]][current_coordinates[0]]
                if current == previous:
                    counter += 1
                    current_line.append(current_coordinates)
                    if counter == self.victory_requirement and current != 0:
                        self._finish_game(current_line)
                        return True
                else:
                    counter = 1
                    previous = current
                    current_line = [current_coordinates]
        return False

    def _check_horizontal_victory(self):
        for y in range(self.size):
            counter = 1
            previous = self.grid[y][0]
            current_line = [(0, y)]
            for x in range(1, self.size):
                current_coordinates = (x, y)
                current = self.grid[current_coordinates[1]][current_coordinates[0]]
                if current == previous:
                    counter += 1
                    current_line.append(current_coordinates)
                    if counter == self.victory_requirement and current != 0:
                        self._finish_game(current_line)
                        return True
                else:
                    counter = 1
                    previous = current
                    current_line = [current_coordinates]
        return False

    def _check_diagonal_victory(self):
        if self._check_descending_diagonal_victory():
            return True
        return self._check_ascending_diagonal_victory()

    def _check_descending_diagonal_victory(self):
        for y in range(self.size):
            counter = 1
            previous = self.grid[y][0]
            current_line = [(0, y)]
            for increment in range(1, self.size - y):
                current_coordinates = (increment, y + increment)
                current = self.grid[current_coordinates[1]][current_coordinates[0]]
                if current == previous:
                    counter += 1
                    current_line.append(current_coordinates)
                    if counter == self.victory_requirement and current != 0:
                        self._finish_game(current_line)
                        return True
                else:
                    counter = 1
                    previous = current
                    current_line = [current_coordinates]
        for x in range(1, self.size):
            counter = 1
            previous = self.grid[0][x]
            current_line = [(x, 0)]
            for increment in range(1, self.size - x):
                current_coordinates = (x + increment, increment)
                current = self.grid[current_coordinates[1]][current_coordinates[0]]
                if current == previous:
                    counter += 1
                    current_line.append(current_coordinates)
                    if counter == self.victory_requirement and current != 0:
                        self._finish_game(current_line)
                        return True
                else:
                    counter = 1
                    previous = current
                    current_line = [current_coordinates]
        return False

    def _check_ascending_diagonal_victory(self):
        for y in range(self.size):
            counter = 1
            previous = self.grid[y][0]
            current_line = [(0, y)]
            for increment in range(1, y + 1):
                current_coordinates = (increment, y - increment)
                current = self.grid[current_coordinates[1]][current_coordinates[0]]
                if current == previous:
                    counter += 1
                    current_line.append(current_coordinates)
                    if counter == self.victory_requirement and current != 0:
                        self._finish_game(current_line)
                        return True
                else:
                    counter = 1
                    previous = current
                    current_line = [current_coordinates]
        for x in range(1, self.size):
            counter = 1
            previous = self.grid[self.size - 1][x]
            current_line = [(x, self.size - 1)]
            for increment in range(1, self.size - x):
                current_coordinates = (x + increment, self.size - 1 - increment)
                current = self.grid[current_coordinates[1]][current_coordinates[0]]
                if current == previous:
                    counter += 1
                    current_line.append(current_coordinates)
                    if counter == self.victory_requirement and current != 0:
                        self._finish_game(current_line)
                        return True
                else:
                    counter = 1
                    previous = current
                    current_line = [current_coordinates]
        return False

    def _finish_game(self, line):
        symbol = self.grid[line[0][1]][line[0][0]]
        for coordinates in line:
            if symbol == 1:
                red_symbol = X(coordinates[0] * self.cell_size, coordinates[1] * self.cell_size, "red")
                self.reds.add(red_symbol)
            else:
                red_symbol = O(coordinates[0] * self.cell_size, coordinates[1] * self.cell_size, "red")
                self.reds.add(red_symbol)
        self._update_all_sprites()
        self.game_over = True
