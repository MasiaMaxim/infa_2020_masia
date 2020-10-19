import pygame
from pygame.draw import *
from random import randint
import numpy as np
pygame.init()

FPS = 100
width = 1200
height = 900
Rmax = 100
Rmin = 10
screen = pygame.display.set_mode((width, height))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]


def new_ball(x, y, r, color, speed, alpha, balls, i, FPS, width, height):
    '''рисует новый шарик '''
    betta = alpha
    circle(screen, color, (x, y), r)
    if (x + r) >= width:
        betta = 180 - alpha
    if (y + r) >= height:
        betta = 360 - alpha
    if (x - r) <= 0:
        betta = 180 - alpha
    if (y - r) <= 0:
        betta = 360 - alpha
    balls[i] = x + int(0.05*speed*np.cos(np.pi*betta/180)*(FPS/100)), y + int(0.05*speed*np.sin(np.pi*betta/180)*(FPS/100)), r, color, speed, betta





def click(event, x, y, r, color, speed, alpha, balls, j, FPS):
    flag = 0
    x_click, y_click = event.pos
    if ((((x - x_click)**2 + (y - y_click)**2)**0.5) <= r):
        flag = 1
        balls[j] = 0,0,0,0,0,0
    return flag




pygame.display.update()
clock = pygame.time.Clock()
finished = False

create_ball_event = pygame.USEREVENT
pygame.time.set_timer(create_ball_event, 1000)
balls = [(0,0,0,0,0,0)] * 10
flags = 0
score = 0

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True


        elif (event.type == pygame.MOUSEBUTTONDOWN):
            flags = 0
            for j in range(0, 9):
            	if (click(event, *balls[j], balls, j, FPS) == 1):
            		flags = flags + 1
            if flags != 0:
            	score = score + flags
            else:
            	score -= 1


        elif (event.type == create_ball_event):
        	balls.pop(9)
        	balls.insert(0, (randint(Rmax, width - Rmax), randint(Rmax, height - Rmax), randint(Rmin, Rmax), COLORS[randint(0, 5)], randint(10, 100), randint(0, 360)))
        	            #x, y, r, color, speed, alpha

    for i in range(0, 9):
        new_ball(*balls[i], balls, i, FPS, width, height)


    myfont = pygame.font.SysFont('Comic Sans MS', 30) #выбираем шрифт
    textsurface = myfont.render(str(score), False, (255, 255, 255)) #создаём поверхность с текстом
    screen.blit(textsurface,(0,0)) # отображаем поверхность

    pygame.display.update()

    screen.fill(BLACK)


pygame.quit()
