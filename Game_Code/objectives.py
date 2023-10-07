import pygame
import math

from Game_Asset_Code import *
from .people import People
from .player import Player

class Objectives:
    def __init__(self,level_1,level_1_wizard_talk):
        People.__init__(self,level_1,level_1_wizard_talk)
        Player.__init__(self,player_x,player_y,player_width,player_height,player_rect,level_1,player_control,dialogue_condition,dialogue_story_condition)
        self.level_1=level_1 ; self.font=r"Assets\Misc\Fonts\Pixellari.ttf"  ; self.RED=(255,55,55) ; self.level_1_wizard_talk=level_1_wizard_talk
        self.player_rect=player_rect ; self.people_level_1_rect=people_level_1_rect ; self.camera_x_y=camera_x_y ; self.red_arrow_icon=red_arrow_icon
        self.red_arrow_icon_flip=red_arrow_icon_flip
    
    
    def distance(self,place_x:int,place_y:int):
        if any([self.level_1]):
            self.player_objective_distance_list=[]
            self.player_objective_distance=math.hypot(self.player_rect.x-place_x,self.player_rect.y-place_y)
            self.player_objective_distance_list.append(self.player_objective_distance)
            return self.player_objective_distance_list
    
    def level_one_objectives(self):
        #first meet with the wizard #then meet with the abyss #then defeat all enemies and then proceed to top-left corner
        if any([self.level_1]):
            if self.level_1_wizard_talk:
                self.objectives_distance=Objectives.distance(self,self.people_level_1_rect[0].x,self.people_level_1_rect[0].y)
                return self.objectives_distance[0]
            
    def rotation_angle(self):
        if any([self.level_1]):
            if Objectives.level_one_objectives(self) is not None:
                self.angle=-math.degrees(math.atan2(self.player_rect.y-self.people_level_1_rect[0].y,self.player_rect.x-self.people_level_1_rect[0].x))
                return self.angle
        
    def show_objectives(self):
        if any([self.level_1]):
            if Objectives.level_one_objectives(self) is not None:
                self.font_title=pygame.font.Font(self.font,24) 
                self.font_title_render=self.font_title.render(f"{round(Objectives.level_one_objectives(self),0)}",True,self.RED) 
                
                if self.player_rect.x<self.people_level_1_rect[0].x:
                    self.arrow_icon=red_arrow_icon
                else:
                    self.arrow_icon=red_arrow_icon_flip
                
                self.arrow_icon=pygame.transform.rotate(self.arrow_icon,Objectives.rotation_angle(self))


                SCREEN.blit(self.arrow_icon,(SCREEN_WIDTH//2-5,SCREEN_HEIGHT-750)) 
                SCREEN.blit(self.font_title_render,(SCREEN_WIDTH//2-25,SCREEN_HEIGHT-725))  


        
        

    

