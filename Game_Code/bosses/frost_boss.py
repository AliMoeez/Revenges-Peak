import pygame

from Game_Asset_Code import *
from .boss_general_fucntions import BossGeneralFunctions

class FrostBoss:
    def __init__(self,level_2) -> None:
        self.level_2=level_2
        self.frost_boss_rect=frost_boss_rect
        self.player_rect=player_rect
        self.camera_x_y=camera_x_y

    def idle(self):
        self.frost_boss_idle=frost_boss_idle ; self.frost_boss_idle_flip=frost_boss_idle_flip ; self.frost_boss_idle_number=frost_boss_idle_number
        if self.level_2:
            BossGeneralFunctions.idle(self,self.frost_boss_rect,self.frost_boss_idle,self.frost_boss_idle_flip,self.frost_boss_idle_number,0,0,7,0.25)

    def move(self):
        pass

    def attack(self):
        pass

    def slow_down(self):
        pass

    def player_hit(self):
        pass

    def health(self):
        pass

    def collision_with_object():
        pass

    def collision_with_object_logic(self):
        pass


