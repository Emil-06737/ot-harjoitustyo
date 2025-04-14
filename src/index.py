import pygame
from grid import Grid

SIZE = 3
CELL_SIZE = 50

def main():
    display = pygame.display.set_mode((SIZE * CELL_SIZE, SIZE * CELL_SIZE))
    pygame.display.set_caption("Ristinolla")
    grid = Grid(SIZE, CELL_SIZE)
    pygame.init()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                grid.add(pos[0] // CELL_SIZE, pos[1] // CELL_SIZE)
            if event.type == pygame.QUIT:
                running = False
            grid.all_sprites.draw(display)
            pygame.display.update()
    pygame.quit()

if __name__ == "__main__":
    main()
