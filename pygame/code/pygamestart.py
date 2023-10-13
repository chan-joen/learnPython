import sys
import pygame
from pygame.locals import *

pygame.init()

##초당 프레임 단위 설정##
FPS = 30
FramePerSec = pygame.time.Clock()

##색상 세팅##
BLUE = (0,0,255)
RED = (255,0,0)
GREEN = (0, 255, 0)
BLACK = (0,0,0)
WHITE = (255,255,255)

##게임 창 설정##
GameDisplay = pygame.display.set_mode((1280,720))
GameDisplay.fill(WHITE)
pygame.display.set_caption("PYGAME Example")

##선 및 도형 그리기##
# 파라미터 설명
# pygame.draw.shape(surface,color,pointlist(centerpoint),width)
# surface: 어느 게임 창에 위치시킬 것인지 설정
# color: 오브젝트 색상 설정
# pointlist: 튜플형식으로 각 포인트(각)의 좌표를 설정
# start_point, end_point, centerpoint: 시작 좌표, 끝점, 가운데 좌표
# width: 도형 테두리 굵기 지정
"""
# 선
pygame.draw.line(surface, color, start_point, end_point, width)
pygame.draw.lines(surface, color, start_point, end_point, width)

# 면
pygame.draw.polygon(surface, color, pointlist, width)

# 원
pygame.draw.circle(surface, color, center_point, radius, width)

# 타원
pygame,draw.ellipse(surface, color, bounding_rectangle, width)

# 직사각형
pygame.draw.rect(surface, color, rectangle_tuple, width)
#rectangle_tuple은 (사각형시작x좌표,사각형시작y좌표,가로길이,세로길이) 의 튜플로 이루어져 있음
"""
#도형 예제
pygame.draw.circle(GameDisplay,BLACK,(100,50),30)

pygame.draw.line(GameDisplay,BLUE,(200,20),(180,60))
pygame.draw.line(GameDisplay,BLUE,(200,20),(220,60))
pygame.draw.line(GameDisplay,BLUE,(180,60),(220,60))

pygame.draw.rect(GameDisplay,RED,(300,20,50,50),2)

pygame.draw.ellipse(GameDisplay,GREEN,(400,20,80,50),2)

##Game loop 설정: 게임이 진행되는 동안 실행되는 이벤트(함수)들 만들기##

# 게임을 종료시키는 함수
while True:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    FramePerSec.tick(FPS)