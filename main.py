import pygame

from boss import *
from map_game import *
from bullet_icon import *
from fighter import *
from boom_box import *

pygame.init()

SCREEN_WIDTH = 800
SCREEN_hEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_hEIGHT))
pygame.display.set_caption('Rambo')
player = fighter()

run = True
while run:
    player.show()
    
pygame.quit()