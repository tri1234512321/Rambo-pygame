from types import NoneType
import pygame, sys

from boss import *
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

player = fighter(200, 300, 5, 1.5)
boss = boss(350, 300, 5, 2, screen)
boss_attack = boss.boss_attack

#Key event
run_left = False
run_right = False
bossAttack = False
skill = [False, False, False]

run = True
while run:
    clock.tick(FPS)
    
    # ---------------MAP------------
    screen.fill('black')
    level.run()
    # ---------------MAP------------
    #img = player.show(screen)
    img2 = boss.show(screen)

    #boss attack
    boss_attack.update()
    boss_attack.draw(screen)
    #boss.ai(player, boss_attack)

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
            if event.key == pygame.K_SPACE:
                boss.attack(0)
            if event.key == pygame.K_DOWN:
                boss.attack(1) 
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                run_left = False
            if event.key == pygame.K_RIGHT:
                run_right = False
            if event.key == pygame.K_SPACE:
                bossAttack = False
        
    #state = player.update(run_left, run_right, level_map)
    state = boss.update(run_left, run_right ,level_map)
    
    pygame.display.update()
    
pygame.quit()
