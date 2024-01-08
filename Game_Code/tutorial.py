import pygame

from Game_Asset_Code import *
from .dialogue import Dialouge
from .player import Player
from .enemies import EnemyOne

class Tutorial:
    def __init__(self,level_1,tutorial_one,tutorial_two):
        Dialouge.__init__(self,level_1,dialogue_condition,dialogue_story_condition,level_1_wizard_talk,level_2,level_2_guard_talk,level_2_boss_talk,level_2_player_talk,level_2_enemy_talk,
                          level_3,level_3_player_talk_1,level_3_player_talk_2,level_3_player_talk_3,level_3_player_talk_4,level_3_player_lose,level_3_player_win,level_4,level_4_player_talk_1,level_4_player_talk_2,level_4_player_lose,level_4_player_win)
        EnemyOne.__init__(self,level_1,enemy_1_level_1_rect,reset_locations,player_control,level_2,level_3,level_4,level_4_player_talk_2)
        self.tutorial_one=tutorial_one ; self.tutorial_two=tutorial_two 
        self.level_1=level_1 ; self.player_rect=self.player_rect ; self.font=r"Assets\Misc\Fonts\Pixellari.ttf"  ; self.WHITE=(255,55,55) 
        self.text_position=text_position ; self.player_x_movement=player_x_movement ; self.player_y_movement=player_y_movement ; self.tutorial_two_list=tutorial_two_list
        self.left_mouse_button_icon=left_mouse_button_icon ; self.investigate_object_level_one=investigate_object_level_one ; self.talk_to_abyss_level_one=talk_to_abyss_level_one
        self.player_attack_cooldown=player_attack_cooldown

    def begin_tutorial(self,event,event_list):
        if any([self.level_1]) and not self.tutorial_one:
             self.enemy_one_distance_list=EnemyOne.distance(self)
             for idx,distance in enumerate(self.enemy_one_distance_list):
                 if distance<500 and self.tutorial_two_list[0]>=1:
                     self.tutorial_two_list[0]-=1
                     return True

    def backround(self):
        self.screen_fade=pygame.Surface((SCREEN_WIDTH,SCREEN_HEIGHT))  ; self.screen_fade.set_alpha(50) ; self.screen_fade.fill((0,0,0)) ; SCREEN.blit(self.screen_fade,(0,0))
        self.text_bgackround_fade=pygame.Surface((SCREEN_WIDTH,SCREEN_HEIGHT-250))  ; self.text_bgackround_fade.set_alpha(50) ; self.text_bgackround_fade.fill((100,100,100)) ; SCREEN.blit(self.text_bgackround_fade,(0,550))

        self.font_title=pygame.font.Font(self.font,25) 
        self.font_title_render=self.font_title.render("To Continue",True,self.WHITE) 
        SCREEN.blit(self.font_title_render,(SCREEN_WIDTH//2+450,SCREEN_HEIGHT-45))


        SCREEN.blit(self.left_mouse_button_icon,(SCREEN_WIDTH//2+400,SCREEN_HEIGHT-55))


    def escape_button(self):
        pass

    def text(self):
        if self.tutorial_one:
            self.tutorial_text="Welcome To Revenge's Peak. To Move use the W,A,S,D keys. The objective arrow is at the top and helps you get to the next objective for each level."
        if self.tutorial_two and not self.tutorial_one:
            self.tutorial_text="Quick, enemies are nearby. Use the E key to attack and the F key to control one of your enemies for a short period of time."

    def text_movement(self):
        self.message_speed=2
        Tutorial.text(self)
        if self.text_position[0]<self.message_speed*len(self.tutorial_text):
            self.text_position[0]+=0.55
                
    def line_movment(self):
        Tutorial.text_movement(self)
        if self.tutorial_one or (self.tutorial_two and not self.tutorial_one):
            self.font_title=pygame.font.Font(self.font,30)
            return Dialouge.line_function(self,SCREEN,self.tutorial_text[0:int(self.text_position[0])//self.message_speed],(SCREEN_WIDTH//2-550,600),self.font_title,self.WHITE)
        
    def player_idle_show(self):
        if self.level_1 and self.tutorial_one or (self.tutorial_two and not self.tutorial_one):
            Player.idle(self,pygame.key.get_pressed())
            self.player_x_movement[0]=0 
            self.player_y_movement[0]=0

    def show(self):
        if self.level_1 and self.tutorial_one or (self.tutorial_two and not self.tutorial_one):
            Tutorial.backround(self)
            Tutorial.line_movment(self)

    def skip(self,event,event_list):
        if self.level_1 and self.tutorial_one or (self.tutorial_two and not self.tutorial_one):
            if event.type==pygame.MOUSEBUTTONDOWN:
                return True
