import pygame
from parts import Segment
import config as c


class Snake:
    def __init__(self, x, y, direction, col, scr):
        self.direction = direction
        self.col = col
        self.scr = scr

        self.stack = []
        head = Segment(x, y, self.direction, self.col, self.scr)
        self.stack.append(head)
        self.track = head
        self.energy = c.start_energy

    def step(self):
        j = len(self.stack) - 1
        self.track = self.stack[j]
        while j != 0:
            self.stack[j].set_direction(self.stack[j - 1].direction)
            self.stack[j].set_x(self.stack[j - 1].x)
            self.stack[j].set_y(self.stack[j - 1].y)
            j -= 1
        self.stack[0].set_direction(self.direction)
        x = self.stack[0].x + self.stack[0].dx
        y = self.stack[0].y + self.stack[0].dy
        self.stack[0].set_x(x)
        self.stack[0].set_y(y)

    def grow(self):
        x = self.track.x - self.track.dx
        y = self.track.y - self.track.dy
        ass = Segment(x, y, self.track.direction, self.col, self.scr)
        self.stack.append(ass)

    def self_intersection(self):
        x = self.head_x()
        y = self.head_y()
        for seg in self.stack[2:-1]:
            if seg.x == x and seg.y == y:
                return True
        return False

    def shrink(self):
        self.track = self.stack.pop(-1)

    def head_x(self):
        return self.stack[0].x

    def head_y(self):
        return self.stack[0].y

    def set_direction(self, direction):
        if self.direction == 1 and direction == 3:
            pass
        if self.direction == 3 and direction == 1:
            pass
        if self.direction == 2 and direction == 4:
            pass
        if self.direction == 4 and direction == 2:
            pass
        self.direction = direction

    def increase_hp(self, energy):
        self.energy += energy

    def decrease_hp(self, energy):
        self.energy -= energy

    def __len__(self):
        return len(self.stack)

    def draw(self):
        for seg in self.stack:
            seg.draw()


if __name__ == "__main__":
    import time

    pygame.init()
    pygame.display.set_caption("snake v1.0")
    screen = pygame.display.set_mode((c.screen_width, c.screen_height), pygame.HWSURFACE)

    screen.fill(c.gray)
    snake = Snake(0, 0, 1, c.green, screen)
    pygame.display.flip()
    pygame.display.update()
    time.sleep(1)

    screen.fill(c.gray)
    snake.grow()
    snake.draw()
    pygame.display.flip()
    pygame.display.update()
    time.sleep(1)

    screen.fill(c.gray)
    snake.step()
    snake.draw()
    pygame.display.flip()
    pygame.display.update()
    time.sleep(1)

    screen.fill(c.gray)
    snake.set_direction(2)
    snake.step()
    snake.step()
    snake.draw()
    pygame.display.flip()
    pygame.display.update()
    time.sleep(1)

    screen.fill(c.gray)
    snake.step()
    snake.draw()
    pygame.display.flip()
    pygame.display.update()
    time.sleep(2)
