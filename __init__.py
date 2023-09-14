import pygame,sys
from pytmx.util_pygame import load_pygame
from Game_Asset_Code.general_assets import *
from Game_Asset_Code.player_assets import *
from Game_Asset_Code.boss_assets import *
from Game_Asset_Code.enemy_assets import *

pygame.init()

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
    
    def level_screen_blit(self):
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
        global level_1
        if level_screen:
            self.font_play_bg_1=pygame.Surface((450,50)) ; self.font_play_bg_1.set_alpha(85) ; self.font_play_bg_1.fill(self.LIGHT_BROWN) ; self.font_play_bg_1_blit=SCREEN.blit(self.font_play_bg_1,(SCREEN_WIDTH//2-210,SCREEN_HEIGHT-705))
            self.font_play_bg_2=pygame.Surface((550,33)) ; self.font_play_bg_2.set_alpha(85) ; self.font_play_bg_2.fill(self.LIGHT_BROWN) ; self.font_play_bg_2_blit=SCREEN.blit(self.font_play_bg_2,(SCREEN_WIDTH//2-255,SCREEN_HEIGHT-605))
            self.font_play_bg_3=pygame.Surface((1075,33)) ; self.font_play_bg_3.set_alpha(85) ; self.font_play_bg_3.fill(self.LIGHT_BROWN) ; self.font_play_bg_3_blit=SCREEN.blit(self.font_play_bg_3,(SCREEN_WIDTH//2-530,SCREEN_HEIGHT-505)) 
            self.font_play_bg_level_1=pygame.Surface((50,60)) ; self.font_play_bg_level_1.set_alpha(85) ; self.font_play_bg_level_1.fill(self.LIGHT_BROWN) ; self.font_play_bg_level_1_blit=SCREEN.blit(self.font_play_bg_level_1,(SCREEN_WIDTH//2-363,SCREEN_HEIGHT-405))      
            if self.font_play_bg_level_1_blit.collidepoint(pygame.mouse.get_pos()) and event.type==pygame.MOUSEBUTTONDOWN:
                level_1=True

class LevelOne(Menu):
    def __init__(self,camera_x_y):
        super().__init__()
        self.camera_x_y=camera_x_y ; self.player_rect=player_rect ; self.test_tile_set=test_tile_set

    def level_one(self):
        if level_1:
            self.camera_x_y[0]+=self.player_rect.x-self.camera_x_y[0]
            self.camera_x_y[1]+=self.player_rect.y-self.camera_x_y[1]
            for layer in self.test_tile_set:
                for tile in layer.tiles():
                    x_val=tile[0]*32 ; y_val=tile[1]*32
                    SCREEN.blit(tile[2],(x_val-self.camera_x_y[0],y_val-self.camera_x_y[1]))


class Player(LevelOne):
    def __init__(self,player_x,player_y,player_width,player_height,player_rect):
        super().__init__(camera_x_y)
        self.player_x=player_x ; self.player_y=player_y ; self.player_width=player_width ; self.player_height=player_height ; self.player_rect=player_rect ; self.player_x_movement=player_x_movement ; self.player_y_movement=player_y_movement

    def idle(self):
        self.player_idle=player_idle ; self.player_idle_flip=player_idle_flip
        if level_1:
            if not key[pygame.K_d] and not key[pygame.K_a] and not key[pygame.K_w] and not key[pygame.K_s]:
                SCREEN.blit(self.player_idle[0],(self.player_rect.x-self.camera_x_y[0],self.player_rect.y-self.camera_x_y[1]))
            SCREEN.blit(frost_brute_idle_1,(200-self.camera_x_y[0],200-self.camera_x_y[1]))
            SCREEN.blit(skeleton_1_idle_1,(400-self.camera_x_y[0],200-self.camera_x_y[1]))

    def move(self):
        self.player_run=player_run ; self.player_run_flip=player_run_flip ; self.player_run_number=player_run_number
        if level_1:
            if key[pygame.K_d]:
                self.player_x_movement[0]=2
                if key[pygame.K_w]:
                    self.player_x_movement[0]=1 ; self.player_y_movement[0]=-1
            elif key[pygame.K_w]: self.player_y_movement[0]=-2
            elif key[pygame.K_a]:
                self.player_x_movement[0]=-2
                if key[pygame.K_s]:
                    self.player_x_movement[0]=-1 ; self.player_y_movement[0]=1
            elif key[pygame.K_s]: self.player_y_movement[0]=2
            else: 
                self.player_x_movement[0]=0 
                self.player_y_movement[0]=0
            if key[pygame.K_d] or key[pygame.K_d] and key[pygame.K_w] or key[pygame.K_w]:
                SCREEN.blit(self.player_run[int(self.player_run_number[0])//2],(self.player_rect.x-self.camera_x_y[0],self.player_rect.y-self.camera_x_y[1]))
            if key[pygame.K_a] or key[pygame.K_a] and key[pygame.K_s] or key[pygame.K_s]:
                SCREEN.blit(self.player_run_flip[int(self.player_run_number[0])//2],(self.player_rect.x-self.camera_x_y[0],self.player_rect.y-self.camera_x_y[1]))

            self.player_run_number[0]+=0.10
            if self.player_run_number[0]>10:self.player_run_number[0]=0

    def collision(self):
        if level_1:
            self.player_rect.x+=self.player_x_movement[0]
            self.player_rect.y+=self.player_y_movement[0]

while run:
    SCREEN.fill((0,0,0))
    key=pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit() 
            sys.exit()

    menu=Menu()
    menu.main_menu()
    menu.main_menu_buttons()
    menu.level_screen_blit_backround()
    menu.level_screen_blit()

    levelone=LevelOne(camera_x_y)
    levelone.level_one()

    player=Player(player_x,player_y,player_width,player_height,player_rect)
    player.idle()
    player.move()
    player.collision()

    pygame.display.update()

