import sys
import pygame, pymunk, pymunk.pygame_util
from pygame.locals import *

pygame.init()

FramePerSec = pygame.time.Clock()

GameDisplay = pygame.display.set_mode((1280,720))
GameDisplay.fill((255,255,255))
pygame.display.set_caption("Suika Game")

space = pymunk.Space()

space.gravity = (0, 1000)

draw_options = pymunk.pygame_util.DrawOptions(GameDisplay)

floor = pymunk.Body(body_type = pymunk.Body.STATIC)
floor.position = (500,670)
floor_shape = pymunk.Segment(floor,(0,0),(500,0),1)
floor_shape.friction = 0.2
space.add(floor,floor_shape)

L_wall = pymunk.Body(body_type = pymunk.Body.STATIC)
L_wall.position = (500,670)
L_wall_shape = pymunk.Segment(L_wall,(0,0),(0,-700),1)
L_wall_shape.friction = 0.2
space.add(L_wall,L_wall_shape)

R_wall = pymunk.Body(body_type = pymunk.Body.STATIC)
R_wall.position = (1000,670)
R_wall_shape = pymunk.Segment(R_wall,(0,0),(0,-700),1)
R_wall_shape.friction = 0.2
space.add(R_wall,R_wall_shape)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('.\pygame\source\\arrow-2079328_1280.png')
        self.rect=self.image.get_rect()
        self.rect = self.rect.inflate(-20,-20)
        print("플레이어:",self.rect)
        self.rect.center = (750,20)

    def move(self):
        pressKeys = pygame.key.get_pressed()
        if self.rect.left>500:
            if pressKeys[K_LEFT]:
                self.rect.move_ip(-2,0)
                position_P = self.rect.center
                return position_P
        if self.rect.right<1000:
            if pressKeys[K_RIGHT]:
                self.rect.move_ip(2,0)
                position_P = self.rect.center
                return position_P
    def ball(self):
        perssKeys = pygame.key.get_pressed()
        if perssKeys[K_SPACE]:
            ball = pymunk.Body(1,1)
            ball.position = self.rect.center
            ball_shape = pymunk.Circle(ball,50)
            ball_shape.friction = 0.2 
            space.add(ball,ball_shape)
            
            
P1=Player()


 
All_groups = pygame.sprite.Group()
All_groups.add(P1)

running = True
while running:
    FramePerSec.tick(60)
    space.step(1/60)

    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    GameDisplay.fill((255,255,255))
    space.debug_draw(draw_options)

    for i in All_groups:
        GameDisplay.blit(i.image,i.rect)
        i.move()
        i.ball()
        if str(i) == '<Player Sprite(in 1 groups)>':
            player_pos = i


pygame.quit()