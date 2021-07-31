import pygame

square_size = 20
nx = 50
ny = 30
screen_width = nx * square_size
screen_height = ny * square_size
fps = 5
key = {"UP": 1, "DOWN": 2, "LEFT": 3, "RIGHT": 4}
start_energy = 200
segment_energy = 50
apple_energy = 30

gray = pygame.Color("gray")
green = pygame.Color("green")
red = pygame.Color("red")
black = pygame.Color("black")
