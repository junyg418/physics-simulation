import sys
import pygame
from pygame.locals import *
from charactor import circle

while True:
    moveType = input('''
    완전탄성충돌 : 1
    포물선 통통 : 2
    종료 : 아무 키나 입력
    >>>''')

    if moveType == '1':
        move = 0 # 'wantanchung'
        break
    elif moveType == '2':
        move = 1 # 'pomul'
        break
    else:
        sys.exit()


pygame.init()

FPS = 100
FramePerSec = pygame.time.Clock()

BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

GameDisplay = pygame.display.set_mode((640, 440))
GameDisplay.fill(WHITE)
# pygame.draw.circle(GameDisplay, BLACK, (100, 50), 30)
pygame.display.set_caption("Gravity Falls")

Circle = circle.Circle(GameDisplay)



while True:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
        elif event.type == MOUSEBUTTONDOWN:
            pygame.draw.circle(GameDisplay, BLACK, event.pos, 30)
    FramePerSec.tick(FPS)
    Circle.accel()
    if move:
        Circle.angry()
    Circle.draw()
