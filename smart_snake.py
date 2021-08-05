import numpy as np
import config as c
import pygame
from snake import Snake


class SmartSnake(Snake):
    def __init__(self, x, y, direction, col, scr):
        Snake.__init__(self, x, y, direction, col, scr)
        self.vis_r = 3
        r = self.vis_r
        self.apple_brain_right = np.zeros(shape=[2*r+1, 2*r+1])
        self.apple_brain_forward = np.zeros(shape=[2*r+1, 2*r+1])
        self.apple_brain_left = np.zeros(shape=[2*r+1, 2*r+1])
        self.block_brain_right = np.zeros(shape=[2*r+1, 2*r+1])
        self.block_brain_forward = np.zeros(shape=[2*r+1, 2*r+1])
        self.block_brain_left = np.zeros(shape=[2*r+1, 2*r+1])

    def set_default_brains(self):
        r = self.vis_r
        self.apple_brain_right[r, r+1:2*r+2, 0] = list(range(r, 0, -1))
        self.apple_brain_forward[0:r, r, 1] = list(range(1, r+1))
        self.apple_brain_left[r, 0:r, 2] = list(range(1, r+1))

        self.block_brain_right[r, r+1, 2] = -10
        self.block_brain_forward[r-1, r, 1] = -10
        self.block_brain_left[r, r-1, 0] = -10

    def make_decision(self, apple_map, brick_map, meat_map):
        a_view = self.map_view(apple_map)
        b_view = self.map_view(brick_map)
        m_view = self.map_view(meat_map)
        b_view = b_view + m_view
        right = np.sum(a_view*self.apple_brain_right) + np.sum(a_view*self.apple_brain_right)
        forward = np.sum(a_view*self.apple_brain_forward) + np.sum(a_view*self.apple_brain_forward)
        left = np.sum(a_view*self.apple_brain_left) + np.sum(a_view*self.apple_brain_left)
        if forward >= left and forward >= right:
            print('forward')
            pass
        elif right >= left:
            print('right')
            self.turn_right()
        else:
            print('left')
            self.turn_left()


    def map_view(self, mp):
        r = self.vis_r
        x = self.head_x()
        y = self.head_y()
        a = mp[x-r:x+r+1, x-r:x+r+1]
        k = 2-self.direction
        a = np.rot90(a, k)
        return a


if __name__ == "__main__":

    pygame.init()
    pygame.display.set_caption("snake v1.0")
    screen = pygame.display.set_mode((c.screen_width, c.screen_height), pygame.HWSURFACE)
    snake = SmartSnake(4, 4, 1, c.green, screen)
    snake.set_default_brains()
    # print(snake.apple_brain[:, :, 0])
    # print(snake.apple_brain[:, :, 1])
    # print(snake.apple_brain[:, :, 2])
    # print(snake.block_brain[:, :, 0])
    # print(snake.block_brain[:, :, 1])
    # print(snake.block_brain[:, :, 2])
    map = np.zeros(shape=[10, 10])
    map[5,5] = 1
    print(snake.map_view(map))



