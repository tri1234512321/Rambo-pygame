import pygame, sys

# from boss import *
# from map_game import *
# from bullet_icon import *
from fighter import *
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
FPS = 60

# ---------------MAP------------
level = Level(level_map, screen)
# ---------------MAP------------

player = fighter(300, 300, 5, 1.5)
run_left = False
run_right = False

run = True
while run:
    clock.tick(FPS)
    
    # ---------------MAP------------
    screen.fill('black')
    level.run()
    # ---------------MAP------------
    
    img = player.show(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
            if event.key == pygame.K_LEFT:
                run_left = True
            if event.key == pygame.K_RIGHT:
                run_right = True
            if event.key == pygame.K_UP:
                player.jump()
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                run_left = False
            if event.key == pygame.K_RIGHT:
                run_right = False
        
    state = player.update(run_left, run_right, level_map)
    
    pygame.display.update()
    
pygame.quit()