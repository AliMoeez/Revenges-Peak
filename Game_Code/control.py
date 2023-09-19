import pygame
import math

from Game_Asset_Code import *


class Control:
    def __init__(self,level_1,player_control):
        self.player_rect=player_rect ; self.enemy_1_level_1_rect=enemy_1_level_1_rect ; self.level_1=level_1 
        self.player_control=player_control ; self.player_control_cooldown=player_control_cooldown ; self.enemy_1_level_1_rect=enemy_1_level_1_rect
        if self.level_1:
            self.enemy_rects=self.enemy_1_level_1_rect

    def distance(self):
        if any([self.level_1]):
            self.player_enemy_distance=[]
            for idx,enemy in enumerate(self.enemy_rects):
                self.player_enemy_distance.append(math.hypot(self.player_rect.x-self.enemy_rects[idx].x,self.player_rect.y-self.enemy_rects[idx].y))
            return self.player_enemy_distance

    def mechanic_walk(self,key):
        self.distance_player=Control.distance(self)
        if any([self.level_1]) and self.player_control and self.player_control_cooldown[0]>0:
            for idx,enemy in enumerate(self.enemy_rects):
                if key[pygame.K_d] and not key[pygame.K_a]:
                    self.enemy_rects[idx].x+=2
                if key[pygame.K_a] and not key[pygame.K_d]:
                    self.enemy_rects[idx].x-=2

                
    def print_statement(self):
        self.distance_player=Control.distance(self)
       # print(self.distance_player)
        

               



