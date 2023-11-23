import pygame
import math

from Game_Asset_Code import *
from .boss_general_fucntions import BossGeneralFunctions

class FrostBoss:
    def __init__(self,level_2,level_2_boss_talk) -> None:
        self.level_2=level_2
        self.frost_boss_rect=frost_boss_rect
        self.player_rect=player_rect
        self.camera_x_y=camera_x_y
        self.level_2_boss_talk=level_2_boss_talk
        self.level_2_tile_set_rect=level_2_tile_set_rect
        self.frost_boss_x_movement=frost_boss_x_movement
        self.frost_boss_y_movement=frost_boss_y_movement
        self.frost_boss_attack_number=frost_boss_attack_number
        self.frost_boss_health_icon=frost_boss_health_icon
        self.frost_boss_health=frost_boss_health
        self.frost_boss_fall_type=frost_boss_fall_type
        self.player_attack_number=player_attack_number
        self.player_health=player_health

    def distance(self):
        self.distance_list=[]
        self.player_boss_distance=math.hypot(self.player_rect.x-self.frost_boss_rect.x,self.player_rect.y-self.frost_boss_rect.y)
        self.distance_list.append(self.player_boss_distance)
        return self.distance_list
        
    def idle(self):
        self.frost_boss_idle=frost_boss_idle ; self.frost_boss_idle_flip=frost_boss_idle_flip ; self.frost_boss_idle_number=frost_boss_idle_number
        if self.level_2 and self.level_2_boss_talk:
            BossGeneralFunctions.idle(self,self.frost_boss_rect,self.frost_boss_idle,
                                      self.frost_boss_idle_flip,self.frost_boss_idle_number,70,30,7,0.25,self.frost_boss_health)
            pygame.draw.rect(SCREEN,(100,100,100),pygame.Rect(self.frost_boss_rect.x-self.camera_x_y[0],self.frost_boss_rect.y-self.camera_x_y[1],128.5,128.5),width=1)

    def move(self):
        self.frost_boss_run=frost_boss_run ; self.frost_boss_run_flip=frost_boss_run_flip ; self.frost_boss_run_number=frost_boss_run_number
        self.distance_player_boss=FrostBoss.distance(self)
        if self.level_2 and not self.level_2_boss_talk:
            for distance in self.distance_player_boss:
                if distance>100:
                    BossGeneralFunctions.move(self,self.frost_boss_rect,self.frost_boss_run,self.frost_boss_run_flip,
                                            self.frost_boss_run_number,70,30,11,0.25,self.frost_boss_x_movement,
                                            self.frost_boss_y_movement,2,2,self.frost_boss_attack_number,self.frost_boss_health)
                    pygame.draw.rect(SCREEN,(200,200,200),pygame.Rect(self.frost_boss_rect.x-self.camera_x_y[0],self.frost_boss_rect.y-self.camera_x_y[1],128.5,128.5),width=1)
              
    def attack(self):
        self.frost_boss_attack=frost_boss_attack ; self.frost_boss_attack_flip=frost_boss_attack_flip
        self.distance_player_boss=FrostBoss.distance(self)
        if self.level_2 and not self.level_2_boss_talk:
            for distance in self.distance_player_boss:
                if distance<=100:
                    BossGeneralFunctions.attack(self,self.frost_boss_rect,self.frost_boss_attack,self.frost_boss_attack_flip,
                                                self.frost_boss_attack_number,70,30,15,0.25,self.frost_boss_x_movement,
                                                self.frost_boss_y_movement,self.frost_boss_fall_type,self.frost_boss_health,self.player_health,100)
                    pygame.draw.rect(SCREEN,(100,100,100),pygame.Rect(self.frost_boss_rect.x-self.camera_x_y[0],self.frost_boss_rect.y-self.camera_x_y[1],128.5,128.5),width=1)

    def fast_mode(self):
        pass

    def slow_down(self):
        pass

    def player_hit(self):
        self.distance_player_boss=FrostBoss.distance(self)
        if self.level_2 and not self.level_2_boss_talk:
            for distance in self.distance_player_boss:
                if distance<=100:
                    BossGeneralFunctions.player_hit(self,self.frost_boss_health,self.player_attack_number,10,pygame.key.get_pressed())

    def fall(self):
        self.frost_boss_fall=frost_boss_fall ; self.frost_boss_fall_flip=frost_boss_fall_flip ; self.frost_boss_fall_number=frost_boss_fall_number
        if self. level_2 and not self.level_2_boss_talk:
            BossGeneralFunctions.fall(self,self.frost_boss_rect,self.frost_boss_fall,self.frost_boss_fall_flip,self.frost_boss_fall_number,0.25,30,self.frost_boss_x_movement,
                                      self.frost_boss_y_movement,70,30,self.frost_boss_health,self.frost_boss_fall_type)

    def health(self):
        if self.level_2 and not self.level_2_boss_talk:
            BossGeneralFunctions.health(self,self.frost_boss_health,1000,500,2,self.frost_boss_health_icon)
        
    def collision_with_object(self):
        if self.level_2:
            self.collision_function=BossGeneralFunctions.collision_with_object(self,self.level_2_tile_set_rect,self.frost_boss_rect)
            return self.collision_function

    def collision_with_object_logic(self):
        if self.level_2:
            self.collision=FrostBoss.collision_with_object(self)
            BossGeneralFunctions.collision_with_object_logic(self,self.frost_boss_rect,self.frost_boss_x_movement,self.collision,self.frost_boss_y_movement)


