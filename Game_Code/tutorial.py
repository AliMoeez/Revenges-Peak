import pygame

from Game_Asset_Code import *
from .dialogue import Dialouge

class Tutorial:
    def __init__(self,level_1,tutorial_one,tutorial_two):
        Dialouge.__init__(self,level_1,dialogue_condition,dialogue_story_condition,level_1_wizard_talk)
        self.tutorial_one=tutorial_one ; self.tutorial_two=tutorial_two
        self.level_1=level_1 ; self.player_rect=self.player_rect ; self.font=r"Assets\Misc\Fonts\Pixellari.ttf"  ; self.WHITE=(255,55,55) 

    def begin_tutorial(self):
        pass

    def backround(self):
        if self.tutorial_one or (self.tutorial_two and not self.tutorial_one):
            self.screen_fade=pygame.Surface((SCREEN_WIDTH,SCREEN_HEIGHT))  ; self.screen_fade.set_alpha(50) ; self.screen_fade.fill((0,0,0)) ; SCREEN.blit(self.screen_fade,(0,0))
            self.text_bgackround_fade=pygame.Surface((SCREEN_WIDTH,SCREEN_HEIGHT-250))  ; self.text_bgackround_fade.set_alpha(50) ; self.text_bgackround_fade.fill((100,100,100)) ; SCREEN.blit(self.text_bgackround_fade,(0,550))
  
    def escape_button(self):
        pass

    def text(self):
        if self.tutorial_one:
            self.tutorial_text="XYZ"
        if self.tutorial_two and not self.tutorial_one:
            self.tutorial_text="QWE"
        
    def line_movment(self):
        if self.tutorial_one or (self.tutorial_two and not self.tutorial_one):
            return Dialouge.line_function(self,SCREEN,self.tutorial_text,(SCREEN_WIDTH//2-350,600),self.font,self.WHITE)
        
    def text_movement(self):
        pass
        
    def blit(self):
        pass
        
    def skip(self):
        if self.tutorial_one or (self.tutorial_two and not self.tutorial_one):
            return True
