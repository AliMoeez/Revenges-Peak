import pygame
from Game_Asset_Code import *

class Menu:
    def __init__(self):
        self.WHITE=(255,255,255) ; self.LIGHT_BROWN=(133,70,30)
        self.backround_tile_set=backround_tile_set ; self.font=r"Assets\Misc\Fonts\Pixellari.ttf"

    def main_menu(self):
        if (not level_screen or level_screen) and not any([level_1]):
            for layer in self.backround_tile_set:
                for tile in layer.tiles():
                    x_val=tile[0]*32 ; y_val=tile[1]*32
                    SCREEN.blit(tile[2],(x_val,y_val))  

    def main_menu_buttons(self):
        if not level_screen and not any([level_1]):
            self.font_title=pygame.font.Font(self.font,52) ; self.font_title_render=self.font_title.render("Revenge's Peak",True,self.WHITE) ; SCREEN.blit(self.font_title_render,(SCREEN_WIDTH//2-170,SCREEN_HEIGHT-700))  
            self.font_play=pygame.font.Font(self.font,34) ; self.font_play_redner=self.font_play.render("Play",True,self.WHITE)
            self.font_play_surface=pygame.Surface((80,50)) ; self.font_play_surface.set_alpha(85) ; self.font_play_surface.fill(self.LIGHT_BROWN)
            self.font_play_surface_blit=SCREEN.blit(self.font_play_surface,(SCREEN_WIDTH//2-210,SCREEN_HEIGHT-407))
            SCREEN.blit(self.font_play_redner,(SCREEN_WIDTH//2-200,SCREEN_HEIGHT-400))
    
    def level_screen_blit(self,event,key):
        global level_screen
        if not level_screen and not any([level_1]):
            if event.type==pygame.MOUSEBUTTONDOWN and self.font_play_surface_blit.collidepoint(event.pos):
                level_screen= not level_screen
        if level_screen:
            if key[pygame.K_q]:level_screen=False
            self.font_selection=pygame.font.Font(self.font,52) ; self.font_selection_render=self.font_selection.render("Choose Your Level",True,self.WHITE) ; SCREEN.blit(self.font_selection_render,(SCREEN_WIDTH//2-200,SCREEN_HEIGHT-700))
            self.font_help=pygame.font.Font(self.font,28) ; self.font_help_render=self.font_help.render("Tip: Press 'Q' To Return To The Main Menu",True,self.WHITE) ; SCREEN.blit(self.font_help_render,(SCREEN_WIDTH//2-250,SCREEN_HEIGHT-600))
            self.font_help_game=pygame.font.Font(self.font,28) ; self.font_help_game_redner=self.font_help_game.render("Tip: When in Game Press 'Q' To Return To The Level Selection Menu and 'P' To Pause",True,self.WHITE)  ; SCREEN.blit(self.font_help_game_redner,(SCREEN_WIDTH//2-525,SCREEN_HEIGHT-500))              
            self.font_level_1=pygame.font.Font(self.font,50) ; self.font_level_1_render=self.font_level_1.render("1",True,self.WHITE) ; SCREEN.blit(self.font_level_1_render,(SCREEN_WIDTH//2-350,SCREEN_HEIGHT-400))
   
    def level_screen_blit_backround(self):
        if level_screen:
            self.font_play_bg_1=pygame.Surface((450,50)) ; self.font_play_bg_1.set_alpha(85) ; self.font_play_bg_1.fill(self.LIGHT_BROWN) ; self.font_play_bg_1_blit=SCREEN.blit(self.font_play_bg_1,(SCREEN_WIDTH//2-210,SCREEN_HEIGHT-705))
            self.font_play_bg_2=pygame.Surface((550,33)) ; self.font_play_bg_2.set_alpha(85) ; self.font_play_bg_2.fill(self.LIGHT_BROWN) ; self.font_play_bg_2_blit=SCREEN.blit(self.font_play_bg_2,(SCREEN_WIDTH//2-255,SCREEN_HEIGHT-605))
            self.font_play_bg_3=pygame.Surface((1075,33)) ; self.font_play_bg_3.set_alpha(85) ; self.font_play_bg_3.fill(self.LIGHT_BROWN) ; self.font_play_bg_3_blit=SCREEN.blit(self.font_play_bg_3,(SCREEN_WIDTH//2-530,SCREEN_HEIGHT-505)) 
            self.font_play_bg_level_1=pygame.Surface((50,60)) ; self.font_play_bg_level_1.set_alpha(85) ; self.font_play_bg_level_1.fill(self.LIGHT_BROWN) ; self.font_play_bg_level_1_blit=SCREEN.blit(self.font_play_bg_level_1,(SCREEN_WIDTH//2-363,SCREEN_HEIGHT-405))      
            if self.font_play_bg_level_1_blit.collidepoint(pygame.mouse.get_pos()) and event.type==pygame.MOUSEBUTTONDOWN:
                level_1=True
            
    def level_change_condition(self):
        if self.font_play_bg_level_1_blit.collidepoint(pygame.mouse.get_pos()) and event.type==pygame.MOUSEBUTTONDOWN:
            self.level_1=True
