import pygame
import numpy as np
from config import Config
from field import Field
from snake import Snake
from smart_snake import SmartSnake


def dir_from_key():
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                return 1
            elif event.key == pygame.K_w:
                return 2
            elif event.key == pygame.K_a:
                return 3
            elif event.key == pygame.K_s:
                return 0


class Game:
    def __init__(self, conf):
        self.conf = conf
        self.game_on = None
        self.field = None
        self.scr = None
        self.snake = None
        self.snakes = []

    def run_single(self):
        pygame.init()
        pygame.display.set_caption("snake v1.0")
        game_clock = pygame.time.Clock()
        self.scr = pygame.display.set_mode((self.conf.screen_width, self.conf.screen_height), pygame.HWSURFACE)

        self.field = Field(self.conf)
        self.field.set_frame(0)

        self.snake = Snake(5, 5, 1, self.field, self.conf.start_energy)

        self.game_on = True
        while self.game_on:
            game_clock.tick(self.conf.fps)
            self.field.spawn_random_apples(1)
            key_dir = dir_from_key()
            if key_dir in [1, 2, 3, 0]:
                self.snake.set_direction(key_dir)

            self.snake.step()

            x = self.snake.head_x()
            y = self.snake.head_y()

            if self.field.brick_map[x, y] == 1:
                self.game_over()
                break

            if self.snake.self_intersection():
                self.game_over()
                break

            if self.field.apple_map[x, y] == 1:
                self.snake.incr_energy(self.conf.apple_energy)
                self.field.remove_apple(x, y)

            self.snake.decr_energy(5)
            if self.snake.energy >= self.conf.segment_energy:
                self.snake.grow()
                self.snake.decr_energy(self.conf.segment_energy)
            elif self.snake.energy < 0:
                self.snake.shrink()
                self.snake.incr_energy(self.conf.segment_energy)
            if len(self.snake) < 1:
                self.game_over()

            self.update_image()

    def run_simulation(self):
        # init pygame instance
        pygame.init()
        pygame.display.set_caption("snake v1.0")
        game_clock = pygame.time.Clock()
        self.scr = pygame.display.set_mode((self.conf.screen_width, self.conf.screen_height), pygame.HWSURFACE)

        # init field
        self.field = Field(self.conf)
        self.field.set_frame(5)

        # spawn start snakes
        for i in range(self.conf.sim_start_snakes_number):
            x = np.random.randint(self.conf.nx)
            y = np.random.randint(self.conf.ny)
            while self.field.brick_map[x, y] != 0:
                x = np.random.randint(self.conf.nx)
                y = np.random.randint(self.conf.ny)
            d = x % 4
            self.snakes.append(SmartSnake(x, y, d, self.field, self.conf.start_energy))
            self.snakes[i].set_default_brains()

        # spawn start apples
        self.field.spawn_random_apples(int(self.conf.sim_start_apples_number))

        # game loop
        self.game_on = True
        while self.game_on:
            # spawn apples
            self.field.spawn_random_apples(self.conf.sim_apples_grow)

            # snakes make decision
            for snake in self.snakes:
                snake.make_decision()

            # snakes move
            for snake in self.snakes:
                snake.step()

            # first iteration of management of snakes
            corpses = []
            for snake in self.snakes:
                x = snake.head_x()
                y = snake.head_y()

                # bricks collisions
                if self.field.brick_map[x, y] != 0:
                    corpses.append(snake)

                # meat collisions
                if self.field.meat_map[x, y] != 1:
                    if snake not in corpses:
                        corpses.append(snake)

            # remove brick and meat casualties
            for snake in corpses:
                snake.die()
                self.snakes.remove(snake)
            corpses = []

            for snake in self.snakes:
                x = snake.head_x()
                y = snake.head_y()

                # consume apples
                if self.field.apple_map[x, y] > 0:
                    snake.incr_energy(self.conf.apple_energy)
                    self.field.remove_apple(x, y)

                # energy loss
                snake.decr_energy(5)

                # grow or shrink
                if snake.energy >= self.conf.segment_energy:
                    snake.grow()
                    snake.decr_energy(self.conf.segment_energy)
                elif snake.energy < 0:
                    snake.shrink()
                    snake.incr_energy(self.conf.segment_energy)

                # starvation death
                if len(snake) < 1:  # no corpse after starvation death!
                    snake.die()
                    self.snakes.remove(snake)

            # tail collision death
            for snake in self.snakes:
                x = snake.head_x()
                y = snake.head_y()
                if self.field.meat_map[x, y] != 1:
                    if snake not in self.snakes:
                        corpses.append(snake)

            # remove tail casualties
            for snake in corpses:
                snake.die()
                self.snakes.remove(snake)
                print('tail collision')

            # checkout overall death
            if len(self.snakes) == 0:
                self.game_over()

            # birth
            for snake in self.snakes:
                # snake.checkout_body()  # if there is a discontinuity
                if len(snake) > 9:
                    new_snake = snake.divide()
                    self.snakes.append(new_snake)

            self.update_image()
            game_clock.tick(self.conf.fps)

    def game_over(self):
        self.game_on = False

    def update_image(self):
        pix_arr = self.field.render_field()
        pygame.surfarray.blit_array(self.scr, pix_arr)
        pygame.display.flip()
        pygame.display.update()


if __name__ == "__main__":
    conf = Config()
    game = Game(conf)
    #game.run_single()
    game.run_simulation()
