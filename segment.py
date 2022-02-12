import numpy as np


class Segment:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
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
    sut = Segment(5, 5, 0)
    print(sut.dx)
    print(sut.dy)
    sut.set_direction(1)
    print(sut.dx)
    print(sut.dy)
    sut.set_direction(2)
    print(sut.dx)
    print(sut.dy)
    sut.set_direction(3)
    print(sut.dx)
    print(sut.dy)
    sut.step()
    sut.step()
    print(sut.x)
    print(sut.y)
