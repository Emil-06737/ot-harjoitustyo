import pygame

class Timer():
    def __init__(self):
        self._timer = pygame.time.Clock()

    def update(self, framerate=60):
        self._timer.tick(framerate)