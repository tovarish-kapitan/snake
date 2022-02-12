import numpy as np


class Field:
    def __init__(self, conf):
        self.conf = conf
        self.nx = self.conf.nx
        self.ny = self.conf.ny

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
            self.set_apple(x, y)

    def set_apple(self, x, y):
        self.apple_map[x, y] += 1

    def remove_apple(self, x, y):
        self.apple_map[x, y] = 0

    def incr_meat(self, x, y):
        self.meat_map[x, y] += 1

    def decr_meat(self, x, y):
        if self.meat_map[x, y] > 0:
            self.meat_map[x, y] -= 1
        else:
            pass

    def render_field(self):
        brick_arr = (self.brick_map > 0) * self.conf.black
        apple_arr = (self.apple_map > 0) * self.conf.red
        meat_arr = (self.meat_map > 0) * self.conf.green

        arr = brick_arr + apple_arr + meat_arr
        ground_arr = (arr == 0) * self.conf.gray
        arr = arr + ground_arr
        square = np.ones(shape=[self.conf.square_size, self.conf.square_size])
        square.astype(int)
        pix = np.kron(arr, square)
        return pix
