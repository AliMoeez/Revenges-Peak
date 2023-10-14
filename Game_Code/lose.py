import pygame

from Game_Asset_Code import *


class Lose:
    def __init__(self,level_1,player_lose_condition,reset_locations):
        self.level_1=level_1 
        self.reset_locations=reset_locations
        self.player_health=player_health ; self.player_lose_condition=player_lose_condition
        self.font=r"Assets\Misc\Fonts\Pixellari.ttf" 
        self.RED=(220,20,60) ; self.WHITE=(255,255,255)
        self.screen_fade_number=screen_fade_number
        self.reset_length=reset_length

    def condition(self):
        if any([self.level_1]):
            if self.player_health[0]<0:
                return True
            
    def screen_fade(self):
        self.screen_fade=pygame.Surface((SCREEN_WIDTH,SCREEN_HEIGHT))  ; self.screen_fade.set_alpha(self.screen_fade_number[0]) 
        self.screen_fade.fill((0,0,0))  ; SCREEN.blit(self.screen_fade,(0,0))
     
    def text(self):
        self.font_title=pygame.font.Font(self.font,52) 
        self.font_title_render=self.font_title.render("YOU LOSE",True,self.RED) ; SCREEN.blit(self.font_title_render,(SCREEN_WIDTH//2-150,SCREEN_HEIGHT-700))  
       
        self.font_main_menu=pygame.font.Font(self.font,34) 
        self.font_main_menu_render=self.font_main_menu.render("Main Menu",True,self.RED)

        self.font_retry=pygame.font.Font(self.font,34) 
        self.font_retry_render=self.font_retry.render("Retry",True,self.RED)
          
    def buttons(self):
        self.font_menu_surface=pygame.Surface((170,50))  ; self.font_menu_surface.set_alpha(0)  ; self.font_menu_surface.fill(self.WHITE)
        self.font_menu_surface_blit=SCREEN.blit(self.font_menu_surface,(SCREEN_WIDTH//2-310,SCREEN_HEIGHT-407)) 
        self.main_menu_blit=SCREEN.blit(self.font_main_menu_render,(SCREEN_WIDTH//2-300,SCREEN_HEIGHT-400))

        self.font_retry_surface=pygame.Surface((100,50))  ; self.font_retry_surface.set_alpha(0)  ; self.font_retry_surface.fill(self.WHITE)
        self.font_retry_surface_blit=SCREEN.blit(self.font_retry_surface,(SCREEN_WIDTH//2+90,SCREEN_HEIGHT-407)) 
        self.retry_blit=SCREEN.blit(self.font_retry_render,(SCREEN_WIDTH//2+100,SCREEN_HEIGHT-400))

    def show_loss(self):
        if self.player_lose_condition:
            self.screen_fade_number[0]+=1
            if self.screen_fade_number[0]>200: self.screen_fade_number[0]=200
            Lose.screen_fade(self)
            Lose.text(self)
            Lose.buttons(self)

    def retry(self,event):
        if self.player_lose_condition:
            Lose.text(self)
            Lose.buttons(self)
            if event.type==pygame.MOUSEBUTTONDOWN and self.retry_blit.collidepoint(pygame.mouse.get_pos()):
                self.player_health[0]=1000
                return True

    def back_to_menu(self,event):
        if self.player_lose_condition:
            Lose.text(self)
            Lose.buttons(self)
            if event.type==pygame.MOUSEBUTTONDOWN and self.main_menu_blit.collidepoint(pygame.mouse.get_pos()):
                self.player_health[0]=1000
                return True

    def reset_positions(self,object,x_pos:int,y_pos:int):
        if self.reset_locations:
            object.x=x_pos
            object.y=y_pos
            return object
        
    def reset_positions_multiple(self,object:list,x_pos:list,y_pos:list):
        if self.reset_locations:
            for idx,charactor in enumerate(object):
                object[idx].x=x_pos[idx]
                object[idx].y=y_pos[idx]
            return object
        

