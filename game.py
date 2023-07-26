# .\myInstalledPackages\pygame\__init__.py , line 284, commented by me as it was raising error
# .\myInstalledPackages\pygame\__init__.py , line 337-344, commented by me as was printing non-required text

import sys
sys.path.append("D:\Projects\Python\FlappyBird\myInstalledPackages")

import pygame
import random
# import myInstalledPackages.pygame as pygame


BLACK = (0,0,0)
YELLOW = (255,255,0)
RED = (255,0,0)
DULL_GOLD = (187,161,79)

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
WINDOW_SIZE = (WINDOW_WIDTH,WINDOW_HEIGHT)
XLIM = WINDOW_WIDTH*0.05
YLIM = WINDOW_HEIGHT*0.05

snake_x = WINDOW_WIDTH/2
snake_y = WINDOW_HEIGHT/2
square_length = 10
velocity_x = 0
velocity_y = 0
velocity = 0.3

pygame.init()
pygame.display.set_caption("SnakeGame")
gameWindow = pygame.display.set_mode(WINDOW_SIZE)


FOOD = []
while len(FOOD) < 5:
    food_x = random.randint(XLIM,WINDOW_WIDTH)
    food_y = random.randint(YLIM,WINDOW_HEIGHT)
    FOOD.append((food_x,food_y))

print(FOOD)
    


exit_game = False
game_over = False

# Creating a game loop
while not exit_game:
    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            exit_game = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                velocity_x = velocity
                velocity_y = 0
            elif event.key == pygame.K_LEFT:
                velocity_x = -velocity
                velocity_y = 0
            elif event.key == pygame.K_UP:
                velocity_x = 0
                velocity_y = -velocity
            elif event.key == pygame.K_DOWN:
                velocity_x = 0
                velocity_y = velocity

    if snake_x > WINDOW_WIDTH-5 or snake_y > WINDOW_HEIGHT-5 or snake_x < 1 or snake_y < 1 :
        exit_game = True
    snake_x += velocity_x
    snake_x %= WINDOW_WIDTH
    snake_y += velocity_y
    snake_y %= WINDOW_HEIGHT
    pygame.display.update()
            
    gameWindow.fill(DULL_GOLD)
    pygame.draw.rect(gameWindow,BLACK,(snake_x,snake_y,square_length,square_length))
    pygame.display.update()

pygame.quit()
quit()
