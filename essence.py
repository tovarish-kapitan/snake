import config as c


def x_to_pix(x):
    pix = round(x * c.square_size)
    return pix


def y_to_piy(y):
    piy = round(y * c.square_size)
    return piy


class Essence:
    def __init__(self, x, y, col, scr):
        self.x = x
        self.y = y
        self.pix = x_to_pix(x)
        self.piy = y_to_piy(y)
        self.size = c.square_size
        self.col = col
        self.scr = scr
        self.draw()

    def set_x(self, x):
        self.x = x
        self.pix = x_to_pix(x)

    def set_y(self, y):
        self.y = y
        self.piy = y_to_piy(y)

    def draw(self):
        pass


if __name__ == "__main__":
    pass
