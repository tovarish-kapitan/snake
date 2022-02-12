import numpy as np
import config as c
import pygame
from snake import Snake
from field import Field


class SmartSnake(Snake):
    def __init__(self, x, y, direction, field, start_energy):
        Snake.__init__(self, x, y, direction, field, start_energy)
        self.vis_r = 5
        r = self.vis_r
        self.apple_brain_right = np.zeros(shape=[2*r+1, 2*r+1])
        self.apple_brain_forward = np.zeros(shape=[2*r+1, 2*r+1])
        self.apple_brain_left = np.zeros(shape=[2*r+1, 2*r+1])
        self.block_brain_right = np.zeros(shape=[2*r+1, 2*r+1])
        self.block_brain_forward = np.zeros(shape=[2*r+1, 2*r+1])
        self.block_brain_left = np.zeros(shape=[2*r+1, 2*r+1])

    def set_default_brains(self):
        r = self.vis_r
        self.apple_brain_right[r, r+1:2*r+2] = list(range(r, 0, -1))
        self.apple_brain_forward[0:r, r] = list(range(1, r+1))
        self.apple_brain_left[r, 0:r] = list(range(1, r+1))

        self.block_brain_right[r, r+1] = -20
        self.block_brain_forward[r-1, r] = -20
        self.block_brain_left[r, r-1] = -20

    def make_decision(self):
        a_view = self.map_view(self.field.apple_map)
        b_view = self.map_view(self.field.brick_map)
        m_view = self.map_view(self.field.meat_map)
        b_view = b_view + m_view
        right = np.sum(a_view*self.apple_brain_right) + np.sum(b_view*self.block_brain_right)
        forward = np.sum(a_view*self.apple_brain_forward) + np.sum(b_view*self.block_brain_forward)
        left = np.sum(a_view*self.apple_brain_left) + np.sum(b_view*self.block_brain_left)
        if forward >= left and forward >= right:
            # print('forward')
            pass
        elif right >= left:
            # print('right')
            self.turn_right()
        else:
            # print('left')
            self.turn_left()

    def map_view(self, mp):
        r = self.vis_r
        x = self.head_x()
        y = self.head_y()
        a = mp[x-r:x+r+1, y-r:y+r+1]
        a = np.transpose(a)
        k = 2-self.direction
        a = np.rot90(a, k)
        return a

    def divide(self):
        ass = self.stack[-1]
        new_snake = SmartSnake(ass.x, ass.y, ass.direction, self.field, self.energy // 2)
        new_snake.set_direction((ass.direction+2) % 4)
        self.shrink()
        for i in range(4):
            ass = self.stack[-1]
            seg = ass
            seg.set_direction((ass.direction+2) % 4)
            new_snake.stack.append(seg)
            self.shrink()
        self.energy = self.energy // 2
        new_snake.checkout_body()
        self.checkout_body()
        new_snake.set_default_brains()
        return new_snake


if __name__ == "__main__":

    pygame.init()
    pygame.display.set_caption("snake v1.0")
    screen = pygame.display.set_mode((c.screen_width, c.screen_height), pygame.HWSURFACE)

    field = Field()
    field.set_frame(5)
    snake = SmartSnake(5, 10, 3, field)
    snake.set_default_brains()

    # field.incr_apple(11, 10)
    # field.incr_apple(12, 10)
    snake.make_decision()
    print(snake.direction)

    pix_arr = field.render_field()
    pygame.surfarray.blit_array(screen, pix_arr)
    pygame.display.update()

    import time
    time.sleep(10)



