import pygame
import math

from Game_Asset_Code import *
from .level_one import LevelOne

class Player(LevelOne):
    def __init__(self,player_x,player_y,player_width,player_height,player_rect,level_1):
        self.player_x=player_x ; self.player_y=player_y ; self.player_width=player_width ; self.player_height=player_height ; self.player_rect=player_rect ; self.player_x_movement=player_x_movement ; self.player_y_movement=player_y_movement
        self.camera_x_y=camera_x_y  ; self.level_1=level_1 ;  self.level_screen=level_screen ; self.player_key=player_key
        self.level_1_tile_set_rect=level_1_tile_set_rect

    def idle(self,key):
        self.player_idle_list=player_idle_list ; self.player_idle_list_flip=player_idle_list_flip ; self.player_idle_number=player_idle_number
        if self.level_1:
            pygame.draw.rect(SCREEN,(200,200,200),pygame.Rect(self.player_rect.x-self.camera_x_y[0],self.player_rect.y-self.camera_x_y[1],32,64))
            if (not key[pygame.K_a] and not key[pygame.K_d] and not key[pygame.K_w] and not key[pygame.K_s])  or (key[pygame.K_a] and key[pygame.K_d]) or (key[pygame.K_w] and key[pygame.K_s]):
                if self.player_key[-1]=="d": SCREEN.blit(self.player_idle_list[int(self.player_idle_number[0])//2],(self.player_rect.x-self.camera_x_y[0]-40,self.player_rect.y-self.camera_x_y[1]-40))
                else: SCREEN.blit(self.player_idle_list_flip[int(self.player_idle_number[0])//2],(self.player_rect.x-self.camera_x_y[0]-40,self.player_rect.y-self.camera_x_y[1]-40))
            
            if len(self.player_key)>5: del self.player_key[0]
            
            self.player_idle_number[0]+=0.15
            if self.player_idle_number[0]>7: self.player_idle_number[0]=0
    
            SCREEN.blit(frost_brute_idle_1,(200-self.camera_x_y[0],200-self.camera_x_y[1]))
            SCREEN.blit(skeleton_1_idle_1,(400-self.camera_x_y[0],200-self.camera_x_y[1]))

    def move(self,key):
        self.player_run_list=player_run_list ; self.player_run_list_flip=player_run_list_flip ; self.player_run_number=player_run_number
        if self.level_1:
            if key[pygame.K_d] and not key[pygame.K_a]:
                SCREEN.blit(self.player_run_list[int(self.player_run_number[0])//2],(self.player_rect.x-self.camera_x_y[0]-40,self.player_rect.y-self.camera_x_y[1]-40))
                self.player_x_movement[0]=3 ; self.player_key.append("d")
                if key[pygame.K_w]:
                    self.player_x_movement[0]=math.sqrt(3) ; self.player_y_movement[0]=-math.sqrt(3)
                elif key[pygame.K_s]:
                    self.player_x_movement[0]=math.sqrt(3) ; self.player_y_movement[0]=math.sqrt(3)

            elif key[pygame.K_w] and not key[pygame.K_s]: 
                self.player_y_movement[0]=-3
                if self.player_key[-1]=="d": SCREEN.blit(self.player_run_list[int(self.player_run_number[0])//2],(self.player_rect.x-self.camera_x_y[0]-40,self.player_rect.y-self.camera_x_y[1]-40))
                else: SCREEN.blit(self.player_run_list_flip[int(self.player_run_number[0])//2],(self.player_rect.x-self.camera_x_y[0]-40,self.player_rect.y-self.camera_x_y[1]-40))

            elif key[pygame.K_a] and not key[pygame.K_d]:
                SCREEN.blit(self.player_run_list_flip[int(self.player_run_number[0])//2],(self.player_rect.x-self.camera_x_y[0]-40,self.player_rect.y-self.camera_x_y[1]-40))
                self.player_x_movement[0]=-3 ; self.player_key.append("a")
                if key[pygame.K_w]:
                    self.player_x_movement[0]=-math.sqrt(3); self.player_y_movement[0]=-math.sqrt(3)
                elif key[pygame.K_s]:
                    self.player_x_movement[0]=-math.sqrt(3) ; self.player_y_movement[0]=math.sqrt(3)

            elif key[pygame.K_s] and not key[pygame.K_w]: 
                self.player_y_movement[0]=3
                if self.player_key[-1]=="d": SCREEN.blit(self.player_run_list[int(self.player_run_number[0])//2],(self.player_rect.x-self.camera_x_y[0]-40,self.player_rect.y-self.camera_x_y[1]-40))
                else: SCREEN.blit(self.player_run_list_flip[int(self.player_run_number[0])//2],(self.player_rect.x-self.camera_x_y[0]-40,self.player_rect.y-self.camera_x_y[1]-40))
            
            else: 
                self.player_x_movement[0]=0 ; self.player_y_movement[0]=0
    
            self.player_run_number[0]+=0.15
            if self.player_run_number[0]>7:self.player_run_number[0]=0

    def collision_with_object(self):
        if self.level_1:
            self.tile_hit=[]
            for tiles in self.level_1_tile_set_rect:
                if self.player_rect.colliderect(tiles):
                    self.tile_hit.append(tiles)
            return self.tile_hit
                    
    def collision_with_object_logic(self):
        if self.level_1:
            self.player_rect.x+=self.player_x_movement[0]
            collision=Player.collision_with_object(self)
            for tile in collision:
                if self.player_x_movement[0]>0:
                    self.player_rect.right=tile.left
                if self.player_x_movement[0]<0:
                    self.player_rect.left=tile.right
            self.player_rect.y+=self.player_y_movement[0]
            collision=Player.collision_with_object(self)
            for tile in collision:
                if self.player_y_movement[0]>0:
                    self.player_rect.bottom=tile.top
                if self.player_y_movement[0]<0:
                    self.player_rect.top=tile.bottom


