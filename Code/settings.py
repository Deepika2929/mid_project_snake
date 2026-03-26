import pygame
from sys import exit
from os.path import join

pygame.init()
info = pygame.display.Info()

CELL_SIZE = 80
ROWS = int((info.current_h * 0.7) // CELL_SIZE)
COLS = int((info.current_w * 0.7) // CELL_SIZE)
WINDOW_WIDTH = COLS * CELL_SIZE
WINDOW_HEIGHT = ROWS * CELL_SIZE

#COLORS
LIGHT_RED = "#E13232"
DARK_RED = "#B00808"

#START POS
START_LENGTH = 3
START_ROW = ROWS // 2
START_COL = START_LENGTH + 2

#SHADOW
SHADOW_SIZE = pygame.Vector2(4,4)
SHADOW_OPACITY = 50