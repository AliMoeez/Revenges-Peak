import pygame 


from Game_Asset_Code import *
from .menu import Menu

class LevelOne(Menu):
    def __init__(self,camera_x_y,level_1,level_screen):
      #  super().__init__(level_screen,level_1)
        self.camera_x_y=camera_x_y ; self.player_rect=player_rect ; self.test_tile_set=test_tile_set ; self.level_1=level_1
        self.level_screen=level_screen

    def level_one(self):
        if self.level_1:
            self.camera_x_y[0]+=self.player_rect.x-self.camera_x_y[0]
            self.camera_x_y[1]+=self.player_rect.y-self.camera_x_y[1]
            for layer in self.test_tile_set:
                for tile in layer.tiles():
                    x_val=tile[0]*32 ; y_val=tile[1]*32
                    SCREEN.blit(tile[2],(x_val-self.camera_x_y[0],y_val-self.camera_x_y[1]))