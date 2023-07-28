# .\myInstalledPackages\pygame\__init__.py , line 284, commented by me as it was raising error
# .\myInstalledPackages\pygame\__init__.py , line 337-344, commented by me as was printing non-required text

import sys
sys.path.append("D:\Projects\Python\SnakeGame\myInstalledPackages")

import pygame
import random
import time
import json
import os
from datetime import datetime
# from pandas.io.json import json_normalize
# import myInstalledPackages.pygame as pygame


DATABASE_FILE = 'db.json'

BLACK = (0,0,0)
YELLOW = (255,255,0)
RED = (255,0,0)
DULL_GOLD = (187,161,79)
LOVENDER = (251,174,210)

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
SNAKE_LIST = []
SNAKE_LIST.append((snake_x,snake_y))


# welcome page
def start():
    input_name = pygame.Rect((5*XLIM),(WINDOW_HEIGHT-3*YLIM)/2,300,50)
    font = pygame.font.Font(None,35)
    gameWindow.fill(LOVENDER)
    pygame.draw.rect(gameWindow,BLACK,input_name,2,10)
    PLAYER_NAME = ""
    exit_game = False
    while not exit_game:
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("you choose to quit")
                print("*** THANK YOU ***")
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return PLAYER_NAME
                elif event.key == pygame.K_BACKSPACE:
                    PLAYER_NAME = PLAYER_NAME[:-1]
                else:
                    PLAYER_NAME += event.unicode
            name_label = font.render("Player Name:",True,BLACK)
            name = font.render(PLAYER_NAME, True, BLACK)
            gameWindow.blit(name_label, ((6*XLIM),(WINDOW_HEIGHT-5*YLIM)/2))
            gameWindow.blit(name, ((6*XLIM),(WINDOW_HEIGHT-2*YLIM)/2))
            pygame.display.update()


def plot_snake(gameWindow,snake_list):
    for x,y in snake_list:
        pygame.draw.rect(gameWindow,BLACK,(x,y,square_length,square_length))


def game_over(SCORE):
    end = pygame.font.SysFont("verdana",square_length*4,bold=True,italic=False)
    end = end.render("GAME OVER!!",True,RED,BLACK)
    gameWindow.blit(end,((5*XLIM),(WINDOW_HEIGHT-3*YLIM)/2))
    pygame.display.update()
    time.sleep(1)
    gameWindow.fill(DULL_GOLD)
    end = pygame.font.SysFont("verdana",square_length*2,bold=True,italic=False)
    end = end.render((f"Your Score is: {SCORE}"),True,RED,BLACK)
    gameWindow.blit(end,((5*XLIM),(WINDOW_HEIGHT-3*YLIM)/2))
    pygame.display.update()
    time.sleep(2)



exit_game = False
PLAYER_NAME = start()
print(PLAYER_NAME)

# Creating a game loop
while not exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("you choose to quit")
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
        game_over(SCORE)
        print("snake hits the wall")
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
            SNAKE_LEN += square_length
            food_x = random.randint(XLIM,WINDOW_WIDTH-XLIM)
            food_y = random.randint(YLIM,WINDOW_HEIGHT-YLIM)
            FOOD.append((food_x,food_y))
            pygame.draw.rect(gameWindow,RED,(food_x,food_y,square_length,square_length))
            pygame.display.update()
            break
    SNAKE_LIST.append((snake_x,snake_y))

    if len(SNAKE_LIST) > SNAKE_LEN:
        del SNAKE_LIST[0]

    # increase length of snake but don't allow the snake to grow too long
    if SNAKE_LEN < WINDOW_WIDTH/2:
        plot_snake(gameWindow,SNAKE_LIST)

    # snake hits itself
    if (snake_x,snake_y) in SNAKE_LIST[:-1]:
        game_over(SCORE)
        print("snake hits itself")
        exit_game = True
    
    score = pygame.font.SysFont("verdana",square_length,bold=True,italic=False)
    score = score.render(f"SCORE: {str(SCORE)}",True,BLACK,DULL_GOLD)
    gameWindow.blit(score,(square_length,square_length))
    pygame.display.update()


# adding data to "db.json" file
newData = {
    "rank": 0,
    "name": f"{PLAYER_NAME}",
    "score": SCORE,
    "date": str(datetime.date(datetime.now()))
}

if os.path.exists(DATABASE_FILE) and os.stat(DATABASE_FILE).st_size > 0:
    with open(DATABASE_FILE, "r") as file:
        data = json.load(file)
else:
    data = {"people": []}  # File is empty
    newData["rank"] = 1

rank = sum(1 for player in data["people"] if player["score"] > SCORE) + 1
newData["rank"] = rank
data["people"].append(newData)
data["people"].sort(key=lambda x: x['score'], reverse=True)

with open(DATABASE_FILE, "w") as file:
    json.dump(data, file,indent=4)




print("*** THANK YOU ***")
pygame.quit()
quit()





