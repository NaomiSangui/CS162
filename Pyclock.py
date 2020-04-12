# Import needed stuff
import pygame
from pygame.locals import *

# Set up the game and its base variables
pygame.init()   
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
keys = [False, False, False, False]
Playerpos=[100,100]
# Load images
Player = pygame.image.load("resources/images/player_character.png")
Dungeon_Flooring = pygame.image.load("resources/images/dungeon_flooring.png")

# Background
screen.blit(Dungeon_Flooring,(0,0))
# Movement
while 1:
    screen.fill(0)
    screen.blit(Player, Playerpos)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit() 
            exit(0)
            #Movement
        if event.type == pygame.KEYDOWN:
            if event.key==K_w:
                keys[0]=True
            elif event.key==K_a:
                keys[1]=True
            elif event.key==K_s:
                keys[2]=True
            elif event.key==K_d:
                keys[3]=True
        if event.type == pygame.KEYUP:
            if event.key==pygame.K_w:
                keys[0]=False
            elif event.key==pygame.K_a:
                keys[1]=False
            elif event.key==pygame.K_s:
                keys[2]=False
            elif event.key==pygame.K_d:
                keys[3]=False
    # Player movement cont.
    if keys[0]:
        Playerpos[1]-=0.1
    elif keys[2]:
        Playerpos[1]+=0.1
    if keys[1]:
        Playerpos[0]-=0.1
    elif keys[3]:
        Playerpos[0]+=0.1