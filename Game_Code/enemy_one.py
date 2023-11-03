import pygame
import math

from Game_Asset_Code import *
from .lose import Lose
from .enemy_general_functions import EnemyGeneralFunctions
from .control_test import ControlTest

class EnemyOne:
    def __init__(self,level_1,enemy_1_level_1_rect,reset_locations,player_control):
        EnemyGeneralFunctions.__init__(self)
        Lose.__init__(self,level_1,player_lose_condition,reset_locations)
        self.level_1=level_1 ; self.camera_x_y=camera_x_y ; self.enemy_1_level_1_rect=enemy_1_level_1_rect ; self.skeleton_idle_number=skeleton_idle_number
        self.skeleton_run_number=skeleton_run_number ; self.skeleton_attack_number=skeleton_attack_number ; self.player_rect=player_rect
        self.enemy_1_x_movement=enemy_1_x_movement ; self.enemy_1_y_movement=enemy_1_y_movement ; self.player_control_index=player_control_index
        self.level_1_tile_set_rect=level_1_tile_set_rect ; self.player_attack_number=player_attack_number ; self.font=r"Assets\Misc\Fonts\Pixellari.ttf"
        self.red=(178,34,34) ; self.player_key=player_key ; self.player_health=player_health ; self.reset_locations=reset_locations ; self.skeleton_fall_number=skeleton_fall_number
        self.enemy_1_health=enemy_1_health ; self.enemy_1_fall_type=enemy_1_fall_type ; self.player_control=player_control ; self.player_control_cooldown=player_control_cooldown
        self.enemy_1_x_control_movement=enemy_1_x_control_movement ; self.enemy_1_y_control_movement=enemy_1_y_control_movement
        self.enemy_2_rects=enemy_2_rects

        self.enemy_1_level_1_x=enemy_1_level_1_x ; self.enemy_1_level_1_y=enemy_1_level_1_y

        if level_1:
            self.enemy_1_rects=enemy_1_level_1_rect
            self.tile_level=self.level_1_tile_set_rect
            self.enemy_rects_total=enemy_level_1_group_rect
            for idx,skeleton in enumerate(self.enemy_1_rects):
                self.skeleton_idle_number.append(0) 
                self.skeleton_run_number.append(0) 
                self.skeleton_attack_number.append(0)
                self.enemy_1_x_movement.append(0) 
                self.enemy_1_y_movement.append(0) 
                self.skeleton_fall_number.append(0)
                self.enemy_1_health.append(100) 
                self.enemy_1_fall_type.append(0)

    def distance(self):
        if any([self.level_1]):
            return EnemyGeneralFunctions.distance(self,self.enemy_1_rects)
        
    def iscontrolled(self):
        if any([self.level_1]) and self.player_control and self.player_control_cooldown[0]>0  and self.player_control_index[0][1]=="Enemy_1":
            return self.player_control_index[0][0]
    
    def enemy_index(self):
        if any([self.level_1]):
            for idx,skeleton in enumerate(self.enemy_1_rects):
                  if idx==self.player_control_index[0][0] and self.player_control_index[0][1]=="Enemy_1":
                      return skeleton

    def idle(self,key):
        self.enemy_1_distance=EnemyOne.distance(self)
        self.skeleton_idle=skeleton_idle; self.skeleton_idle_flip=skeleton_idle_flip

        if any([self.level_1]):
                
                if EnemyOne.enemy_index(self) not in self.enemy_1_rects:
                    EnemyGeneralFunctions.idle(self,self.enemy_1_distance,self.player_control_index,self.enemy_1_health,self.enemy_1_x_movement,self.enemy_1_y_movement,
                        self.skeleton_idle,self.skeleton_idle_flip,self.skeleton_idle_number,self.enemy_1_rects,0.10,4)
                
                if EnemyOne.enemy_index(self) in self.enemy_1_rects:
                    self.enemy_1_rects_control=[i for i in self.enemy_1_rects if i!=EnemyOne.enemy_index(self)]
                    self.enemy_1_distance_control=[i for idx, i in enumerate(self.enemy_1_distance) if idx!=self.player_control_index[0][0]]
                    
                    EnemyGeneralFunctions.idle_control(self,self.enemy_1_distance_control,self.player_control_index,self.enemy_1_health,self.enemy_1_x_movement,self.enemy_1_y_movement,
                        self.skeleton_idle,self.skeleton_idle_flip,self.skeleton_idle_number,self.enemy_1_rects_control,0.10,4)


    def run(self,key):
        self.enemy_1_distance=EnemyOne.distance(self)
        self.skeleton_run=skeleton_run; self.skeleton_run_flip=skeleton_run_flip

        if any([self.level_1]):
            print(self.enemy_1_distance)
            if EnemyOne.enemy_index(self) not in self.enemy_1_rects:
                    EnemyGeneralFunctions.move(self,self.enemy_1_distance,self.player_control_index,
                        self.enemy_1_health,self.enemy_1_rects,self.skeleton_run,self.skeleton_run_flip,self.skeleton_run_number,
                        self.enemy_1_x_movement,self.enemy_1_y_movement,0.10,7)
            
            if EnemyOne.enemy_index(self) in self.enemy_1_rects:
                    self.enemy_1_rects_control=[i for i in self.enemy_1_rects if i!=EnemyOne.enemy_index(self)]
                    self.enemy_1_distance_control=[i for idx, i in enumerate(self.enemy_1_distance) if idx!=self.player_control_index[0][0]]

                  #  print(self.enemy_1_rects_control,"NEW RECTS")
                  #  print(self.enemy_1_distance_control)

                    
                    EnemyGeneralFunctions.move_control(self,self.enemy_1_distance_control,self.player_control_index,
                        self.enemy_1_health,self.enemy_1_rects_control,self.skeleton_run,self.skeleton_run_flip,self.skeleton_run_number,
                        self.enemy_1_x_movement,self.enemy_1_y_movement,0.10,7)



    def attack(self,key):
        self.enemy_1_distance=EnemyOne.distance(self)
        self.skeleton_attack=skeleton_attack; self.skeleton_attack_flip=skeleton_attack_flip
        
        if any([self.level_1]):
            
           
            if EnemyOne.enemy_index(self) not in self.enemy_1_rects:
               
                EnemyGeneralFunctions.attack(self,self.enemy_1_distance,self.enemy_1_health,self.player_control_index,self.enemy_1_x_movement,self.enemy_1_y_movement,
                    self.skeleton_attack,self.skeleton_attack_flip,self.skeleton_attack_number,self.enemy_1_rects,self.enemy_1_fall_type,
                    0.10,7,25,55,30,30,self.player_health,200)
           
            if EnemyOne.enemy_index(self)  in self.enemy_1_rects:
                self.enemy_1_rects_control=[i for i in self.enemy_1_rects if i!=EnemyOne.enemy_index(self)]
                self.enemy_1_distance_control=[i for idx, i in enumerate(self.enemy_1_distance) if idx!=self.player_control_index[0][0]]
                

                EnemyGeneralFunctions.attack_control(self,self.enemy_1_distance_control,self.enemy_1_health,self.player_control_index,self.enemy_1_x_movement,self.enemy_1_y_movement,
                    self.skeleton_attack,self.skeleton_attack_flip,self.skeleton_attack_number,self.enemy_1_rects_control,self.enemy_1_fall_type,
                    0.10,7,25,55,30,30,self.player_health,200)

  

    def player_hit(self):
        if any([self.level_1]):
            EnemyGeneralFunctions.player_hit(self,self.font,self.red,self.enemy_1_distance,player_attack_number,self.enemy_1_health,self.enemy_1_rects,self.player_key,25)
     
    def fall(self):
        self.skeleton_fall=skeleton_fall  ; self.skeleton_fall_flip=skeleton_fall_flip
        if any([self.level_1]):
            EnemyGeneralFunctions.fall(self,self.enemy_1_rects,self.enemy_1_fall_type,self.skeleton_fall,self.skeleton_fall_flip,
                                    self.skeleton_fall_number,self.enemy_1_health,0.25,7,0,0,self.enemy_1_x_movement,self.enemy_1_y_movement)

    def reset_position(self):
        if self.reset_locations:
            if self.level_1:
                Lose.reset_positions_multiple(self,self.enemy_1_rects,self.enemy_1_level_1_x,self.enemy_1_level_1_y,self.enemy_1_health,100)
                return True

    def collision_with_object(self):
        if any([self.level_1]):
            return EnemyGeneralFunctions.collision_with_object(self,self.tile_level,self.enemy_1_rects)

    def collision_with_object_logic(self):
        if any([self.level_1]):
            self.collision=EnemyOne.collision_with_object(self)
            EnemyGeneralFunctions.collision_with_object_logic(self,self.enemy_1_rects,self.enemy_1_x_movement,self.enemy_1_y_movement,self.collision)

    
    
    def control_run(self,key):
        if any([self.level_1]) and self.player_control and self.player_control_cooldown[0]>0 and not key[pygame.K_e] and self.player_control_index[0][1]=="Enemy_1":
            if EnemyOne.enemy_index(self)  in self.enemy_1_rects:
                self.enemy_1_rects_control=[i for i in self.enemy_1_rects if i==EnemyOne.enemy_index(self)]
               # self.enemy_1_distance_control=[i for idx, i in enumerate(self.enemy_1_distance) if idx==self.player_control_index[0][0]]
                
                ControlTest.mechanic_walk(self,key,self.skeleton_run,self.enemy_1_rects_control,self.enemy_1_x_control_movement,self.enemy_1_y_control_movement,
                        self.skeleton_run_flip,self.skeleton_run_number,self.skeleton_idle,self.skeleton_idle_number,self.skeleton_idle_flip)

    def control_attack(self,key):
        if any([self.level_1]) and self.player_control and self.player_control_cooldown[0]>0  and self.player_control_index[0][1]=="Enemy_1":
            if EnemyOne.enemy_index(self) in self.enemy_1_rects:
                self.enemy_1_rects_control=[i for i in self.enemy_1_rects if i==EnemyOne.enemy_index(self)]
              #  self.enemy_1_distance_control=[i for idx, i in enumerate(self.enemy_1_distance) if idx==self.player_control_index[0][0]]
                ControlTest.mechanic_attack(self,key,self.skeleton_attack,self.enemy_1_rects_control,self.skeleton_attack_flip,
                                        self.skeleton_attack_number,self.enemy_1_x_control_movement,self.enemy_1_y_control_movement)
            
    def control_collision(self):
        if any([self.level_1]) and self.player_control and self.player_control_cooldown[0]>0  and self.player_control_index[0][1]=="Enemy_1":
            if EnemyOne.enemy_index(self) in self.enemy_1_rects:
                self.enemy_1_rects_control=[i for i in self.enemy_1_rects if i==EnemyOne.enemy_index(self)]
            #    self.enemy_1_distance_control=[i for idx, i in enumerate(self.enemy_1_distance) if idx==self.player_control_index[0][0]]
                ControlTest.mechanic_collision(self,self.tile_level,self.enemy_1_rects_control)
    
    def control_collision_object_logic(self):
        if any([self.level_1]) and self.player_control and self.player_control_cooldown[0]>0  and self.player_control_index[0][1]=="Enemy_1":
            if EnemyOne.enemy_index(self)  in self.enemy_1_rects:
                self.enemy_1_rects_control=[i for i in self.enemy_1_rects if i==EnemyOne.enemy_index(self)]
             #   self.enemy_1_distance_control=[i for idx, i in enumerate(self.enemy_1_distance) if idx==self.player_control_index[0][0]]
                ControlTest.mechanic_collision_logic(self,self.tile_level,self.enemy_1_rects_control,self.enemy_1_x_control_movement,self.enemy_1_y_control_movement,)


            
        
