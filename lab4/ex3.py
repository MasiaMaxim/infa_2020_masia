import pygame
from pygame.draw import *
from random import randint
pygame.init()

FPS = 100
screen = pygame.display.set_mode((1200, 900))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]


def new_ball(x, y, r, color):
    '''рисует новый шарик '''
    circle(screen, color, (x, y), r)


def click(event, x, y, r, color):
    x_click, y_click = event.pos
    if ((((x - x_click)**2 + (y - y_click)**2)**0.5) <= r):
        print('+1')
    else:
        print('-1')


pygame.display.update()
clock = pygame.time.Clock()
finished = False

create_bubble_event = pygame.USEREVENT
pygame.time.set_timer(create_bubble_event, 1000)
balls = [(0,0,0,0)] * 10

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif (event.type == pygame.MOUSEBUTTONDOWN):
            for j in range(0, 9):	
                click(event, *balls[j])
        elif (event.type == create_bubble_event):
        	balls.pop(9)
        	balls.insert(0, (randint(100, 1100), randint(100, 900), randint(10, 100), COLORS[randint(0, 5)])) #x, y, r, color

    for i in range(0, 9):
        new_ball(*balls[i])
    pygame.display.update()

    screen.fill(BLACK)


pygame.quit()
