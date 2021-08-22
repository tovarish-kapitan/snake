import pygame
from segment import Segment
import config as c


class Snake:
    def __init__(self, x, y, direction, field):
        self.direction = direction
        self.field = field

        self.stack = []
        head = Segment(x, y, self.direction)
        self.stack.append(head)
        self.track = head
        self.energy = c.start_energy
        self.field.incr_meat(x, y)

    def step(self):
        j = len(self.stack) - 1
        self.track = self.stack[j]
        self.field.decr_meat(self.track.x, self.track.y)
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
        x = self.track.x - self.track.dx
        y = self.track.y - self.track.dy
        ass = Segment(x, y, self.track.direction)
        self.stack.append(ass)
        self.field.incr_meat(x, y)
        self.track = ass

    def self_intersection(self):
        x = self.head_x()
        y = self.head_y()
        for seg in self.stack[2:-1]:
            if seg.x == x and seg.y == y:
                return True
        return False

    def shrink(self):
        self.track = self.stack.pop(-1)
        self.field.decr_meat(self.track.x, self.track.y)

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

    def incr_energy(self, energy):
        self.energy += energy

    def decr_energy(self, energy):
        self.energy -= energy

    def __len__(self):
        return len(self.stack)


if __name__ == "__main__":
    pass
