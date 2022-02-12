import pygame
from segment import Segment
import config as c


class Snake:
    def __init__(self, x, y, direction, field, start_energy):
        self.direction = direction
        self.field = field

        self.stack = []
        head = Segment(x, y, self.direction)
        self.stack.append(head)
        self.energy = start_energy
        self.field.incr_meat(x, y)

    def step(self):
        j = len(self.stack) - 1
        ass = self.stack[j]
        self.field.decr_meat(ass.x, ass.y)
        while j != 0:
            self.stack[j].set_direction(self.stack[j - 1].direction)
            self.stack[j].x = self.stack[j - 1].x
            self.stack[j].y = self.stack[j - 1].y
            j -= 1
        self.stack[0].set_direction(self.direction)
        x = self.stack[0].x + self.stack[0].dx
        y = self.stack[0].y + self.stack[0].dy
        self.stack[0].x = x
        self.stack[0].y = y
        self.field.incr_meat(x, y)

    def grow(self):
        x, y = self.track_xy()
        ass = Segment(x, y, self.stack[-1].direction)
        self.stack.append(ass)
        self.field.incr_meat(x, y)

    def self_intersection(self):
        x = self.head_x()
        y = self.head_y()
        for seg in self.stack[2:-1]:
            if seg.x == x and seg.y == y:
                return True
        return False

    def shrink(self):
        x = self.stack[-1].x
        y = self.stack[-1].y
        self.field.decr_meat(x, y)
        self.stack.pop(-1)

    def head_x(self):
        return self.stack[0].x

    def head_y(self):
        return self.stack[0].y

    def set_direction(self, direction):
        if self.direction == 1 and direction == 3:
            return
        if self.direction == 3 and direction == 1:
            return
        if self.direction == 2 and direction == 0:
            return
        if self.direction == 0 and direction == 2:
            return
        self.direction = direction

    def incr_energy(self, energy):
        self.energy += energy

    def decr_energy(self, energy):
        self.energy -= energy

    def __len__(self):
        return len(self.stack)

    def turn_left(self):
        self.direction = (self.direction + 1) % 4

    def turn_right(self):
        self.direction = (self.direction - 1) % 4

    def die(self):
        for seg in self.stack:
            x = seg.x
            y = seg.y
            self.field.decr_meat(x, y)
            # self.field.meat_map[x, y] = 0
            if self.field.brick_map[x, y] == 0:
                self.field.apple_map[x, y] = 1

    def checkout_body(self):
        for seg in self.stack:
            x = seg.x
            y = seg.y
            if self.field.meat_map[x, y] == 0:
                self.field.meat_map[x, y] = 1

    def track_xy(self):
        x = self.stack[-1].x - self.stack[-1].dx
        y = self.stack[-1].y - self.stack[-1].dy
        return x, y


if __name__ == "__main__":
    pass
