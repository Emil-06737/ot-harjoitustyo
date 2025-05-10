import pygame
from services.grid import Grid
from ui.displayer import Displayer
from ui.occurence_sequence import OccurenceSequence
from ui.loop import Loop
from ui.timer import Timer
from configuration import SIZE, LENGTH, PLAYERS

CELL_SIZE = 50


def main():
    display = pygame.display.set_mode((SIZE * CELL_SIZE, SIZE * CELL_SIZE))
    pygame.display.set_caption("Ristinolla")
    grid = Grid(SIZE, CELL_SIZE, LENGTH, PLAYERS)
    displayer = Displayer(grid, display)
    occurence_sequence = OccurenceSequence()
    timer = Timer()
    loop = Loop(displayer, occurence_sequence, CELL_SIZE, grid, timer)
    pygame.init()
    loop.begin()


if __name__ == "__main__":
    main()
