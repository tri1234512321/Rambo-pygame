import pygame

from fighter import *

# attack_img = pygame.image.load('images/boss/attack/11.png').convert_alpha()
class boss():
    def __init__(self,x, y, speed, scale, screen):
        self.screen = screen
        self.die = False
        self.health = 12000
        self.max_health = 12000
        self.speed = speed
        self.vision = pygame.Rect(0, 0, SCREEN_WIDTH/2, 20)
        self.shoot_cd = 0
        self.beam_cd = 5
        self.anim = []
        animation_type = ['idle', 'range_attack', 'beam_attack', 'death', 'take_hit']
        for animation in animation_type:
            num_img = len(os.listdir(f'images/boss/model-2/{animation}/'))
            temp = []
            for i in range(num_img):
                image = pygame.image.load(f'images/boss/model-2/{animation}/{i}.png').convert_alpha()
                image = pygame.transform.scale(image, (int(image.get_width() * scale), int(image.get_height() * scale)))
                temp.append(image)
            self.anim.append(temp)
        self.index = 0
        self.action = 0
        self.boss_attack = pygame.sprite.Group()
        self.shoot = []
        self.range_attack = False
        self.beam_attack = False
        self.attack_interval = ANIMATION_TIMESTEP
        self.image = self.anim[self.action][self.index]
        self.flip = True
        self.rect = self.image.get_rect()
        self.rect.midbottom = (x, y)
        self.stand_line = -145
        self.update_time = pygame.time.get_ticks()
        self.vector_y = 0
        self.falling = True
        self.attacking = False
        self.pos_x = x
        self.direction = 1
        print(self.rect)

    def barrier_pos(self, level_map):
        player_pos = (int((self.rect.y + self.vector_y + self.stand_line) / self.stand_line), int(self.pos_x / self.stand_line))
        obj = level_map[player_pos[0]][player_pos[1]]
        bar_pos = SCREEN_hEIGHT
        if obj != ' ' and obj != 'C':
            bar_pos = (player_pos[0] - 1 ) * self.stand_line
        return bar_pos
    
    def change_action(self, new_action):
        if new_action != self.action:
            self.action = new_action
            self.index = 0
            
        #update image
        self.image = self.anim[self.action][self.index]
        
    def update(self, run_left, run_right, level_map):
        pygame.draw.rect(self.image, (255, 0, 0), [0, 0, self.rect.width, self.rect.height], 1)
        #update position of player
        if run_left and self.pos_x - self.speed >= 0:
            self.rect.x -= self.speed
            self.pos_x -= self.speed
            self.flip = False
            self.direction = -1
        if run_right: #and self.pos_x + self.speed <= map_width:
            self.rect.x += self.speed
            self.pos_x += self.speed
            self.flip = True
            self.direction = 1
            
        if self.falling == False:
            self.rect.x -= 0
            
        if self.falling:
            self.pos_x += 0
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
        if self.range_attack:
            self.attack_interval = ANIMATION_TIMESTEP*0.15
        if pygame.time.get_ticks() - self.update_time > self.attack_interval:
            
            if self.shoot_cd > 0:
                self.shoot_cd -= 1 
            self.index += 1
            if self.index >= len(self.anim[self.action]):
                if self.range_attack:
                    self.boss_attack.add(self.shoot.pop(0))
                    self.attack_interval = ANIMATION_TIMESTEP
                    self.range_attack = False
                    self.change_action(0)
                if self.die:
                    self.index = len(self.anim[self.action]) - 1
                else:
                    self.index = 0
            self.update_time = pygame.time.get_ticks()
        
        #update action of player
        if self.die:
            #self.change_action(3)
            return 3
        # elif self.falling:
        #     self.change_action(2)
        #     return 2
        # elif run_left or run_right:
        #     self.change_action(1)
        #     return 1
        elif self.range_attack:
            self.change_action(1)
            return 1
        elif self.beam_attack:
            self.change_action(2)
            return 2
        else:
            self.change_action(0)
        return 0
    
    def jump(self):
        if self.falling == False:
            self.vector_y = -15
            self.falling = True
    
    def attack(self, atk_type):
        if self.shoot_cd == 0:
            if atk_type == 0:
                self.range_attack = True
            elif atk_type == 1:
                self.beam_attack = True
            self.shoot_cd = 5
            attack = Attack(self.rect.centerx + 1.5*(self.rect.size[0])*self.direction, self.rect.centery, self.direction, 0)
            self.shoot.append(attack)

    def ai(self, player, boss_attack):
        self.vision.center = (self.rect.centerx + 75*self.direction, self.rect.centery)
        
        if self.vision.colliderect(player.rect):
            #begin attack
            self.attack(0)
    
    def show(self, surface):
        surface.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)
    
class ai():
    def __init__():
        pass

class Attack(pygame.sprite.Sprite):
    def __init__(self, x, y, direction, atk_type):
        pygame.sprite.Sprite.__init__(self)
        self.speed = 10
        self.anim = []
        self.index = 0
        self.type = atk_type
        attack_type = ['range_attack', 'beam_attack']
        for animation in attack_type:
            num_img = len(os.listdir(f'images/boss/attack/{animation}/'))
            temp = []
            for i in range(num_img):
                image = pygame.image.load(f'images/boss/attack/{animation}/{i}.png').convert_alpha()
                image = pygame.transform.scale(image, (int(image.get_width()), int(image.get_height())))
                temp.append(image)
            self.anim.append(temp)
        self.image = self.anim[self.type][self.index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.direction = direction
        if self.direction == -1:
            temp = pygame.transform.flip(self.image, True, False)
            self.image = temp

        print(atk_type)

    def update(self):
        if self.type == 0:
            self.rect.x += (self.direction * self.speed)

            if self.rect.right < 0 or self.rect.left > SCREEN_WIDTH - 100:
                self.kill()
        elif self.type == 1:
            pass
        
