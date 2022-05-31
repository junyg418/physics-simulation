import sys
import pygame
from pygame.locals import *
from charactor import circle
from charactor import spaceCircle 

tan_bool = False
space_bool = False
while True:
    moveType = input('''
완전탄성충돌 : 1
포물선 통통 : 2
무중력 시뮬 : 3
종료 : 아무 키나 입력
>>>''')

    if moveType == '1':
        move = 0 # 'wantanchung'
        tan_bool = True
        break
    elif moveType == '2':
        move = 1 # 'pomul'
        tan_bool = True
        break
    elif moveType == '3':
        space_bool = True
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

size = (640, 440)
display_x, display_y = size 
GameDisplay = pygame.display.set_mode((display_x, display_y))
GameDisplay.fill(WHITE)
pygame.display.set_caption("Gravity Falls")


if tan_bool:
    circle.dis_x = display_x
    circle.dis_y = display_y
    Circle = circle.Circle(GameDisplay)

while tan_bool:
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
            pygame.draw.circle(GameDisplay, BLACK, event.pos, 10)
    FramePerSec.tick(FPS)
    Circle.accel()
    if move:
        Circle.angry()
    Circle.draw()

if space_bool:
    spaceCircle.dis_x = display_x
    spaceCircle.dis_y = display_y
    spacePlayer = spaceCircle.SpaceCircle(GameDisplay)

while space_bool:
    pygame.display.update()
    # if abs(spacePlayer.v_x)

    font = pygame.font.SysFont("arial", 20)
    text = font.render(f'x축 속도: {abs(spacePlayer.v_x)} y축 속도: {abs(spacePlayer.v_y)}', True, BLACK)
    GameDisplay.blit(text, (0,0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            elif event.key == K_LEFT:
                # spacePlayer.v_x -= 0.1
                spacePlayer.v_x = round(spacePlayer.v_x - 0.1, 1)
                print(f'x{spacePlayer.v_x}')
            elif event.key == K_RIGHT:
                # spacePlayer.v_x += 0.1
                spacePlayer.v_x = round(spacePlayer.v_x + 0.1, 1)
                print(f'x{spacePlayer.v_x}')
            elif event.key == K_UP:
                # spacePlayer.v_y += 0.1
                spacePlayer.v_y = round(spacePlayer.v_y - 0.1, 1)
                print(f'y{spacePlayer.v_y}')
            elif event.key == K_DOWN:
                spacePlayer.v_y = round(spacePlayer.v_y + 0.1, 1)
                print(f'y{spacePlayer.v_y}')
        
    FramePerSec.tick(FPS)
    spacePlayer.x_posMove()
    spacePlayer.y_posMove()
    spacePlayer.draw()