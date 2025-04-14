import pygame
from grid import Grid
from displayer import Displayer
from occurence_sequence import OccurenceSequence
from loop import Loop

SIZE = 3
CELL_SIZE = 50

def main():
    display = pygame.display.set_mode((SIZE * CELL_SIZE, SIZE * CELL_SIZE))
    pygame.display.set_caption("Ristinolla")
    grid = Grid(SIZE, CELL_SIZE)
    displayer = Displayer(grid, display)
    occurence_sequence = OccurenceSequence()
    loop = Loop(displayer, occurence_sequence, CELL_SIZE, grid)
    pygame.init()
    loop.begin()

if __name__ == "__main__":
    main()
