import pygame
import math
import random
import numpy as np

from Game_Asset_Code import *
from .boss_general_fucntions import BossGeneralFunctions


class FinalBoss:
    def __init__(self,level_4,level_4_player_talk_2):
        self.level_4=level_4
        self.final_boss_rect=final_boss_rect
        self.camera_x_y=camera_x_y
        self.final_boss_health=final_boss_health
        self.player_health=player_health
        self.player_rect=player_rect
        self.final_boss_x_movement=final_boss_x_movement
        self.final_boss_y_movement=final_boss_y_movement
        self.elder_attack_number_level_4=elder_attack_number_level_4
        self.elder_max_attack_list=elder_max_attack_list
        self.elder_boss_fall_type=elder_boss_fall_type
        self.elder_attack_list_type=elder_attack_list_type
        self.elder_boss_attack_cooldown=elder_boss_attack_cooldown
        self.level_4_tile_set_rect=level_4_tile_set_rect
        self.elder_attack_poison_effect=elder_attack_poison_effect
        self.level_4_player_talk_2=level_4_player_talk_2
        self.final_boss_player_stop=final_boss_player_stop
        self.player_boss_talk=player_boss_talk
        self.dialogue_click_list=dialogue_click_list
        self.dialogue_objective_list=dialogue_objective_list

        """        self.final_boss_support_x=final_boss_support_x
                self.final_boss_support_y=final_boss_support_y
                self.final_boss_support_fall_type=final_boss_support_fall_type


        final_boss_support_fall_type=[]

        final_boss_support_health=[]

        final_boss_support_x_movement=[]
        final_boss_support_y_movement=[]


        final_boss_support_rect=[]"""


    def distance(self):
        self.distance_list=[]
        self.distance_to_boss=math.hypot(self.player_rect.x-self.final_boss_rect.x,self.player_rect.y-self.final_boss_rect.y)
        self.distance_list.append(self.distance_to_boss)
        return self.distance_list[0]
    
    def distance_player_boss_dialogue(self):
        self.distance_dialogue=math.hypot(self.player_rect.x-3250,self.player_rect.y-730)
        return self.distance_dialogue

    def initial_state(self):
        self.distance=FinalBoss.distance(self) ; self.dialogue_distance=FinalBoss.distance_player_boss_dialogue(self)
        self.elder_idle_list=elder_idle_list ; self.elder_idle_list_flip=elder_idle_list_flip ; self.elder_idle_number_level_4=elder_idle_number_level_4
        self.elder_run_list=elder_run_list ; self.elder_run_list_flip=elder_run_list_flip ; self.elder_run_number_level_4=elder_run_number_level_4
        if self.level_4 and self.level_4_player_talk_2 and self.dialogue_distance<200:

            if self.distance>700: self.boss_x_movement=100
            elif self.distance<=700 and self.distance>100: self.boss_x_movement=2
            else: self.boss_x_movement=0

            if self.distance>100:
                BossGeneralFunctions.move(self,self.final_boss_rect,self.elder_run_list_flip,self.elder_run_list,self.elder_run_number_level_4,65,35,9,0.25,
                                      self.final_boss_x_movement,self.final_boss_y_movement,self.boss_x_movement,2,self.elder_attack_number_level_4,self.final_boss_health,self.player_health)
                self.final_boss_player_stop[0]=1
            else:
                self.final_boss_x_movement[0]=0 ; self.final_boss_y_movement[0]=0
                BossGeneralFunctions.idle(self,self.final_boss_rect,self.elder_idle_list_flip,self.elder_idle_list,self.elder_idle_number_level_4,65,35,7,0.15,
                                      self.final_boss_health,self.player_health)
                self.final_boss_player_stop[0]=0

    def move(self):
        self.distance=FinalBoss.distance(self)
        if self.level_4 and self.distance<=400 and self.distance>100 and not self.level_4_player_talk_2:
            BossGeneralFunctions.move(self,self.final_boss_rect,self.elder_run_list_flip,self.elder_run_list,self.elder_run_number_level_4,65,35,9,0.25,
                                      self.final_boss_x_movement,self.final_boss_y_movement,2,2,self.elder_attack_number_level_4,self.final_boss_health,self.player_health)

    def attack_logic(self):
        self.elder_attacks_1_list=elder_attacks_1_list ; self.elder_attacks_1_list_flip=elder_attacks_1_list_flip ; self.elder_attacks_1_number_level_4=elder_attacks_1_number_level_4
        self.elder_attacks_2_list=elder_attacks_2_list ; self.elder_attacks_2_list_flip=elder_attacks_2_list_flip ; self.elder_attacks_2_number_level_4=elder_attacks_2_number_level_4

        if self.elder_attack_list_type[0]==0:
            self.elder_attack_list=self.elder_attacks_1_list ; self.elder_attack_list_flip=self.elder_attacks_1_list_flip ; self.elder_attack_number=self.elder_attacks_1_number_level_4 ; self.elder_max_attack_list[0]=8 ; self.damage=0
        
        if self.elder_attack_list_type[0]==1:
            self.elder_attack_list=self.elder_attacks_2_list ; self.elder_attack_list_flip=self.elder_attacks_2_list_flip ; self.elder_attack_number=self.elder_attacks_2_number_level_4 ; self.elder_max_attack_list[0]=8 ; self.damage=0
        
        if self.elder_attack_number[0]>=self.elder_max_attack_list[0]-0.5: 
            self.elder_attack_list_type[0]=np.random.choice([0,1],1,p=[0.7,0.3])[0] ; self.elder_boss_attack_cooldown[0]=0 ; self.elder_idle_number_level_4[0]=2
        
        if self.elder_boss_attack_cooldown[0]<10:
            self.elder_boss_attack_cooldown[0]+=0.50 ; self.elder_attack_number[0]=0

    def attack(self):
        self.distance=FinalBoss.distance(self)
        if self.level_4 and self.distance<=100 and self.elder_boss_attack_cooldown[0]==10 and not self.level_4_player_talk_2:
            BossGeneralFunctions.attack(self,self.final_boss_rect,self.elder_attack_list_flip,self.elder_attack_list,self.elder_attack_number,65,35,self.elder_max_attack_list[0],
                                        0.25,self.final_boss_x_movement,self.final_boss_y_movement,self.elder_boss_fall_type,self.final_boss_health,self.player_health,self.damage)

    def poison_effect(self):
        if self.level_4 and self.elder_attack_list_type[0]==1 and self.elder_attack_number[0]>=self.elder_max_attack_list[0]-0.5: 
            self.elder_attack_poison_effect[0]=0
        
        if self.elder_attack_poison_effect[0]>=0 and self.elder_attack_poison_effect[0]<10:
            self.elder_attack_poison_effect[0]+=0.05 ; self.player_health[0]-=1
        else: 
            self.elder_attack_poison_effect[0]=10

    def support_list(self):
        if self.level_4 and self.final_boss_health[0]<=500:
            pass


    def call_support(self):
        if self.level_4 and self.final_boss_health[0]<=500:
            pass


    def health(self):
        pass

    def fall(self):
        pass

    def collision_with_object(self):
        if self.level_4:
            self.collision=BossGeneralFunctions.collision_with_object(self,self.level_4_tile_set_rect,self.final_boss_rect)
            return self.collision

    def collision_with_object_logic(self):
        if self.level_4:
            self.collision=FinalBoss.collision_with_object(self)
            BossGeneralFunctions.collision_with_object_logic(self,self.final_boss_rect,self.final_boss_x_movement,self.collision,self.final_boss_y_movement)