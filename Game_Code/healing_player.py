import pygame
import math

from Game_Asset_Code import *

class HealingPlayer:
    def __init__(self,level_1,level_2,reset_locations,level_3) -> None:
        self.level_1=level_1
        self.level_2=level_2
        self.level_3=level_3
        self.player_health=player_health
        self.player_rect=player_rect
        self.camera_x_y=camera_x_y
        self.health_potion_image=health_potion_image
        self.level_2_health_potion_rect=level_2_health_potion_rect
        self.left_mouse_button_icon=left_mouse_button_icon_miniture
        self.font=r"Assets\Misc\Fonts\Pixellari.ttf"
        self.red=(178,34,34) 
        self.reset_locations=reset_locations
        self.level_3_health_potion_rect=level_3_health_potion_rect
        self.level_3_health_potion_x=level_3_health_potion_x
        self.level_3_health_potion_y=level_3_health_potion_y

        if self.level_1:
            self.level_health_potion_rect=[] ; self.level_health_potion_x=[] ; self.level_health_potion_y=[]
        if self.level_2:
            self.level_health_potion_rect=self.level_2_health_potion_rect ; self.level_health_potion_x=level_2_health_potion_x ;  self.level_health_potion_y=level_2_health_potion_y
        if self.level_3:
            self.level_health_potion_rect=self.level_3_health_potion_rect ; self.level_health_potion_x=level_3_health_potion_x ;  self.level_health_potion_y=level_3_health_potion_y           
            
    def distance(self):
        if any({self.level_1,self.level_2,self.level_3}):
            self.distance_player_health=[]
            for idx,health in enumerate(self.level_health_potion_rect):
                self.distance=math.hypot(self.player_rect.x-self.level_health_potion_rect[idx].x,self.player_rect.y-self.level_health_potion_rect[idx].y)
                self.distance_player_health.append(self.distance)
            return self.distance_player_health    
            
    def blit(self):
        if any([self.level_2,self.level_2,self.level_3]):
            for idx,health in enumerate(self.level_health_potion_rect):
                SCREEN.blit(self.health_potion_image,(self.level_health_potion_rect[idx].x-self.camera_x_y[0],self.level_health_potion_rect[idx].y-self.camera_x_y[1]))

    def text(self):
        self.font_health=pygame.font.Font(self.font,20)
        self.font_health_render=self.font_health.render("To Use",True,self.red)
        return self.font_health_render

    def interaction(self):
        if any([self.level_1,self.level_2,self.level_3]):
            self.distance_player_health=HealingPlayer.distance(self)
            self.health_text=HealingPlayer.text(self)
            for idx,distance in enumerate(self.distance_player_health):
                if distance<100:
                    SCREEN.blit(self.left_mouse_button_icon,(self.level_health_potion_rect[idx].x-self.camera_x_y[0]-25,self.level_health_potion_rect[idx].y-self.camera_x_y[1]-30))
                    SCREEN.blit(self.health_text,(self.level_health_potion_rect[idx].x-self.camera_x_y[0],self.level_health_potion_rect[idx].y-self.camera_x_y[1]-25))

    def healing_condition(self,event):
        if any([self.level_1,self.level_2,self.level_3]):
            self.distance_player_health=HealingPlayer.distance(self)
            for idx,distance in enumerate(self.distance_player_health):
                if distance<100 and event.type==pygame.MOUSEBUTTONDOWN:
                    self.level_health_potion_rect[idx].x=100000
                    return True
        
    def reset_position(self):
        if any([self.level_1,self.level_2,self.level_3]) and self.reset_locations:
             for idx,health in enumerate(self.level_health_potion_rect):
                self.level_health_potion_rect[idx].x=self.level_health_potion_x[idx]
                self.level_health_potion_rect[idx].y=self.level_health_potion_y[idx]
             return True