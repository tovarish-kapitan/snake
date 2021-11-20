import numpy as np
import config as c
import pygame


class Field:
    def __init__(self):
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
        self.brick_map[0:width, :] = 1
        self.brick_map[self.nx-width:, :] = 1
        self.brick_map[:, 0:width] = 1
        self.brick_map[:, self.ny-width:] = 1

    def spawn_random_apples(self, n):
        for i in range(n):
            x = np.random.randint(0, high=self.nx)
            y = np.random.randint(0, high=self.ny)
            while self.brick_map[x, y] == 1:
                x = np.random.randint(0, high=self.nx)
                y = np.random.randint(0, high=self.ny)
            self.incr_apple(x, y)

    def incr_apple(self, x, y):
        self.apple_map[x, y] += 1

    def decr_apple(self, x, y):
        self.apple_map[x, y] = 0

    def incr_meat(self, x, y):
        self.meat_map[x, y] += 1

    def decr_meat(self, x, y):
        self.meat_map[x, y] -= 1

    def render_field(self):
        brick_arr = (self.brick_map > 0) * c.black
        apple_arr = (self.apple_map > 0) * c.red
        meat_arr = (self.meat_map > 0) * c.green
        arr = brick_arr + apple_arr + meat_arr
        ground_arr = (arr == 0) * c.gray
        arr = arr + ground_arr
        square = np.ones(shape=[c.square_size, c.square_size])
        square.astype(int)
        pix = np.kron(arr, square)
        return pix


if __name__ == '__main__':
    from snake import Snake
    pygame.init()
    pygame.display.set_caption("snake v1.0")
    scr = pygame.display.set_mode((c.screen_width, c.screen_height), pygame.HWSURFACE)
    field = Field()
    field.set_frame(1)
    field.apple_map[3, 3] = 1
    field.meat_map[5, 5] = 1
    snake = Snake(7, 7, 1, field)
    pix_arr = field.render_field()
    pygame.surfarray.blit_array(scr, pix_arr)
    pygame.display.flip()
    pygame.display.update()

    snake.step()
    pix_arr = field.render_field()
    pygame.surfarray.blit_array(scr, pix_arr)
    pygame.display.flip()
    pygame.display.update()

    import time
    time.sleep(3)


