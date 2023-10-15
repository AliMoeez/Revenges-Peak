import pygame
import math

from Game_Asset_Code import *
from .control import Control
from .lose import Lose
from .enemy_general_functions import EnemyGeneralFunctions

class EnemyTwo:
    def __init__(self,level_1,enemy_2_level_1_rect,reset_locations):
        EnemyGeneralFunctions.__init__(self)
        Lose.__init__(self,level_1,player_lose_condition,reset_locations)
        self.level_1=level_1 ; self.camera_x_y=camera_x_y ; self.brute_1_idle_number=brute_1_idle_number ; self.brute_1_run_number=brute_1_run_number
        self.player_rect=player_rect ; self.player_control_index=player_control_index ; self.enemy_2_rects=enemy_2_rects ; self.brute_1_attack_number=brute_1_attack_number
        self.enemy_2_level_1_x=enemy_2_level_1_x ; self.enemy_2_level_1_y=enemy_2_level_1_y ; self.enemy_2_x_movement=enemy_2_x_movement ; self.enemy_2_y_movement=enemy_2_y_movement
        self.enemy_rects=enemy_1_level_1_rect+enemy_2_rects ; self.enemy_index=Control.enemy_index(self) ; self.level_1_tile_set_rect=level_1_tile_set_rect
        self.player_health=player_health ; self.reset_locations=reset_locations ; self.brute_1_fall_number=brute_1_fall_number ; self.enemy_2_health=enemy_2_health
        self.red=(178,34,34) ; self.enemy_2_fall_type=enemy_2_fall_type ; self.player_attack_number=player_attack_number ; self.player_key=player_key

        if self.level_1:
            self.tile_level=self.level_1_tile_set_rect
            for i,num in enumerate(self.enemy_2_level_1_x): 
                self.enemy_2_rects.append(pygame.Rect(self.enemy_2_level_1_x[i],self.enemy_2_level_1_y[i],40,70))
                self.brute_1_idle_number.append(0) ; self.brute_1_run_number.append(0) ; self.brute_1_attack_number.append(0)
                self.enemy_2_x_movement.append(0) ; self.enemy_2_y_movement.append(0) ; self.enemy_2_fall_type.append(0)
                self.brute_1_fall_number.append(0) ; self.enemy_2_health.append(100)

            if len(self.enemy_2_rects)>len(self.enemy_2_level_1_x):
                del self.enemy_2_rects[-1]

    def distance(self):
        if any([self.level_1]):
            return EnemyGeneralFunctions.distance(self,self.enemy_2_rects)

    def idle(self):
        self.enemy_2_distance=EnemyTwo.distance(self)
        self.brute_1_idle=brute_1_idle ; self.brute_1_idle_flip=brute_1_idle_flip
        if any([self.level_1]):
            EnemyGeneralFunctions.idle(self,self.enemy_2_distance,self.player_control_index,self.enemy_2_health,self.enemy_2_x_movement,self.enemy_2_y_movement,
                                       self.brute_1_idle,self.brute_1_idle_flip,self.brute_1_idle_number,self.enemy_2_rects,0.10,4)

    def run(self):
        self.enemy_2_distance=EnemyTwo.distance(self)
        self.brute_1_run=brute_1_run ; self.brute_1_run_flip=brute_1_run_flip
        if any([self.level_1]):
            EnemyGeneralFunctions.move(self,self.enemy_2_distance,self.player_control_index,self.enemy_2_health,self.enemy_2_rects,
                                       self.brute_1_run,self.brute_1_run_flip,self.brute_1_run_number,self.enemy_2_x_movement,self.enemy_2_y_movement,
                                       0.10,7)

    def attack(self):
        self.enemy_2_distance=EnemyTwo.distance(self)
        self.brute_1_attack_1=brute_1_attack_1 ; self.brute_1_attack_flip_1=brute_1_attack_flip_1
        if any([self.level_1]):
            for idx,distance in enumerate(self.enemy_2_distance):
                if not self.enemy_index==idx and distance<100 and self.enemy_2_health[idx]>0:
                    self.enemy_2_x_movement[idx]=0 ; self.enemy_2_y_movement[idx]=0
                    if self.player_rect.x>=self.enemy_2_rects[idx].x:
                        SCREEN.blit(self.brute_1_attack_1[int(self.brute_1_attack_number[idx]//2)],(self.enemy_2_rects[idx].x-self.camera_x_y[0]-25,self.enemy_2_rects[idx].y-self.camera_x_y[1]-30))
                        self.enemy_2_fall_type[idx]==1
                    else:
                        SCREEN.blit(self.brute_1_attack_flip_1[int(self.brute_1_attack_number[idx]//2)],(self.enemy_2_rects[idx].x-self.camera_x_y[0]-55,self.enemy_2_rects[idx].y-self.camera_x_y[1]-30))
                        self.enemy_2_fall_type[idx]=2
                    self.brute_1_attack_number[idx]+=0.10
                    if self.brute_1_attack_number[idx]>7: 
                        self.brute_1_attack_number[idx]=0
                        self.player_health[0]-=10
        
    def player_hit(self):
        if any([self.level_1]):
            self.font_hit=pygame.font.Font(self.font,15) 
            self.font_hit_render=self.font_hit.render("-25",True,self.red) 
            for idx,distance in enumerate(self.enemy_2_distance):
                if self.player_attack_number[0]>6.0 and distance<100 and self.enemy_2_health[idx]>0:
                    if (self.player_rect.x<=self.enemy_2_rects[idx].x and self.player_key[-1]=="d"):
                        SCREEN.blit(self.font_hit_render,(self.enemy_2_rects[idx].x-self.camera_x_y[0]+25,self.enemy_2_rects[idx].y-self.camera_x_y[1]))
                        self.enemy_2_health[idx]-=50
                    if (self.player_rect.x>=self.enemy_2_rects[idx].x and self.player_key[-1]=="a"):
                        SCREEN.blit(self.font_hit_render,(self.enemy_2_rects[idx].x-self.camera_x_y[0]+25,self.enemy_2_rects[idx].y-self.camera_x_y[1]))
                        self.enemy_2_health[idx]-=50

    def fall(self):
        self.brute_1_fall_1=brute_1_fall_1 ; self.brute_1_fall_flip_1=brute_1_fall_flip_1
        if any([self.level_1]):
            EnemyGeneralFunctions.fall(self,enemy_2_rects,self.enemy_2_fall_type,self.brute_1_fall_1,self.brute_1_fall_flip_1,
                                       self.brute_1_fall_number,self.enemy_2_health,0.25,7,0,-10)

    def reset_position(self):
        if self.reset_locations:
            if self.level_1:
                Lose.reset_positions_multiple(self,self.enemy_2_rects,self.enemy_2_level_1_x,self.enemy_2_level_1_y)
                return True

    def collision_with_object(self):
        if any([self.level_1]):
            self.tile_hit=[]
            for tile in self.tile_level:
                for idx,enemy_2 in enumerate(self.enemy_2_rects):
                    if enemy_2.colliderect(tile):
                        self.tile_hit.append(tile)
            return self.tile_hit

    def collision_with_object_logic(self):
        if any([self.level_1]):
            for idx,brute in enumerate(self.enemy_2_rects):
                self.enemy_2_rects[idx].x+=self.enemy_2_x_movement[idx]
                self.collision=EnemyTwo.collision_with_object(self)
                for tile in self.collision:
                    if self.enemy_2_x_movement[idx]>0:
                        self.enemy_2_rects[idx].right=tile.left
                    if self.enemy_2_x_movement[idx]<0:
                        self.enemy_2_rects[idx].left=tile.right
                self.enemy_2_rects[idx].y+=self.enemy_2_y_movement[idx]
                self.collision=EnemyTwo.collision_with_object(self)
                for tile in self.collision:
                    if self.enemy_2_y_movement[idx]>0:
                        self.enemy_2_rects[idx].bottom=tile.top
                    if self.enemy_2_y_movement[idx]<0:
                        self.enemy_2_rects[idx].top=tile.bottom