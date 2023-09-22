import pygame 


from Game_Asset_Code import *
from .menu import Menu
from .control import Control

class LevelOne(Menu):
    def __init__(self,camera_x_y,level_1,level_screen):
        self.camera_x_y=camera_x_y ; self.player_rect=player_rect ; self.test_tile_set=test_tile_set ; self.level_1=level_1
        self.level_screen=level_screen ; self.level_1_tile_set_rect=level_1_tile_set_rect

    def level_one(self,player_control,player_control_cooldown):
        self.player_control=player_control ; self.player_control_cooldown=player_control_cooldown ; self.enemy_rects=enemy_1_level_1_rect+enemy_2_rects  ; self.player_control_index=player_control_index
        self.enemy_rects_camera=Control.enemy_camera(self)
        
        if self.player_control and self.player_control_cooldown[0]>0:
            self.rect_camera=self.enemy_rects_camera
        else:
            self.rect_camera=self.player_rect

        if self.level_1:
            self.level_screen=False
            self.camera_x_y[0]+=self.rect_camera.x-self.camera_x_y[0]-525
            self.camera_x_y[1]+=self.rect_camera.y-self.camera_x_y[1]-300
            for layer in self.test_tile_set:
                if layer.name=="Tile Layer 1":
                    for tile in layer.tiles():
                        x_val=tile[0]*32 ; y_val=tile[1]*32
                        SCREEN.blit(tile[2],(x_val-self.camera_x_y[0],y_val-self.camera_x_y[1]))
                if layer.name=="Tile Layer 2":
                    for tile in layer.tiles():
                        x_val=tile[0]*32 ; y_val=tile[1]*32
                        SCREEN.blit(tile[2],(x_val-self.camera_x_y[0],y_val-self.camera_x_y[1]))
                        self.level_1_tile_set_rect.append(pygame.Rect(x_val,y_val,32,32))
                        pygame.draw.rect(SCREEN,(100,100,100),pygame.Rect((x_val-self.camera_x_y[0],y_val-self.camera_x_y[1],32,32)),width=1)
