class Config:
    def __init__(self):
        self.square_size = 4
        self.nx = 100
        self.ny = 100

        self.screen_width = self.nx * self.square_size
        self.screen_height = self.ny * self.square_size
        self.fps = 1000
        self.key = {"UP": 1, "DOWN": 2, "LEFT": 3, "RIGHT": 0}
        self.start_energy = 300
        self.segment_energy = 50
        self.apple_energy = 30

        self.sim_start_snakes_number = 100
        self.sim_start_apples_number = int(self.nx*self.ny*0.05)
        self.sim_apples_grow = int(self.nx*self.ny*0.002)+1

        self.gray = 0xAAAAAA
        self.green = 0x00FF00
        self.red = 0xFF0000
        self.black = 0x111111
