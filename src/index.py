import os
import pygame
from grid import Grid
from ui.displayer import Displayer
from ui.occurence_sequence import OccurenceSequence
from ui.loop import Loop
from ui.timer import Timer

CELL_SIZE = 50

def main():
    size, length = get_setting_variables()
    display = pygame.display.set_mode((size * CELL_SIZE, size * CELL_SIZE))
    pygame.display.set_caption("Ristinolla")
    grid = Grid(size, CELL_SIZE, length)
    displayer = Displayer(grid, display)
    occurence_sequence = OccurenceSequence()
    timer = Timer()
    loop = Loop(displayer, occurence_sequence, CELL_SIZE, grid, timer)
    pygame.init()
    loop.begin()

def get_setting_variables():
    try:
        size = int(os.environ["SIZE"])
    except KeyError:
        size = 13
    try:
        length = int(os.environ["LENGTH"])
    except KeyError:
        length = 5
    return size, length

if __name__ == "__main__":
    main()
