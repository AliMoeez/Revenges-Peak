import pygame
import math

from Game_Asset_Code import *
from .enemy_one import EnemyOne

class Control(EnemyOne):
    def __init__(self,level_1,player_control,player_control_index):
        super().__init__(level_1,enemy_1_level_1_rect)
        self.player_rect=player_rect ; self.enemy_1_level_1_rect=enemy_1_level_1_rect ; self.level_1=level_1 ; self.player_control_index=player_control_index
        self.player_control=player_control ; self.player_control_cooldown=player_control_cooldown ; self.enemy_1_level_1_rect=enemy_1_level_1_rect 
        self.camera_x_y=camera_x_y ; self.enemy_run_number=enemy_run_number ; self.enemy_idle_number=enemy_idle_number
        if self.level_1:
            self.enemy_rects=self.enemy_1_level_1_rect
            self.enemy_rects_type=[]
            for idx,enemy_1 in enumerate(self.enemy_1_level_1_rect):
                self.enemy_rects_type.append("Enemy_1")

    def distance(self):
        if any([self.level_1]):
            self.player_enemy_distance=[]
            for idx,enemy in enumerate(self.enemy_rects):
                self.player_enemy_distance.append(math.hypot(self.player_rect.x-self.enemy_rects[idx].x,self.player_rect.y-self.enemy_rects[idx].y))
            return self.player_enemy_distance
        
    def enemy_definition(self):
        if any([self.level_1]):
            for idx,enemy in enumerate(self.enemy_rects):
                if self.player_control_index[0]==idx:
                    self.enemy_walk=skeleton_run ; self.enemy_walk_flip=skeleton_run_flip
                    self.enemy_idle=skeleton_idle

    def mechanic_idle(self,key):
        if any([self.level_1]) and self.player_control and self.player_control_cooldown[0]>0:
            if not key[pygame.K_e] or not key[pygame.K_d] or not key[pygame.K_a] or not key[pygame.K_w] or not key[pygame.K_s]:
                SCREEN.blit(self.enemy_idle[int(self.enemy_idle_number[0]//2)],(self.enemy_rects[self.player_control_index[0]].x-self.camera_x_y[0],self.enemy_rects[self.player_control_index[0]].y-self.camera_x_y[1]))
                self.enemy_idle_number[0]+=0.15
                if self.enemy_idle_number[0]>len(self.enemy_idle)+1:
                    self.enemy_idle_number[0]=0

    def mechanic_walk(self,key):
        self.distance_player=Control.distance(self)
        if any([self.level_1]) and self.player_control and self.player_control_cooldown[0]>0:
            for idx,enemy in enumerate(self.enemy_rects):
                if not key[pygame.K_e]:
                    if key[pygame.K_d] and not key[pygame.K_a]:
                        self.enemy_rects[self.player_control_index[0]].x+=2
                        SCREEN.blit(self.enemy_walk[int(self.enemy_run_number[0]//2)],(self.enemy_rects[self.player_control_index[0]].x-self.camera_x_y[0],self.enemy_rects[self.player_control_index[0]].y-self.camera_x_y[1]))
                    if key[pygame.K_a] and not key[pygame.K_d]:
                        self.enemy_rects[self.player_control_index[0]].x-=2
                        SCREEN.blit(self.enemy_walk_flip[int(self.enemy_run_number[0]//2)],(self.enemy_rects[self.player_control_index[0]].x-self.camera_x_y[0],self.enemy_rects[self.player_control_index[0]].y-self.camera_x_y[1]))
                    if key[pygame.K_w] and not key[pygame.K_s]:
                        self.enemy_rects[self.player_control_index[0]].y-=2
                    if key[pygame.K_s] and not key[pygame.K_w]:
                        self.enemy_rects[self.player_control_index[0]].y+=2
                    self.enemy_run_number[0]+=0.15
                    if self.enemy_run_number[0]>len(self.enemy_walk)+1:
                        self.enemy_run_number[0]=0

    def mechanic_attack(self,key):
        if any([self.level_1]) and self.player_control and self.player_control_cooldown[0]>0:
            if key[pygame.K_e]:
                pass
   
    def print_statement(self):
        self.distance_player=Control.distance(self)
        

               



