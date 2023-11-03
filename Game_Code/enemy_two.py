import pygame
import math

from Game_Asset_Code import *
from .control import Control
from .lose import Lose
from .enemy_general_functions import EnemyGeneralFunctions
from .control_test import ControlTest

class EnemyTwo:
    def __init__(self,level_1,enemy_2_rects,reset_locations,player_control):
        EnemyGeneralFunctions.__init__(self)
        Lose.__init__(self,level_1,player_lose_condition,reset_locations)
        self.level_1=level_1 ; self.camera_x_y=camera_x_y ; self.brute_1_idle_number=brute_1_idle_number ; self.brute_1_run_number=brute_1_run_number
        self.player_rect=player_rect ; self.player_control_index=player_control_index ; self.enemy_2_level_1_rects=enemy_2_rects ; self.brute_1_attack_number=brute_1_attack_number
        self.enemy_2_level_1_x=enemy_2_level_1_x ; self.enemy_2_level_1_y=enemy_2_level_1_y ; self.enemy_2_x_movement=enemy_2_x_movement ; self.enemy_2_y_movement=enemy_2_y_movement
        self.player_control_cooldown=player_control_cooldown
        self.player_control=player_control
      #  self.enemy_rects=enemy_2_level_1_rects+enemy_2_rects 
      #  self.enemy_index=Control.enemy_index(self) ;
        self.level_1_tile_set_rect=level_1_tile_set_rect
        self.player_health=player_health ; self.reset_locations=reset_locations ; self.brute_1_fall_number=brute_1_fall_number ; self.enemy_2_health=enemy_2_health
        self.red=(178,34,34) ; self.enemy_2_fall_type=enemy_2_fall_type ; self.player_attack_number=player_attack_number ; self.player_key=player_key

        if self.level_1:
            self.tile_level=self.level_1_tile_set_rect
            self.enemy_2_rect=self.enemy_2_level_1_rects
            for i,num in enumerate(self.enemy_2_level_1_x):
                self.brute_1_idle_number.append(0) ; self.brute_1_run_number.append(0) ; self.brute_1_attack_number.append(0)
                self.enemy_2_x_movement.append(0) ; self.enemy_2_y_movement.append(0) ; self.enemy_2_fall_type.append(0)
                self.brute_1_fall_number.append(0) ; self.enemy_2_health.append(100)
                
    def distance(self):
        if any([self.level_1]):
            return EnemyGeneralFunctions.distance(self,self.enemy_2_rect)

    def idle(self):
        self.enemy_2_distance=EnemyTwo.distance(self)
        self.brute_1_idle=brute_1_idle ; self.brute_1_idle_flip=brute_1_idle_flip
        if any([self.level_1]):
            EnemyGeneralFunctions.idle(self,self.enemy_2_distance,self.player_control_index,self.enemy_2_health,self.enemy_2_x_movement,self.enemy_2_y_movement,
                                       self.brute_1_idle,self.brute_1_idle_flip,self.brute_1_idle_number,self.enemy_2_rect,0.10,4)

    def run(self):
        self.enemy_2_distance=EnemyTwo.distance(self)
        self.brute_1_run=brute_1_run ; self.brute_1_run_flip=brute_1_run_flip
        if any([self.level_1]):
            EnemyGeneralFunctions.move(self,self.enemy_2_distance,self.player_control_index,self.enemy_2_health,self.enemy_2_rect,
                                       self.brute_1_run,self.brute_1_run_flip,self.brute_1_run_number,self.enemy_2_x_movement,self.enemy_2_y_movement,
                                       0.10,7)

    def attack(self):
        self.enemy_2_distance=EnemyTwo.distance(self)
        self.brute_1_attack_1=brute_1_attack_1 ; self.brute_1_attack_flip_1=brute_1_attack_flip_1
        if any([self.level_1]):
            EnemyGeneralFunctions.attack(self,self.enemy_2_distance,self.enemy_2_health,self.player_control_index,self.enemy_2_x_movement,self.enemy_2_y_movement,
                self.brute_1_attack_1,self.brute_1_attack_flip_1,self.brute_1_attack_number,self.enemy_2_rect,self.enemy_2_fall_type,
                0.10,7,25,55,30,30,self.player_health,200)
        
    def player_hit(self):
        if any([self.level_1]):
                EnemyGeneralFunctions.player_hit(self,self.font,self.red,self.enemy_2_distance,player_attack_number,self.enemy_2_health,self.enemy_2_rect,self.player_key,25)

    def fall(self):
        self.brute_1_fall_1=brute_1_fall_1 ; self.brute_1_fall_flip_1=brute_1_fall_flip_1
        if any([self.level_1]):
            EnemyGeneralFunctions.fall(self,enemy_2_rects,self.enemy_2_fall_type,self.brute_1_fall_1,self.brute_1_fall_flip_1,
                                       self.brute_1_fall_number,self.enemy_2_health,0.25,7,0,-10,self.enemy_2_x_movement,self.enemy_2_y_movement)

    def reset_position(self):
        if self.reset_locations:
            if self.level_1:
                Lose.reset_positions_multiple(self,self.enemy_2_rect,self.enemy_2_level_1_x,self.enemy_2_level_1_y,self.enemy_2_health,100)
                return True

    def collision_with_object(self):
        if any([self.level_1]):
            return EnemyGeneralFunctions.collision_with_object(self,self.tile_level,self.enemy_2_rect)

    def collision_with_object_logic(self):
        if any([self.level_1]):
            self.collision=EnemyTwo.collision_with_object(self)
            EnemyGeneralFunctions.collision_with_object_logic(self,self.enemy_2_rect,self.enemy_2_x_movement,self.enemy_2_y_movement,self.collision)

    """def control_run(self,key):
        if any([self.level_1]) and self.player_control and self.player_control_cooldown[0]>0 and not key[pygame.K_e] and self.player_control_index[0][1]=="Enemy_2":
            ControlTest.mechanic_walk(self,key,self.brute_1_run,self.enemy_2_level_1_rects,self.enemy_2_x_movement,self.enemy_2_y_movement,
                self.brute_1_run_flip,self.brute_1_run_number,self.brute_1_idle,self.brute_1_idle_number,self.brute_1_idle_flip)

    def control_attack(self,key):
        if any([self.level_1]) and self.player_control and self.player_control_cooldown[0]>0  and self.player_control_index[0][1]=="Enemy_2":
            ControlTest.mechanic_attack(self,key,self.brute_1_attack_1,self.enemy_2_level_1_rects,self.brute_1_attack_flip_1,
                                        self.brute_1_attack_number,self.enemy_2_x_movement,self.enemy_2_y_movement)
            
    def control_collision(self):
        if any([self.level_1]) and self.player_control and self.player_control_cooldown[0]>0  and self.player_control_index[0][1]=="Enemy_2":
            ControlTest.mechanic_collision(self,self.tile_level,self.enemy_2_level_1_rects)
    
    def control_collision_object_logic(self):
        if any([self.level_1]) and self.player_control and self.player_control_cooldown[0]>0  and self.player_control_index[0][1]=="Enemy_2":
            ControlTest.mechanic_collision_logic(self,self.tile_level,self.enemy_2_level_1_rects,self.enemy_2_x_movement,self.enemy_2_y_movement)"""

   # def show_in_control(self):
        
