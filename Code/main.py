from settings import *

from snake import Snake
from apple import Apple
import pygame

class Main:
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption('Snake Game')

        # game objects
        self.bg_rects = [pygame.Rect((COL + int(row % 2 == 0)) * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                         for COL in range(0,COLS,2)for row in range(ROWS)]
        self.snake = Snake()
        self.apple = Apple(self.snake)

        # timer
        self.update_event = pygame.event.custom_type()
        pygame.time.set_timer(self.update_event, 200)


    def draw_bg(self):
        for rect in self.bg_rects:
            pygame.draw.rect(self.display_surface, 'red', rect)

    def input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]: 
            self.snake.direction = pygame.Vector2(1,0) if self.snake.direction.x != -1 else self.snake.direction
        if keys[pygame.K_LEFT]: 
            self.snake.direction = pygame.Vector2(-1,0) if self.snake.direction.x != 1 else self.snake.direction
        if keys[pygame.K_UP]: 
            self.snake.direction = pygame.Vector2(0,-1) if self.snake.direction.y != 1 else self.snake.direction
        if keys[pygame.K_DOWN]: 
            self.snake.direction = pygame.Vector2(0,1) if self.snake.direction.y != -1 else self.snake.direction

    def collision(self):
        # apple
        if self.snake.body[0] == self.apple.pos:
            self.snake.has_eaten = True
            self.apple.set_pos()


    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()


                if event.type == self.update_event:
                    self.snake.update()


            #updates
            self.input()
            self.collision()


            #drawing
            self.display_surface.fill('black')
            #self.draw_bg()
            self.snake.draw()
            self.apple.draw()
            pygame.display.update()

if __name__ == '__main__':

 main = Main()
 main.run()