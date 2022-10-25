import pygame
import os

from map_settings import *

ANIMATION_TIMESTEP = 200
GRAVITY = 0.75

class fighter():
    #built define for game
    def __init__(self,x, y, speed, scale):
        self.die = False
        self.speed = speed
        self.anim = []
        animation_type = ['idle', 'run', 'jump', 'die']
        for animation in animation_type:
            num_img = len(os.listdir(f'images/player/{animation}/'))
            temp = []
            for i in range(num_img):
                image = pygame.image.load(f'images/player/{animation}/{i}.png').convert_alpha()
                image = pygame.transform.scale(image, (int(image.get_width() * scale), int(image.get_height() * scale)))
                temp.append(image)
            self.anim.append(temp)
        self.index = 0
        self.action = 0
        self.image = self.anim[self.action][self.index]
        self.flip = False
        self.rect = self.image.get_rect()
        self.rect.midbottom = (x, y)
        self.update_time = pygame.time.get_ticks()
        self.vector_y = 0
        self.falling = True
        self.pos_x = x
        
    def barrier_pos(self, level_map):
        player_pos = (int((self.rect.y + self.vector_y + tile_size) / tile_size), int(self.pos_x / tile_size))
        obj = level_map[player_pos[0]][player_pos[1]]
        bar_pos = SCREEN_hEIGHT
        if obj != ' ' and obj != 'C':
            bar_pos = (player_pos[0] - 1 ) * tile_size
        return bar_pos
    
    def change_action(self, new_action):
        if new_action != self.action:
            self.action = new_action
            self.index = 0
            
        #update image
        self.image = self.anim[self.action][self.index]
        
    def update(self, run_left, run_right, level_map):
        #update position of player
        if run_left and self.pos_x - self.speed >= 0:
            self.rect.x -= self.speed
            self.pos_x -= self.speed
            self.flip = True
        if run_right: #and self.pos_x + self.speed <= map_width:
            self.rect.x += self.speed
            self.pos_x += self.speed
            self.flip = False
            
        if self.falling == False:
            self.rect.x -= 2
            
        if self.falling:
            self.pos_x += 2
            self.vector_y += GRAVITY
            if self.vector_y > 10:
                self.vector_y = 10
        
        bar = self.barrier_pos(level_map)
        if self.rect.y + self.vector_y >= bar:
            self.rect.y = bar
            self.vector_y = 0
            self.falling = False
        else:
            self.falling = True
                
        self.rect.y += self.vector_y
        
        if(self.rect.y >= SCREEN_hEIGHT - 2 * tile_size):
            self.die = True   
        
        #update frame of action
        if pygame.time.get_ticks() - self.update_time > ANIMATION_TIMESTEP:   
            self.index += 1
            if self.index >= len(self.anim[self.action]):
                if self.die:
                    self.index = len(self.anim[self.action]) - 1
                else:
                    self.index = 0
            self.update_time = pygame.time.get_ticks()
        
        #update action of player
        if self.die:
            self.change_action(3)
            return 3
        elif self.falling:
            self.change_action(2)
            return 2
        elif run_left or run_right:
            self.change_action(1)
            return 1
        else:
            self.change_action(0)
        return 0
    
    def jump(self):
        if self.falling == False:
            self.vector_y = -15
            self.falling = True
    
    def show(self, surface):
        surface.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)
        