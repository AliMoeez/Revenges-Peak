import pygame
import math

from Game_Asset_Code import *
from .boss_general_fucntions import BossGeneralFunctions

class FrostBoss:
    def __init__(self,level_2,level_2_boss_talk,reset_locations) -> None:
        self.level_2=level_2 ; self.frost_boss_rect=frost_boss_rect ; self.player_rect=player_rect ; self.camera_x_y=camera_x_y
        self.level_2_boss_talk=level_2_boss_talk ; self.level_2_tile_set_rect=level_2_tile_set_rect ; self.frost_boss_x_movement=frost_boss_x_movement ; self.frost_boss_y_movement=frost_boss_y_movement
        self.frost_boss_attack_number=frost_boss_attack_number ; self.frost_boss_health_icon=frost_boss_health_icon ; self.frost_boss_health=frost_boss_health ;self.frost_boss_fall_type=frost_boss_fall_type
        self.player_attack_number=player_attack_number ; self.player_health=player_health ; self.frost_boss_fast_mode_timer=frost_boss_fast_mode_timer ; self.frost_boss_x_increment=frost_boss_x_increment
        self.frost_boss_y_increment=frost_boss_y_increment ; self.frost_boss_damage=frost_boss_damage ; self.frost_boss_slow_down_timer=frost_boss_slow_down_timer ; self.frost_boss_fast_mode_icon=frost_boss_fast_mode_icon
        self.frost_boss_fast_mode_timer_max=frost_boss_fast_mode_timer_max ; self.reset_locations=reset_locations ; self.frost_boss_x=frost_boss_x ; self.frost_boss_y=frost_boss_y

    def distance(self):
        self.distance_list=[]
        self.player_boss_distance=math.hypot(self.player_rect.x-self.frost_boss_rect.x,self.player_rect.y-self.frost_boss_rect.y)
        self.distance_list.append(self.player_boss_distance)
        return self.distance_list
        
    def idle(self):
        self.frost_boss_idle=frost_boss_idle ; self.frost_boss_idle_flip=frost_boss_idle_flip ; self.frost_boss_idle_number=frost_boss_idle_number
        if self.level_2 and self.level_2_boss_talk:
            BossGeneralFunctions.idle(self,self.frost_boss_rect,self.frost_boss_idle,
                                      self.frost_boss_idle_flip,self.frost_boss_idle_number,70,30,7,0.25,self.frost_boss_health,self.player_health)
            pygame.draw.rect(SCREEN,(100,100,100),pygame.Rect(self.frost_boss_rect.x-self.camera_x_y[0],self.frost_boss_rect.y-self.camera_x_y[1],128.5,128.5),width=1)

    def move(self):
        self.frost_boss_run=frost_boss_run ; self.frost_boss_run_flip=frost_boss_run_flip ; self.frost_boss_run_number=frost_boss_run_number
        self.distance_player_boss=FrostBoss.distance(self)
        if self.level_2 and not self.level_2_boss_talk:
            for distance in self.distance_player_boss:
                if distance>100:
                    BossGeneralFunctions.move(self,self.frost_boss_rect,self.frost_boss_run,self.frost_boss_run_flip,
                                            self.frost_boss_run_number,70,30,11,0.25,self.frost_boss_x_movement,
                                            self.frost_boss_y_movement,self.frost_boss_x_increment[0],self.frost_boss_y_increment[0],self.frost_boss_attack_number,self.frost_boss_health,self.player_health)
                    pygame.draw.rect(SCREEN,(200,200,200),pygame.Rect(self.frost_boss_rect.x-self.camera_x_y[0],self.frost_boss_rect.y-self.camera_x_y[1],128.5,128.5),width=1)
              
    def attack(self):
        self.frost_boss_attack=frost_boss_attack ; self.frost_boss_attack_flip=frost_boss_attack_flip
        self.distance_player_boss=FrostBoss.distance(self)
        if self.level_2 and not self.level_2_boss_talk:
            for distance in self.distance_player_boss:
                if distance<=100:
                    BossGeneralFunctions.attack(self,self.frost_boss_rect,self.frost_boss_attack,self.frost_boss_attack_flip,
                                                self.frost_boss_attack_number,70,30,15,0.25,self.frost_boss_x_movement,
                                                self.frost_boss_y_movement,self.frost_boss_fall_type,self.frost_boss_health,self.player_health,self.frost_boss_damage[0])
                    pygame.draw.rect(SCREEN,(100,100,100),pygame.Rect(self.frost_boss_rect.x-self.camera_x_y[0],self.frost_boss_rect.y-self.camera_x_y[1],128.5,128.5),width=1)

    def fast_mode(self):
        if self.level_2 and not self.level_2_boss_talk:
        
            if self.frost_boss_fast_mode_timer[0]<=150:
                self.frost_boss_fast_mode_timer[0]+=1 ; self.frost_boss_x_increment[0]=2 ; self.frost_boss_y_increment[0]=2 ; self.frost_boss_damage[0]=100 #100
            
            if self.frost_boss_fast_mode_timer[0]>150:
                
                self.frost_boss_fast_mode_timer[0]=151
                self.frost_boss_fast_mode_timer_max[0]+=1 
                self.frost_boss_x_increment[0]=10 ; self.frost_boss_y_increment[0]=10 ; self.frost_boss_damage[0]=200 #200
                
                if self.frost_boss_fast_mode_timer_max[0]>100:
                    self.frost_boss_fast_mode_timer[0]=0
                    self.frost_boss_fast_mode_timer_max[0]=0

    def slow_down(self):
        if self.level_2 and not self.level_2_boss_talk:
            if self.frost_boss_slow_down_timer[0]<300:
                self.frost_boss_slow_down_timer[0]+=1
            elif self.frost_boss_slow_down_timer[0]>=300 and self.frost_boss_slow_down_timer[0]<700:
                self.frost_boss_slow_down_timer[0]+=1 ; self.frost_boss_x_increment[0]=self.frost_boss_x_increment[0]//1.25 ; self.frost_boss_y_increment[0]=self.frost_boss_y_increment[0]//1.25 ; self.frost_boss_damage[0]=self.frost_boss_damage[0]//1.10
            
            elif self.frost_boss_slow_down_timer[0]>=700 and self.frost_boss_slow_down_timer[0]<900:
                self.frost_boss_slow_down_timer[0]+=1 ; self.frost_boss_x_increment[0]=self.frost_boss_x_increment[0]//1.50 ; self.frost_boss_y_increment[0]=self.frost_boss_y_increment[0]//1.50 ; self.frost_boss_damage[0]=self.frost_boss_damage[0]//1.25
            
            elif self.frost_boss_slow_down_timer[0]>=900:
                self.frost_boss_slow_down_timer[0]=900 ; self.frost_boss_x_increment[0]=self.frost_boss_x_increment[0]//2 ; self.frost_boss_y_increment[0]=self.frost_boss_y_increment[0]//2 ; self.frost_boss_damage[0]=self.frost_boss_damage[0]//1.50

    def player_hit(self):
        self.distance_player_boss=FrostBoss.distance(self)
        if self.level_2 and not self.level_2_boss_talk:
            for distance in self.distance_player_boss:
                if distance<=100: #boss health decreasw was 10 before
                    BossGeneralFunctions.player_hit(self,self.frost_boss_health,self.player_attack_number,1000,pygame.key.get_pressed())

    def fall(self):
        self.frost_boss_fall=frost_boss_fall ; self.frost_boss_fall_flip=frost_boss_fall_flip ; self.frost_boss_fall_number=frost_boss_fall_number
        if self. level_2 and not self.level_2_boss_talk:
            BossGeneralFunctions.fall(self,self.frost_boss_rect,self.frost_boss_fall,self.frost_boss_fall_flip,self.frost_boss_fall_number,0.25,30,self.frost_boss_x_movement,
                                      self.frost_boss_y_movement,70,30,self.frost_boss_health,self.frost_boss_fall_type)
            
    def reset_position(self):
        if self.level_2 and self.reset_locations:
            print("BOSS RESET")
            BossGeneralFunctions.reset_position(self,self.frost_boss_rect,self.frost_boss_x,self.frost_boss_y,self.frost_boss_health,1000)
            return True

    def health(self):
        if self.level_2 and not self.level_2_boss_talk:
            BossGeneralFunctions.health(self,self.frost_boss_health,1000,500,2,self.frost_boss_health_icon,(173,216,230),670,10,682,14,1)
            BossGeneralFunctions.health(self,self.frost_boss_fast_mode_timer,1000,500,2,self.frost_boss_fast_mode_icon,(153,113,130),670,40,682,44,1000/151)
        
    def collision_with_object(self):
        if self.level_2:
            self.collision_function=BossGeneralFunctions.collision_with_object(self,self.level_2_tile_set_rect,self.frost_boss_rect)
            return self.collision_function

    def collision_with_object_logic(self):
        if self.level_2:
            self.collision=FrostBoss.collision_with_object(self)
            BossGeneralFunctions.collision_with_object_logic(self,self.frost_boss_rect,self.frost_boss_x_movement,self.collision,self.frost_boss_y_movement)


