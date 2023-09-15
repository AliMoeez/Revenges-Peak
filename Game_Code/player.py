import pygame

from Game_Asset_Code import *
from .level_one import LevelOne

class Player(LevelOne):
    def __init__(self,player_x,player_y,player_width,player_height,player_rect,level_1):
        self.player_x=player_x ; self.player_y=player_y ; self.player_width=player_width ; self.player_height=player_height ; self.player_rect=player_rect ; self.player_x_movement=player_x_movement ; self.player_y_movement=player_y_movement
        self.camera_x_y=camera_x_y  ; self.level_1=level_1 ;  self.level_screen=level_screen

    def idle(self,key):
        self.player_idle_list=player_idle_list ; self.player_idle_list_flip=player_idle_list_flip ; self.player_idle_number=player_idle_number
        if self.level_1:
            if not key[pygame.K_d] and not key[pygame.K_a] and not key[pygame.K_w] and not key[pygame.K_s]:
                SCREEN.blit(self.player_idle_list[int(self.player_idle_number[0])//2],(self.player_rect.x-self.camera_x_y[0],self.player_rect.y-self.camera_x_y[1]))
            self.player_idle_number[0]+=0.15
            if self.player_idle_number[0]>7: self.player_idle_number[0]=0
    
            SCREEN.blit(frost_brute_idle_1,(200-self.camera_x_y[0],200-self.camera_x_y[1]))
            SCREEN.blit(skeleton_1_idle_1,(400-self.camera_x_y[0],200-self.camera_x_y[1]))

    def move(self,key):
        if self.level_1:
            pass
        """    if key[pygame.K_d]:
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
            if self.player_run_number[0]>10:self.player_run_number[0]=0"""

    def collision(self):
        if self.level_1:
            self.player_rect.x+=self.player_x_movement[0]
            self.player_rect.y+=self.player_y_movement[0]
