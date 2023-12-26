import pygame
import random
import math


from Game_Asset_Code import *
from .boss_general_fucntions import BossGeneralFunctions
from Game_Code.lose import Lose

class GeneralBoss:
    def __init__(self,level_3,level_3_player_talk_4,level_3_player_talk_3,reset_locations):
        Lose.__init__(self,level_1,player_lose_condition,reset_locations,level_2,level_3)
        self.level_3=level_3
        self.level_3_player_talk_4=level_3_player_talk_4
        self.level_3_player_talk_3=level_3_player_talk_3
        self.general_boss_rect=general_boss_rect
        self.general_boss_health=general_boss_health
        self.player_rect=player_rect
        self.camera_x_y=camera_x_y
        self.general_boss_x_movement=general_boss_x_movement
        self.general_boss_y_movement=general_boss_y_movement
        self.general_boss_attack_number=general_boss_attack_number
        self.general_boss_fall_type=general_boss_fall_type
        self.player_health=player_health
        self.general_boss_attack_type=general_boss_attack_type
        self.general_boss_health_icon=general_boss_health_icon
        self.orange_red=(164,36,28)
        self.level_3_tile_set_rect=level_3_tile_set_rect
        self.dialogue_click_list=dialogue_click_list
        self.player_x_movement=player_x_movement
        self.player_y_movement=player_y_movement
        self.general_boss_player_slow_down_number=general_boss_player_slow_down_number
        self.player_attack_number=player_attack_number
        self.reset_locations=reset_locations
        self.general_boss_level_3_x=general_boss_level_3_x
        self.general_boss_level_3_y=general_boss_level_3_y

    def distance(self):
        self.player_general_boss_distance=math.hypot(self.player_rect.x-self.general_boss_rect.x,self.player_rect.y-self.general_boss_rect.y)
        return self.player_general_boss_distance
    
    def walk_up_condition(self):
        self.general_boss_idle=general_boss_idle ; self.general_boss_idle_flip=general_boss_idle_flip ; self.general_boss_idle_number=general_boss_idle_number
        self.general_boss_move=general_boss_move ; self.general_boss_move_flip=general_boss_move_flip ; self.general_boss_move_number=general_boss_move_number
        self.distance=GeneralBoss.distance(self)

        if self.level_3 and self.level_3_player_talk_4 and self.dialogue_click_list[0]>=3:
            if self.distance>=200:
             BossGeneralFunctions.move(self,self.general_boss_rect,self.general_boss_move_flip,self.general_boss_move,self.general_boss_move_number,170,100,len(self.general_boss_move)+1,0.50,
                                      self.general_boss_x_movement,self.general_boss_y_movement,4,4,self.general_boss_attack_number,self.general_boss_health,self.player_health)               
            else:
                self.general_boss_x_movement[0]=0 ; self.general_boss_y_movement[0]=0
                BossGeneralFunctions.idle(self,self.general_boss_rect,self.general_boss_idle_flip,self.general_boss_idle,self.general_boss_idle_number,
                                        170,100,9,0.50,self.general_boss_health,self.player_health)
                
    def idle(self):
        if self.level_3 and not self.level_3_player_talk_4 and self.player_health[0]<0:
            self.general_boss_x_movement[0]=0 ; self.general_boss_y_movement[0]=0
            BossGeneralFunctions.idle(self,self.general_boss_rect,self.general_boss_idle_flip,self.general_boss_idle,self.general_boss_idle_number,
                                    170,100,9,0.50,self.general_boss_health,self.player_health)           
                
    def move(self):
        self.distance=GeneralBoss.distance(self)
        if self.level_3 and self.distance>100 and not self.level_3_player_talk_4:
            self.general_boss_attack_type[0]=random.randint(0,2)
            BossGeneralFunctions.move(self,self.general_boss_rect,self.general_boss_move_flip,self.general_boss_move,self.general_boss_move_number,170,100,7,0.50,
                                      self.general_boss_x_movement,self.general_boss_y_movement,4,4,self.general_boss_attack_number,self.general_boss_health,self.player_health)

    def attack(self):
        self.general_boss_attack_1=general_boss_attack_1 ; self.general_boss_attack_1_flip=general_boss_attack_1_flip ; self.general_boss_attack_1_number=general_boss_attack_1_number
        self.general_boss_attack_2=general_boss_attack_2 ; self.general_boss_attack_2_flip=general_boss_attack_2_flip ; self.general_boss_attack_2_number=general_boss_attack_2_number
        self.general_boss_attack_3=general_boss_attack_3 ; self.general_boss_attack_3_flip=general_boss_attack_3_flip ; self.general_boss_attack_3_number=general_boss_attack_3_number
        self.general_boss_attack_4=general_boss_attack_4 ; self.general_boss_attack_4_flip=general_boss_attack_4_flip ; self.general_boss_attack_4_number=general_boss_attack_4_number

        self.distance=GeneralBoss.distance(self)

        if self.general_boss_attack_type[0]==0:
            self.genreal_boss_attack=self.general_boss_attack_1 ; self.general_boss_attack_flip=self.general_boss_attack_1_flip ; self.player_health_reduction=250 ; self.max_attack_number=9 #25
        elif self.general_boss_attack_type[0]==1:
            self.genreal_boss_attack=self.general_boss_attack_2 ; self.general_boss_attack_flip=self.general_boss_attack_2_flip ; self.player_health_reduction=500 ; self.max_attack_number=12 #50
        elif self.general_boss_attack_type[0]==2:
            self.genreal_boss_attack=self.general_boss_attack_3 ; self.general_boss_attack_flip=self.general_boss_attack_3_flip ; self.player_health_reduction=700 ; self.max_attack_number=9 #70
        elif self.general_boss_attack_type[0]==3:
            self.genreal_boss_attack=self.general_boss_attack_4 ; self.general_boss_attack_flip=self.general_boss_attack_4_flip ; self.player_health_reduction=1500 ; self.max_attack_number=30 #150

        if self.general_boss_attack_number[0]+0.5>=self.max_attack_number:
        
            self.general_boss_attack_type[0]=random.randint(0,3)
            if self.general_boss_attack_type[0]>3: 
                self.general_boss_attack_type[0]=0

        if self.general_boss_attack_type[0]==3:
            self.general_boss_player_slow_down_number[0]=100
        else:
            self.general_boss_player_slow_down_number[0]-=1
            if self.general_boss_player_slow_down_number[0]<=0:
                self.general_boss_player_slow_down_number[0]=0
        
        if self.level_3 and self.distance<=100 and not self.level_3_player_talk_4:
            BossGeneralFunctions.attack(self,self.general_boss_rect,self.general_boss_attack_flip,self.genreal_boss_attack,self.general_boss_attack_number,170,100,self.max_attack_number,0.75,self.general_boss_x_movement,
                                        self.general_boss_y_movement,self.general_boss_fall_type,self.general_boss_health,self.player_health,self.player_health_reduction)
            
    
    def fall(self):
        self.general_boss_fall=general_boss_fall ; self.general_boss_fall_flip=general_boss_fall_flip ; self.general_boss_fall_number=general_boss_fall_number
        if self.level_3 and not self.level_3_player_talk_4:
            BossGeneralFunctions.fall(self,self.general_boss_rect,self.general_boss_fall,self.general_boss_fall_flip,self.general_boss_fall_number,0.50,18,self.general_boss_x_movement,self.general_boss_y_movement,
                                      170,100,self.general_boss_health,self.general_boss_fall_type)
            if self.general_boss_health[0]<=0:
                self.general_boss_player_slow_down_number[0]=0

        
    def health(self):
        if self.level_3 and not self.level_3_player_talk_4:
            BossGeneralFunctions.health(self,self.general_boss_health,1000,500,1000/500,self.general_boss_health_icon,self.orange_red,670,10,682,14,1)

    def player_hit(self,key):
        if self.level_3 and not self.level_3_player_talk_4:
            BossGeneralFunctions.player_hit(self,self.general_boss_health,self.player_attack_number,100,key)

    def reset_position(self):
        if self.level_3 and self.reset_locations:
            Lose.reset_positions(self,self.general_boss_rect,self.general_boss_level_3_x[0],self.general_boss_level_3_y[0])
            self.general_boss_player_slow_down_number[0]=0
            return True
    
    def collision_with_object(self):
        if self.level_3:
            return BossGeneralFunctions.collision_with_object(self,self.level_3_tile_set_rect,self.general_boss_rect)

    def collision_with_object_logic(self):
        if self.level_3:
            self.collision=GeneralBoss.collision_with_object(self)
            BossGeneralFunctions.collision_with_object_logic(self,self.general_boss_rect,self.general_boss_x_movement,self.collision,self.general_boss_y_movement)

    