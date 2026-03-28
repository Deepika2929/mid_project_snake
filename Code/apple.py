from settings import *
from random import choice
from os.path import join
import pygame


class Apple:
    def __init__(self, snake):
        self.pos = pygame.Vector2(5, 5)  # temporary fixed position (test)
        self.display_surface = pygame.display.get_surface()
        self.snake = snake

        self.surf = pygame.image.load(join('graphics', 'apple.png')).convert_alpha()
        self.surf = pygame.transform.scale(self.surf, (CELL_SIZE, CELL_SIZE))

    def set_pos(self):
        available_pos = [
            pygame.Vector2(x, y)
            for x in range(COLS)
            for y in range(ROWS)
            if pygame.Vector2(x, y) not in self.snake.body
        ]
        self.pos = choice(available_pos)

    def draw(self):
        rect = pygame.Rect(
            self.pos.x * CELL_SIZE,
            self.pos.y * CELL_SIZE,
            CELL_SIZE,
            CELL_SIZE
        )

        self.display_surface.blit(self.surf, rect)