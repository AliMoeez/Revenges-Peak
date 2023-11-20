import pygame
import math

from Game_Asset_Code import *
#from .player import Player
from .people import People
from .enemies import EnemyTwo
from .bosses.frost_boss import FrostBoss

class Dialouge:
    def __init__(self,level_1,dialogue_condition,dialogue_story_condition,level_1_wizard_talk,level_2,level_2_guard_talk,level_2_boss_talk,level_2_player_talk,level_2_enemy_talk):
        People.__init__(self,level_1,level_1_wizard_talk,reset_locations,level_2) 
        EnemyTwo.__init__(self,level_1,enemy_2_rects,reset_locations,player_control,level_2)
        FrostBoss.__init__(self,level_2,level_2_boss_talk)
        self.dialogue_condition=dialogue_condition ; self.object_rect=object_rect ; self.camera_x_y=camera_x_y ; self.player_rect=player_rect ; self.level_1=level_1 ; self.mouse_button_blit_list=mouse_button_blit_list
        self.dialogue_click_list=dialogue_click_list ; self.font=r"Assets\Misc\Fonts\Pixellari.ttf"  ; self.WHITE=(255,55,55) ; self.dialouge_list=dialouge_list ; self.dialogue_story_condition=dialogue_story_condition
        self.player_icon=player_icon ; self.abyss_icon=abyss_icon ; self.text_position=text_position ; self.dialogue_offset=dialogue_offset ; self.dialogue_offset_length=dialogue_offset_length
        self.level_1_wizard_talk=level_1_wizard_talk ; self.mouse_button_blit_list=mouse_button_blit_list ; self.elder_icon=elder_icon 
        self.level_2=level_2
        self.guard_icon=guard_icon
        self.level_2_guard_talk=level_2_guard_talk
        self.level_2_boss_talk=level_2_boss_talk
        self.level_2_player_talk=level_2_player_talk
        self.brute_1_icon=brute_1_icon
        self.level_2_enemy_talk=level_2_enemy_talk
        self.frost_boss_icon=frost_boss_icon

    def distance_level_object(self):
        self.tile_interact_rect_distance=[]
        for idx,tile in enumerate(self.object_rect):
            self.tile_interact_rect_distance.append(math.hypot(self.player_rect.x-self.object_rect[idx].x,self.player_rect.y-self.object_rect[idx].y))
        return self.tile_interact_rect_distance

    def level_object_interaction(self):
        Dialouge.distance_level_object(self)
        self.left_mouse_button_icon=left_mouse_button_icon
        if any([self.level_1,self.level_2]):
            self.mouse_button_blit_list.clear()
            for idx,distance in enumerate(self.tile_interact_rect_distance):
                if self.tile_interact_rect_distance[idx]<100: 
                    SCREEN.blit(self.left_mouse_button_icon,(self.object_rect[idx].x-self.camera_x_y[0]-15,self.object_rect[idx].y-self.camera_x_y[1]-100))
                    self.mouse_button_blit_list.append("Mouse Button Blitted")
                    return self.object_rect[idx]
    
    def level_dialogue_condition(self,event,event_list):
        if any([self.level_1,self.level_2]):
            if event.type==pygame.MOUSEBUTTONDOWN and len(self.mouse_button_blit_list)>0:
                return True 
  
    def text(self):
        if self.level_1:    
            self.test_level_1_dialogue=level_1_dialogue(self.player_icon,self.abyss_icon)[0]
            self.test_level_2_dialogue=level_1_dialogue(self.player_icon,self.abyss_icon)[1]
            self.test_level_3_dialogue=level_1_dialogue(self.player_icon,self.abyss_icon)[2]

    def get_index_object(self):
        if self.dialogue_condition:
            self.object_rect_idx=Dialouge.level_object_interaction(self)
            for idx,object in enumerate(self.object_rect):
                if self.object_rect_idx==self.object_rect[idx]:
                    return idx
                
    def text_type(self):
        if self.dialogue_condition and self.level_1:
            Dialouge.text(self)
            self.object_index=Dialouge.get_index_object(self)
            if self.object_index==1:
                self.dialogue_show=self.test_level_1_dialogue
                self.dialouge_list[0]=len(self.dialogue_show)
                return self.dialogue_show,self.dialouge_list
            elif self.object_index==2:
                self.dialogue_show=self.test_level_2_dialogue
                self.dialouge_list[0]=len(self.dialogue_show)
                return self.dialogue_show,self.dialouge_list
            elif self.object_index==3:
                self.dialogue_show=self.test_level_3_dialogue
                self.dialouge_list[0]=len(self.dialogue_show)
                return self.dialogue_show,self.dialouge_list
        else:
            self.dialogue_show="None"
        
    def beginning_condition(self):
        if self.level_2 and self.level_2_player_talk:
            return True
        
    def dialogue_condition_distance(self):
        if self.level_1:
            self.distance_talk=People.distance_dialogue(self)
        if self.level_2:
          #  if self.level_2_guard_talk:
          #      self.distance_talk=People.distance_dialogue(self)
          #  elif self.level_2_enemy_talk and not self.level_2_guard_talk:
               # self.distance_talk=EnemyTwo.distance(self)
            if self.level_2_boss_talk:
                self.distance_talk=FrostBoss.distance(self) 
            else:
                self.distance_talk=People.distance_dialogue(self)

    def level_dialogue_story(self,event,event_list):
        Dialouge.dialogue_condition_distance(self)
        if any([self.level_1,self.level_2]):
            for idx,distance in enumerate(self.distance_talk):
                if distance<200:
                    if self.level_1:
                        if self.level_1_wizard_talk: return True
                        else: return False
                    if self.level_2:
                        if self.level_2_guard_talk or (self.level_2_enemy_talk and not self.level_2_guard_talk) or self.level_2_boss_talk: 
                            return True
                        else: 
                            return False
                    
    def text_story(self):
        if self.level_1:
            self.test_level_1_dialogue=level_1_dialogue_walk_up(self.player_icon,self.elder_icon)
        if self.level_2:
            self.test_level_1_dialogue=level_2_dialogue(self.player_icon)
            self.test_level_2_dialogue=level_2_dialogue_walk_up(self.player_icon,self.guard_icon,self.brute_1_icon,self.frost_boss_icon)[0]
            self.test_level_3_dialogue=level_2_dialogue_walk_up(self.player_icon,self.guard_icon,self.brute_1_icon,self.frost_boss_icon)[1]
            self.test_level_4_dialogue=level_2_dialogue_walk_up(self.player_icon,self.guard_icon,self.brute_1_icon,self.frost_boss_icon)[2]

    def text_type_story(self):
        if self.dialogue_story_condition:
            Dialouge.text_story(self)
            if  self.level_1_wizard_talk and self.level_1:
                self.dialogue_show=self.test_level_1_dialogue
                self.dialouge_list[0]=len(self.dialogue_show)
                return self.dialogue_show,self.dialouge_list
            """if self.level_2_player_talk and self.level_2:
                self.dialogue_show=self.test_level_1_dialogue
                self.dialouge_list[0]=len(self.dialogue_show)
                return self.dialogue_show,self.dialouge_list
            if self.level_2_guard_talk and not self.level_2_player_talk and self.level_2:
                self.dialogue_show=self.test_level_2_dialogue
                self.dialouge_list[0]=len(self.dialogue_show)
                return self.dialogue_show,self.dialouge_list
            if self.level_2_enemy_talk and not self.level_2_guard_talk and self.level_2:
                self.dialogue_show=self.test_level_3_dialogue
                self.dialouge_list[0]=len(self.dialogue_show)
                return self.dialogue_show,self.dialouge_list"""
            if self.level_2 and self.level_2_boss_talk:
                self.dialogue_show=self.test_level_4_dialogue
                self.dialouge_list[0]=len(self.dialogue_show)
                return self.dialogue_show,self.dialouge_list

        else:
            self.dialogue_show="None"
               
    def scrolling_text(self):
        self.message_speed=2
        if (self.dialogue_condition or self.dialogue_story_condition) and self.dialogue_show!="None":
            for idx,dialouge in enumerate(self.dialogue_show):
                if self.dialogue_click_list[0]==idx:
                    if self.text_position[0]<self.message_speed*len(self.dialogue_show[idx][0]):
                        self.text_position[0]+=4 #0.75
                    
    def line_function(self,screen,text,position,font,colour):
        self.words=[i.split(' ') for i in text.splitlines()]
        self.space=font.size(' ')[0]
        self.width_max,self.height_max=screen.get_size()
        self.x_pos,self.y_pos=position
        for lines in self.words:
            for words in lines:
                self.word_to_surface=font.render(words,0,colour)
                self.word_w,self.word_h=self.word_to_surface.get_size()
                if self.x_pos +self.word_w>=self.width_max:
                    self.x_pos=position[0]
                    self.y_pos+=self.word_h
                screen.blit(self.word_to_surface,(self.x_pos,self.y_pos))
                self.x_pos+=self.word_w+self.space
            self.x_pos=position[0]
            self.y_pos+=self.word_h
        
    def show(self):
        Dialouge.scrolling_text(self)
        if (self.dialogue_condition or self.dialogue_story_condition) and self.dialogue_show!="None":
            self.screen_fade=pygame.Surface((SCREEN_WIDTH,SCREEN_HEIGHT))  ; self.screen_fade.set_alpha(50) ; self.screen_fade.fill((0,0,0)) ; SCREEN.blit(self.screen_fade,(0,0))
            self.text_bgackround_fade=pygame.Surface((SCREEN_WIDTH,SCREEN_HEIGHT-250))  ; self.text_bgackround_fade.set_alpha(50) ; self.text_bgackround_fade.fill((100,100,100)) ; SCREEN.blit(self.text_bgackround_fade,(0,550))
            self.font_title=pygame.font.Font(self.font,25) 
            self.font_title_render=self.font_title.render("To Continue",True,self.WHITE) 
            SCREEN.blit(self.font_title_render,(SCREEN_WIDTH//2+450,SCREEN_HEIGHT-45))
            SCREEN.blit(self.left_mouse_button_icon,(SCREEN_WIDTH//2+400,SCREEN_HEIGHT-55))
            for idx,dialouge in enumerate(self.dialogue_show):
                if self.dialogue_click_list[0]==idx:
                    self.font_title=pygame.font.Font(self.font,30) 
                    Dialouge.line_function(self,SCREEN,self.dialogue_show[idx][0][0:int(self.text_position[0])//self.message_speed],(SCREEN_WIDTH//2-350,600),self.font_title,self.WHITE)
                    self.icon_blit=SCREEN.blit(self.dialogue_show[idx][1],(SCREEN_WIDTH//2-550,SCREEN_HEIGHT-200))
                    self.font_name=pygame.font.Font(self.font,30)  ; self.font_name_render=self.font_name.render(self.dialogue_show[idx][2],True,self.WHITE)
                    SCREEN.blit(self.font_name_render,(SCREEN_WIDTH//2-550,SCREEN_HEIGHT-75))
    
    def end_dialouge(self,event,event_list):
        Dialouge.text_type(self)
        if self.dialogue_condition or self.dialogue_story_condition:
            try:
                if self.dialogue_click_list[0]>=self.dialouge_list[0]:
                    self.dialogue_click_list[0]=0
                    return True
            except IndexError:
                pass
