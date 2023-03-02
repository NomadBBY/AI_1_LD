import pygame

WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH//COLS

RED = (208, 30, 15) # A deep red
WHITE = (255, 250, 250) # An off-white
BLACK = (20, 20, 20) # A dark grey
BLUE = (28, 137, 204) # A vibrant blue
GREY = (192, 192, 192) # A light grey

CROWN = pygame.transform.scale(pygame.image.load('assets/crown.png'), (44, 25))
