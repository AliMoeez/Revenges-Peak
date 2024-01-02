import pygame
import math

from Game_Asset_Code import *
from .people import People
from .dialogue import Dialouge

class Objectives:
    def __init__(self,level_1,level_1_wizard_talk,talk_to_abyss_level_one,investigate_object_level_one,
                 dialogue_objective_list,level_2_guard_talk,level_2_boss_talk,level_2,level_2_player_talk,level_2_enemy_talk,
                 level_3_player_talk_1,level_3_player_talk_2,level_3_player_talk_3,level_3_player_talk_4,level_3,
                 level_4,level_4_player_talk_1,level_4_player_talk_2,level_4_player_lose,level_4_player_win):
        People.__init__(self,level_1,level_1_wizard_talk,reset_locations,level_2)
        Dialouge.__init__(self,level_1,dialogue_condition,dialogue_story_condition,level_1_wizard_talk,level_2,level_2_guard_talk,level_2_boss_talk,level_2_player_talk,level_2_enemy_talk,
                          level_3,level_3_player_talk_1,level_3_player_talk_2,level_3_player_talk_3,level_3_player_talk_4,level_3_player_lose,level_3_player_win,level_4,level_4_player_talk_1,level_4_player_talk_2,level_4_player_lose,level_4_player_win)
        self.level_1=level_1 ; self.font=r"Assets\Misc\Fonts\Pixellari.ttf"  ; self.RED=(255,55,55) ; self.level_1_wizard_talk=level_1_wizard_talk
        self.player_rect=player_rect ; self.people_level_1_rect=people_level_1_rect ; self.camera_x_y=camera_x_y ; self.red_arrow_icon=red_arrow_icon
        self.WHITE=(255,255,255) ; self.talk_to_abyss_level_one=talk_to_abyss_level_one ; self.investigate_object_level_one=investigate_object_level_one
        self.dialogue_objective_list=dialogue_objective_list
        self.level_2=level_2; self.level_2_guard_talk=level_2_guard_talk ; self.level_2_boss_talk=level_2_boss_talk
        self.people_level_2_rect=people_level_2_rect
        self.level_2_enemy_talk=level_2_enemy_talk
        self.enemy_2_level_2_rects=enemy_2_level_2_rects
        self.enemy_1_health=enemy_1_health
        self.enemy_2_health=enemy_2_health
        self.frost_boss_rect=frost_boss_rect
        self.level_3_player_talk_1=level_3_player_talk_1
        self.level_3=level_3
        self.level_3_player_talk_2=level_3_player_talk_2
        self.level_3_player_talk_3=level_3_player_talk_3
        self.enemy_3_level_3_rect=enemy_3_level_3_rect
        self.level_3_player_talk_4=level_3_player_talk_4
        self.enemy_3_health=enemy_3_health
        self.object_rect=object_rect
        
        self.level_4=level_4
        self.level_4_player_talk_1=level_4_player_talk_1
        self.level_4_player_talk_2=level_4_player_talk_2
        self.level_4_player_lose=level_4_player_lose
        self.level_4_player_win=level_4_player_win

    def distance(self,place_x:int,place_y:int):
        if any([self.level_1,self.level_2,self.level_3,self.level_4]):
            self.player_objective_distance_list=[]
            self.player_objective_distance=math.hypot(self.player_rect.x-place_x,self.player_rect.y-place_y)
            self.player_objective_distance_list.append(self.player_objective_distance)
            return self.player_objective_distance_list
    
    def level_one_objectives(self):
        #first meet with the wizard #then meet with the abyss #then defeat all enemies and then proceed to top-left corner
        if any([self.level_1]):
            
            if self.level_1_wizard_talk:
                self.objectives_distance=Objectives.distance(self,self.people_level_1_rect[0].x,self.people_level_1_rect[0].y)
                if self.objectives_distance[0]<200:
                    self.dialogue_objective_list[0]=1
                return self.objectives_distance[0],self.people_level_1_rect[0].x,self.people_level_1_rect[0].y
            
            if self.talk_to_abyss_level_one and not self.level_1_wizard_talk:
                self.objectives_distance=Objectives.distance(self,384,384)
                if self.objectives_distance[0]<200:
                    self.dialogue_objective_list[0]=2
                return self.objectives_distance[0],384,384
            
            if self.investigate_object_level_one and not self.talk_to_abyss_level_one:
                self.objectives_distance=Objectives.distance(self,4224,1952)
                if self.objectives_distance[0]<200:
                    self.dialogue_objective_list[0]=3
                return self.objectives_distance[0],4224,1952
        
            if not self.investigate_object_level_one:
                self.objectives_distance=Objectives.distance(self,4512,160)
                return self.objectives_distance[0],4512,160
            
    def level_two_objectives(self):
        if self.level_2:
            if self.level_2_guard_talk:
                self.objectives_distance=Objectives.distance(self,self.people_level_2_rect[0].x,self.people_level_2_rect[0].y)
                if self.objectives_distance[0]<200:
                    self.dialogue_objective_list[0]=1
                return self.objectives_distance[0],self.people_level_2_rect[0].x,self.people_level_2_rect[0].y
            if self.level_2_enemy_talk and not self.level_2_guard_talk:
                self.objectives_distance=Objectives.distance(self,self.enemy_2_level_2_rects[0].x,self.enemy_2_level_2_rects[0].y)
                if self.objectives_distance[0]<200:
                    self.dialogue_objective_list[0]=2
                return self.objectives_distance[0],self.enemy_2_level_2_rects[0].x,self.enemy_2_level_2_rects[0].y
            if self.level_2_boss_talk and not self.level_2_enemy_talk and all(self.enemy_1_health)<=0 and all(self.enemy_2_health)<=0:
                self.objectives_distance=Objectives.distance(self,self.frost_boss_rect.x,self.frost_boss_rect.y)
                if self.objectives_distance[0]<200:
                    self.dialogue_objective_list[0]=3
                return self.objectives_distance[0],self.frost_boss_rect.x,self.frost_boss_rect.y
            
    
    def level_three_objectives(self):
        if self.level_3:
           if not self.level_3_player_talk_1 and self.level_3_player_talk_2:
                self.objectives_distance=Objectives.distance(self,self.enemy_3_level_3_rect[0].x,self.enemy_3_level_3_rect[0].y)
                if all(i<=0 for i in self.enemy_1_health) and all(i<=0 for i in self.enemy_2_health) and all(i<=0 for i in self.enemy_3_health):
                    self.dialogue_objective_list[0]=1
                return self.objectives_distance[0],self.enemy_3_level_3_rect[0].x,self.enemy_3_level_3_rect[0].y
           if self.level_3_player_talk_3 and not self.level_3_player_talk_2:
                self.objectives_distance=Objectives.distance(self,3904,417)
                if self.objectives_distance[0]<200:
                    self.dialogue_objective_list[0]=2
                return self.objectives_distance[0],3904,417
           if self.level_3_player_talk_4 and not self.level_3_player_talk_3:
                self.objectives_distance=Objectives.distance(self,288,225)
                if self.objectives_distance[0]<200:
                    self.dialogue_objective_list[0]=3
                return self.objectives_distance[0],288,225
           
    def level_four_objectives(self):
        if self.level_4:
            if self.level_4_player_talk_1:
                self.objectives_distance=Objectives.distance(self,690,1520)
                if self.objectives_distance[0]<200:
                    self.dialogue_objective_list[0]=1
                return self.objectives_distance[0],690,1520

    def define_level(self):
        if self.level_1: self.level_objectives=Objectives.level_one_objectives(self)
        if self.level_2: self.level_objectives=Objectives.level_two_objectives(self)
        if self.level_3: self.level_objectives=Objectives.level_three_objectives(self)
        if self.level_4: self.level_objectives=Objectives.level_four_objectives(self)

    def rotation_angle(self):
        if any([self.level_1,self.level_2,self.level_3,self.level_4]):
            if self.level_objectives is not None:
                self.interact_x,self.interact_y=self.level_objectives[1],self.level_objectives[2]
                self.dx,self.dy=self.interact_x-self.player_rect.x, self.interact_y-self.player_rect.y            
                self.angle=math.degrees(math.atan2(-self.dy,self.dx))-90
                return self.angle
        
    def background(self):
        self.objectives_backgruond=pygame.Surface((115,100))  ; self.objectives_backgruond.set_alpha(85)  ; self.objectives_backgruond.fill(self.WHITE) 
        self.objectives_backgruond=SCREEN.blit(self.objectives_backgruond,(SCREEN_WIDTH//2-30,SCREEN_HEIGHT-790))

    def show_objectives(self):
        if any([self.level_1,self.level_2,self.level_3,self.level_4]):
            if self.level_objectives is not None:
                Objectives.background(self)
                self.font_title=pygame.font.Font(self.font,24) 
                self.font_title_render=self.font_title.render(f"{round(self.level_objectives[0],1)}m",True,self.RED) 
                self.arrow_icon=pygame.transform.rotate(self.red_arrow_icon,Objectives.rotation_angle(self))
                self.objective_icon=self.font_title.render(f"Objectives",True,self.RED)
                SCREEN.blit(self.objective_icon,(SCREEN_WIDTH//2-30,SCREEN_HEIGHT-790)) ; SCREEN.blit(self.arrow_icon,(SCREEN_WIDTH//2-5,SCREEN_HEIGHT-770)) ; SCREEN.blit(self.font_title_render,(SCREEN_WIDTH//2-15,SCREEN_HEIGHT-715))  
