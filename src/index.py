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
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    grid.add(0,0)
                if event.key == pygame.K_2:
                    grid.add(1,0)
                if event.key == pygame.K_3:
                    grid.add(2,0)
                if event.key == pygame.K_4:
                    grid.add(0,1)
                if event.key == pygame.K_5:
                    grid.add(1,1)
                if event.key == pygame.K_6:
                    grid.add(2,1)
                if event.key == pygame.K_7:
                    grid.add(0,2)
                if event.key == pygame.K_8:
                    grid.add(1,2)
                if event.key == pygame.K_9:
                    grid.add(2,2)
            if event.type == pygame.QUIT:
                running = False
            grid.all_sprites.draw(display)
            pygame.display.update()
    pygame.quit()    

if __name__ == "__main__":
    main()