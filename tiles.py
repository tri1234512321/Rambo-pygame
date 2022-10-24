import pygame
from map_settings import tile_size

class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos, size):
        super().__init__()
        self.image = pygame.Surface((size,size))
        # LXR is horizontal land
        # T
        # O is stone column
        # B
        # C is coin
        # W is water
        land_image = pygame.image.load("images/terrain_tiles.png")
        coin_image = pygame.image.load("images/coins/coin_tiles.png")
        water_image = pygame.image.load("images/decoration/water/1.png")
        if(tile_type == 'L'):
            self.image.blit(land_image,(0,0),(0,192,tile_size, tile_size))
        if(tile_type == 'X'):
            self.image.blit(land_image,(0,0),(64,192,tile_size, tile_size))
        if(tile_type == 'R'):
            self.image.blit(land_image,(0,0),(128,192,tile_size, tile_size))
        if(tile_type == 'T'):
            self.image.blit(land_image,(0,0),(192,0,tile_size, tile_size))
        if(tile_type == 'O'):
            self.image.blit(land_image,(0,0),(192,64,tile_size, tile_size))
        if(tile_type == 'B'):
            self.image.blit(land_image,(0,0),(192,192,tile_size, tile_size))
        if(tile_type == 'C'):
            self.image.blit(coin_image,(0,0),(0,0,tile_size,tile_size))
        if(tile_type == 'W'):
            self.image.blit(water_image,(0,0),(0,0,tile_size,tile_size))
        self.rect = self.image.get_rect(topleft = pos)
    
    def update(self, x_shift):
        self.rect.x += x_shift

