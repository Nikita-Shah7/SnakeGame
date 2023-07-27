# .\myInstalledPackages\pygame\__init__.py , line 284, commented by me as it was raising error
# .\myInstalledPackages\pygame\__init__.py , line 337-344, commented by me as was printing non-required text

import sys
sys.path.append("D:\Projects\Python\SnakeGame\myInstalledPackages")

import pygame
import random
import time
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
square_length = 12
velocity_x = 0
velocity_y = 0
velocity = 0.2

SCORE = 0

pygame.init()
pygame.display.set_caption("SnakeGame")
gameWindow = pygame.display.set_mode(WINDOW_SIZE)


FOOD = []
while len(FOOD) < 6:
    food_x = random.randint(XLIM,WINDOW_WIDTH-XLIM)
    food_y = random.randint(YLIM,WINDOW_HEIGHT-YLIM)
    FOOD.append((food_x,food_y))
pygame.display.update()

SNAKE_LEN = 1


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
    
    # Snake hits the walls
    if snake_x > WINDOW_WIDTH-5 or snake_y > WINDOW_HEIGHT-5 or snake_x < 1 or snake_y < 1 :
        end = pygame.font.SysFont("verdana",square_length*4,bold=True,italic=False)
        end = end.render("GAME OVER!!",True,RED,BLACK)
        gameWindow.blit(end,((5*XLIM),(WINDOW_HEIGHT-3*YLIM)/2))
        pygame.display.update()
        time.sleep(2)
        exit_game = True
    snake_x += velocity_x
    snake_x %= WINDOW_WIDTH
    snake_y += velocity_y
    snake_y %= WINDOW_HEIGHT
    pygame.display.update()
    

    gameWindow.fill(DULL_GOLD)

    # creating an off_screen_surface
    food_surface = pygame.Surface(WINDOW_SIZE)
    food_surface.fill(DULL_GOLD)
    for food_x, food_y in FOOD:
            pygame.draw.rect(food_surface, RED, (food_x, food_y, square_length, square_length))
    gameWindow.blit(food_surface,(0,0))
    pygame.draw.rect(gameWindow,BLACK,(snake_x,snake_y,square_length,square_length))


    # eating food
    sensitivity = square_length*0.6
    for food_x,food_y in FOOD:
        if abs(food_x - snake_x) < sensitivity and abs(food_y - snake_y) < sensitivity:
            FOOD.remove((food_x,food_y))
            SCORE += 1
            food_x = random.randint(XLIM,WINDOW_WIDTH-XLIM)
            food_y = random.randint(YLIM,WINDOW_HEIGHT-YLIM)
            FOOD.append((food_x,food_y))
            pygame.draw.rect(gameWindow,RED,(food_x,food_y,square_length,square_length))
            pygame.display.update()
            break
    
    score = pygame.font.SysFont("verdana",square_length,bold=True,italic=False)
    score = score.render(f"SCORE: {str(SCORE)}",True,BLACK,DULL_GOLD)
    gameWindow.blit(score,(square_length,square_length))
    pygame.display.update()


pygame.quit()
quit()





