import pygame
import numpy as np
import config as c
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
    def __init__(self):
        self.game_on = None
        self.field = None
        self.scr = None
        self.snake = None
        self.snakes = []

    def run_single(self):
        pygame.init()
        pygame.display.set_caption("snake v1.0")
        gameClock = pygame.time.Clock()
        self.scr = pygame.display.set_mode((c.screen_width, c.screen_height), pygame.HWSURFACE)

        self.field = Field()
        self.field.set_frame(0)
        self.snake = Snake(5, 5, 1, self.field)
        self.game_on = True
        while self.game_on:
            gameClock.tick(c.fps)
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
                self.snake.incr_energy(c.apple_energy)
                self.field.decr_apple(x, y)
            self.snake.decr_energy(5)
            if self.snake.energy >= c.segment_energy:
                self.snake.grow()
                self.snake.decr_energy(c.segment_energy)
            elif self.snake.energy < 0:
                self.snake.shrink()
                self.snake.incr_energy(c.segment_energy)
            if len(self.snake) < 1:
                self.game_over()
            pix_arr = self.field.render_field()
            pygame.surfarray.blit_array(self.scr, pix_arr)
            pygame.display.flip()
            pygame.display.update()

    def run_simulation(self):
        pygame.init()
        pygame.display.set_caption("snake v1.0")
        gameClock = pygame.time.Clock()
        self.scr = pygame.display.set_mode((c.screen_width, c.screen_height), pygame.HWSURFACE)

        self.field = Field()
        self.field.set_frame(5)
        for i in range(20):
            x = np.random.randint(c.nx)
            y = np.random.randint(c.ny)
            while self.field.brick_map[x, y] != 0:
                x = np.random.randint(c.nx)
                y = np.random.randint(c.ny)
            d = x % 4
            self.snakes.append(SmartSnake(x, y, d, self.field))
            self.snakes[i].set_default_brains()

        self.field.spawn_random_apples(30000)
        self.game_on = True
        while self.game_on:
            gameClock.tick(c.fps)
            self.field.spawn_random_apples(50)
            for snake in self.snakes:
                snake.make_decision()
            for snake in self.snakes:
                snake.step()
            dead = []
            for snake in self.snakes:
                x = snake.head_x()
                y = snake.head_y()
                if self.field.brick_map[x, y] != 0:
                    dead.append(snake)
                if self.field.meat_map[x, y] != 1:
                    if snake not in self.snakes:
                        dead.append(snake)
                if self.field.apple_map[x, y] == 1:
                    snake.incr_energy(c.apple_energy)
                    self.field.decr_apple(x, y)
                snake.decr_energy(5)
                if snake.energy >= c.segment_energy:
                    snake.grow()
                    snake.decr_energy(c.segment_energy)
                elif snake.energy < 0:
                    snake.shrink()
                    snake.incr_energy(c.segment_energy)
                if len(snake) < 1:
                    if snake in dead:
                        dead.remove(snake)
                    snake.die()
                    self.snakes.remove(snake)
            for snake in self.snakes:
                x = snake.head_x()
                y = snake.head_y()
                if self.field.meat_map[x, y] != 1:
                    if snake not in self.snakes:
                        dead.append(snake)
            for snake in dead:
                snake.die()
                self.snakes.remove(snake)
            if len(self.snakes) == 0:
                self.game_over()
            for snake in self.snakes:
                snake.checkout_body()
                if len(snake) > 9:
                    new_snake = snake.divide()
                    self.snakes.append(new_snake)
                    
            pix_arr = self.field.render_field()
            pygame.surfarray.blit_array(self.scr, pix_arr)
            pygame.display.flip()
            pygame.display.update()

    def game_over(self):
        self.game_on = False


if __name__ == "__main__":
    game = Game()
    # game.run_single()
    game.run_simulation()
