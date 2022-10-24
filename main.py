import pygame, sys

# from boss import *
# from map_game import *
# from bullet_icon import *
# from fighter import *
# from boom_box import *
# ---------------MAP------------
from map_settings import *
from tiles import Tile
from level import Level
# ---------------MAP------------

pygame.init()



screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_hEIGHT))
pygame.display.set_caption('Rambo')
clock = pygame.time.Clock()
# player = fighter()
# ---------------MAP------------
level = Level(level_map, screen)
# ---------------MAP------------


run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    # player.show()
    # ---------------MAP------------
    screen.fill('black')
    level.run()
    # ---------------MAP------------

    pygame.display.update()
    clock.tick(60)
    
pygame.quit()