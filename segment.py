import pygame
import numpy as np
import config as c


class Segment:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.size = c.square_size
        self.direction = None
        self.dx = None
        self.dy = None
        self.set_direction(direction)

    def set_direction(self, direction):
        self.direction = direction
        self.dx = int(np.sin(0.5 * np.pi * self.direction))
        self.dy = int(np.cos(0.5 * np.pi * self.direction))

    def step(self):
        self.x += self.dx
        self.y += self.dy


if __name__ == "__main__":
    pass
