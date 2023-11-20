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

    def distance(self):
        self.distance_list=[]
        self.player_boss_distance=math.hypot(self.player_rect.x-self.frost_boss_rect.x,self.player_rect.y-self.frost_boss_rect.y)
        self.distance_list.append(self.player_boss_distance)
        return self.distance_list
        
    def idle(self):
        self.frost_boss_idle=frost_boss_idle ; self.frost_boss_idle_flip=frost_boss_idle_flip ; self.frost_boss_idle_number=frost_boss_idle_number
        if self.level_2 and self.level_2_boss_talk:
            BossGeneralFunctions.idle(self,self.frost_boss_rect,self.frost_boss_idle,self.frost_boss_idle_flip,self.frost_boss_idle_number,0,0,7,0.25)

    def move(self):
        self.frost_boss_run=frost_boss_run ; self.frost_boss_run_flip=frost_boss_run_flip ; self.frost_boss_run_number=frost_boss_run_number
        if self.level_2 and not self.level_2_boss_talk:
            BossGeneralFunctions.move(self,self.frost_boss_rect,self.frost_boss_run,self.frost_boss_run_flip,
                                      self.frost_boss_run_number,0,0,11,0.25,self.frost_boss_x_movement,self.frost_boss_y_movement,2,2)
              
    def attack(self):
        pass

    def slow_down(self):
        pass

    def player_hit(self):
        pass

    def health(self):
        pass

    def collision_with_object(self):
        if self.level_2:
            self.collision_function=BossGeneralFunctions.collision_with_object(self,self.level_2_tile_set_rect,self.frost_boss_rect)
            return self.collision_function

    def collision_with_object_logic(self):
        if self.level_2:
            self.collision=FrostBoss.collision_with_object(self)
            BossGeneralFunctions.collision_with_object_logic(self,self.frost_boss_rect,self.frost_boss_x_movement,self.collision,self.frost_boss_y_movement)


