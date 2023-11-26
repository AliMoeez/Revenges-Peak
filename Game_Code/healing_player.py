import pygame

from Game_Asset_Code import *

class HealingPlayer:
    def __init__(self,level_1,level_2) -> None:
        self.level_1=level_1
        self.level_2=level_2
        self.player_health=player_health
        self.player_rect=player_rect
        self.camera_x_y=camera_x_y
        self.health_potion_image=health_potion_image
        self.level_2_health_potion_rect=level_2_health_potion_rect

    def distance(self):
        pass

    def blit(self):
        if any([self.level_2,self.level_2]):
            for idx,health in enumerate(self.level_2_health_potion_rect):
                SCREEN.blit(self.health_potion_image,(self.level_2_health_potion_rect[idx].x-self.camera_x_y[0],self.level_2_health_potion_rect[idx].y-self.camera_x_y[1]))

    def interaction(self):
        pass

    def healing_condition(self):
        pass

