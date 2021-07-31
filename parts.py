import pygame
from essence import Essence
import numpy as np
import config as c


class Apple(Essence):
    def __init__(self, x, y, col, scr):
        self.energy = c.apple_energy
        Essence.__init__(self, x, y, col, scr)

    def draw(self):
        pygame.draw.ellipse(self.scr, self.col, (self.pix, self.piy, self.size, self.size))


class Brick(Essence):
    def __init__(self, x, y, col, scr):
        Essence.__init__(self, x, y, col, scr)

    def draw(self):
        pygame.draw.rect(self.scr, self.col, (self.pix, self.piy, self.size, self.size))


class Segment(Essence):
    def __init__(self, x, y, direction, col, scr):
        Essence.__init__(self, x, y, col, scr)
        self.direction = None
        self.dx = None
        self.dy = None
        self.set_direction(direction)

    def set_direction(self, direction):
        self.direction = direction
        self.dx = int(np.sin(0.5 * np.pi * self.direction))
        self.dy = int(np.cos(0.5 * np.pi * self.direction))

    def step(self):
        self.set_x(self.x + self.dx)
        self.set_y(self.y + self.dy)
        self.draw()

    def draw(self):
        pygame.draw.rect(self.scr, self.col, (self.pix, self.piy, self.size, self.size))


if __name__ == "__main__":
    import time

    pygame.init()
    pygame.display.set_caption("snake v1.0")
    screen = pygame.display.set_mode((c.screen_width, c.screen_height), pygame.HWSURFACE)
    screen.fill(c.gray)

    seg = Segment(0, 0, 1, c.green, screen)
    apple = Apple(1, 0, c.red, screen)
    brick = Brick(2, 0, c.black, screen)
    pygame.display.update()
    pygame.display.flip()
    time.sleep(1)

    # screen.fill(gray)
    # seg.step()
    # apple.draw()
    # brick.draw()
    # pygame.display.update()
    # pygame.display.flip()
    # time.sleep(1)
