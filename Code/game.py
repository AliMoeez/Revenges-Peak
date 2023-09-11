import pygame,sys
from pytmx.util_pygame import load_pygame
from general_assets import *
from player_assets import *
from boss_assets import *
from enemy_assets import *

class Menu:
    def __init__(self,level_screen,level_1):
        self.WHITE=(205,205,205) ; self.level_screen=level_screen ; self.level_1=level_1
        self.backround_tile_set=backround_tile_set

    def main_menu(self):
        if not self.level_screen and not any([self.level_1]):
            for layer in self.backround_tile_set:
                for tile in layer.tiles():
                    x_val=tile[0]*32 ; y_val=tile[1]*32
                    SCREEN.blit(tile[2],(x_val,y_val))

class LevelOne(Menu):
    def __init__(self,camera_x_y):
        super().__init__(level_screen,level_1)
        self.camera_x_y=camera_x_y ; self.player_rect=player_rect ; self.test_tile_set=test_tile_set

    def level_one(self):
        if self.level_1:
            self.camera_x_y[0]+=self.player_rect.x-self.camera_x_y[0]
            self.camera_x_y[1]+=self.player_rect.y-self.camera_x_y[1]
            for layer in self.test_tile_set:
                for tile in layer.tiles():
                    x_val=tile[0]*32 ; y_val=tile[1]*32
                    SCREEN.blit(tile[2],(x_val-self.camera_x_y[0],y_val-self.camera_x_y[1]))

class Player(LevelOne):
    def __init__(self,player_x,player_y,player_width,player_height,player_rect):
        super().__init__(camera_x_y)
        self.player_x=player_x ; self.player_y=player_y ; self.player_width=player_width ; self.player_height=player_height
        self.player_rect=player_rect
        self.player_x_movement=player_x_movement ; self.player_y_movement=player_y_movement

    def idle(self):
        self.player_idle=player_idle ; self.player_idle_flip=player_idle_flip
        if self.level_1:
            if not key[pygame.K_d] and not key[pygame.K_a] and not key[pygame.K_w] and not key[pygame.K_s]:
                SCREEN.blit(self.player_idle[0],(self.player_rect.x-self.camera_x_y[0],self.player_rect.y-self.camera_x_y[1]))
            SCREEN.blit(frost_brute_idle_1,(200-self.camera_x_y[0],200-self.camera_x_y[1]))
            SCREEN.blit(skeleton_1_idle_1,(400-self.camera_x_y[0],200-self.camera_x_y[1]))

    def move(self):
        self.player_run=player_run ; self.player_run_flip=player_run_flip ; self.player_run_number=player_run_number
        if self.level_1:
            if key[pygame.K_d]:
                self.player_x_movement[0]=2
                if key[pygame.K_w]:
                    self.player_x_movement[0]=1 ; self.player_y_movement[0]=-1
            elif key[pygame.K_w]: self.player_y_movement[0]=-2
            elif key[pygame.K_a]:
                self.player_x_movement[0]=-2
                if key[pygame.K_s]:
                    self.player_x_movement[0]=-1 ; self.player_y_movement[0]=1
            elif key[pygame.K_s]: self.player_y_movement[0]=2
            else: 
                self.player_x_movement[0]=0 
                self.player_y_movement[0]=0
            if key[pygame.K_d] or key[pygame.K_d] and key[pygame.K_w] or key[pygame.K_w]:
                SCREEN.blit(self.player_run[int(self.player_run_number[0])//2],(self.player_rect.x-self.camera_x_y[0],self.player_rect.y-self.camera_x_y[1]))
            if key[pygame.K_a] or key[pygame.K_a] and key[pygame.K_s] or key[pygame.K_s]:
                SCREEN.blit(self.player_run_flip[int(self.player_run_number[0])//2],(self.player_rect.x-self.camera_x_y[0],self.player_rect.y-self.camera_x_y[1]))

            self.player_run_number[0]+=0.10
            if self.player_run_number[0]>10:self.player_run_number[0]=0

    def collision(self):
        if self.level_1:
            self.player_rect.x+=self.player_x_movement[0]
            self.player_rect.y+=self.player_y_movement[0]

while run:
    SCREEN.fill((0,0,0))
  #  x=clock.tick(FPS)
    
    key=pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit() 
            sys.exit()

    menu=Menu(level_screen,level_1)
    menu.main_menu()

    levelone=LevelOne(camera_x_y)
    levelone.level_one()

    player=Player(player_x,player_y,player_width,player_height,player_rect)
    player.idle()
    player.move()
    player.collision()

    pygame.display.update()

