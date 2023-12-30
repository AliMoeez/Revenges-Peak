import pygame
import math
import random

from Game_Asset_Code import *
from .boss_general_fucntions import BossGeneralFunctions


class FinalBoss:
    def __init__(self,level_4):
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


    def distance(self):
        self.distance=math.hypot(self.player_rect.x-self.final_boss_rect.x,self.player_rect.y-self.final_boss_rect.y)
        return self.distance

    def intial_state(self):
        pass

    def idle(self):
        self.distance=FinalBoss.distance(self)
        self.elder_idle_list=elder_idle_list ; self.elder_idle_list_flip=elder_idle_list_flip ; self.elder_idle_number_level_4=elder_idle_number_level_4
      #  if self.level_4:
      #       pygame.draw.rect(SCREEN,(100,100,100),pygame.Rect(self.final_boss_rect.x-self.camera_x_y[0],self.final_boss_rect.y-self.camera_x_y[1],50,100),width=1)
        if self.level_4 and self.distance>400:
            BossGeneralFunctions.idle(self,self.final_boss_rect,self.elder_idle_list_flip,self.elder_idle_list,self.elder_idle_number_level_4,65,35,7,0.25,
                                      self.final_boss_health,self.player_health)
            
    def move(self):
        self.distance=FinalBoss.distance(self)
        self.elder_run_list=elder_run_list ; self.elder_run_list_flip=elder_run_list_flip ; self.elder_run_number_level_4=elder_run_number_level_4
        if self.level_4 and self.distance<=400 and self.distance>100:
            BossGeneralFunctions.move(self,self.final_boss_rect,self.elder_run_list_flip,self.elder_run_list,self.elder_run_number_level_4,65,35,9,0.25,
                                      self.final_boss_x_movement,self.final_boss_y_movement,2,2,self.elder_attack_number_level_4,self.final_boss_health,self.player_health)

    def attack_logic(self):
        self.elder_attacks_1_list=elder_attacks_1_list ; self.elder_attacks_1_list_flip=elder_attacks_1_list_flip ; self.elder_attacks_1_number_level_4=elder_attacks_1_number_level_4
        self.elder_attacks_2_list=elder_attacks_2_list ; self.elder_attacks_2_list_flip=elder_attacks_2_list_flip ; self.elder_attacks_2_number_level_4=elder_attacks_2_number_level_4

        if self.elder_attack_list_type[0]==0:
            self.elder_attack_list=self.elder_attacks_1_list ; self.elder_attack_list_flip=self.elder_attacks_1_list_flip ; self.elder_attack_number=self.elder_attacks_1_number_level_4
            self.elder_max_attack_list[0]=8 ; self.damage=0

        if self.elder_attack_list_type[0]==1:
            self.elder_attack_list=self.elder_attacks_2_list ; self.elder_attack_list_flip=self.elder_attacks_2_list_flip ; self.elder_attack_number=self.elder_attacks_2_number_level_4
            self.elder_max_attack_list[0]=8 ; self.damage=0

        print(self.elder_attack_list_type[0])

        print(self.elder_attack_number[0],self.elder_max_attack_list[0])

        if self.elder_attack_number[0]>=self.elder_max_attack_list[0]-0.5: 
            print("HERE")
            self.elder_attack_list_type[0]=random.randint(0,1)


        
    def attack(self):
        self.distance=FinalBoss.distance(self)
        if self.level_4 and self.distance<=100:
            BossGeneralFunctions.attack(self,self.final_boss_rect,self.elder_attack_list_flip,self.elder_attack_list,self.elder_attack_number,65,35,self.elder_max_attack_list[0],
                                        0.40,self.final_boss_x_movement,self.final_boss_y_movement,self.elder_boss_fall_type,self.final_boss_health,self.player_health,self.damage)

    def poison_effect(self):
        pass

    def call_support(self):
        pass

    def health(self):
        pass

    def fall(self):
        pass

    def collision_with_object(self):
        pass


    def collision_with_object_logic(self):
        pass

