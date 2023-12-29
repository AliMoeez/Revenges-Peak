import pygame


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


    def idle(self):
        self.elder_idle_list=elder_idle_list ; self.elder_idle_list_flip=elder_idle_list_flip ; self.elder_idle_number_level_4=elder_idle_number_level_4
        if self.level_4:
            BossGeneralFunctions.idle(self,self.final_boss_rect,self.elder_idle_list_flip,self.elder_idle_list,self.elder_idle_number_level_4,0,0,7,0.25,
                                      self.final_boss_health,self.player_health)

