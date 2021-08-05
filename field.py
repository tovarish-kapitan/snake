import numpy as np
import config as c
import pygame

from parts import Brick, Apple


class Field:
    def __init__(self, scr):
        self.scr = scr
        self.nx = c.nx
        self.ny = c.ny

        self.brick_map = np.zeros([self.nx, self.ny])
        self.brick_map.astype(int)
        self.bricks = []

        self.apple_map = np.zeros([self.nx, self.ny])
        self.apple_map.astype(int)
        self.apples = []

        self.meat_map = np.zeros([self.nx, self.ny])
        self.meat_map.astype(int)

    def set_frame(self, width):
        self.brick_map[width, width:self.ny-width] = 1
        self.brick_map[self.nx-width-1, width:self.ny-width] = 1
        self.brick_map[width:self.nx-width, width] = 1
        self.brick_map[width:self.nx-width, self.ny-width-1] = 1
        self.init_bricks()
        self.draw_bricks()

    def init_bricks(self):
        for x in range(self.nx):
            for y in range(self.ny):
                if self.brick_map[x, y] == 1:
                    brick = Brick(x, y, c.black, self.scr)
                    self.bricks.append(brick)

    def spawn_random_apples(self, n):
        for i in range(n):
            x = np.random.randint(0, high=self.nx)
            y = np.random.randint(0, high=self.ny)
            while self.brick_map[x, y] == 1:
                x = np.random.randint(0, high=self.nx)
                y = np.random.randint(0, high=self.ny)
            apple = Apple(x, y, c.red, self.scr)
            self.apples.append(apple)
            self.apple_map[x, y] += 1
            apple.draw()

    def draw_bricks(self):
        for brick in self.bricks:
            brick.draw()

    def draw_apples(self):
        for apple in self.apples:
            apple.draw()


if __name__ == '__main__':
    import time

    pygame.init()
    pygame.display.set_caption("snake v1.0")
    screen = pygame.display.set_mode((c.screen_width, c.screen_height), pygame.HWSURFACE)
    screen.fill(c.gray)

    t = Field(screen)
    t.set_frame(2)
    pygame.display.flip()
    pygame.display.update()
    time.sleep(3)

    t.spawn_random_apples(5)
    pygame.display.flip()
    pygame.display.update()
    time.sleep(3)
