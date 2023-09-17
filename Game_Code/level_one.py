import pygame 


from Game_Asset_Code import *
from .menu import Menu

class LevelOne(Menu):
    def __init__(self,camera_x_y,level_1,level_screen):
        self.camera_x_y=camera_x_y ; self.player_rect=player_rect ; self.test_tile_set=test_tile_set ; self.level_1=level_1
        self.level_screen=level_screen ; self.level_1_tile_set_rect=level_1_tile_set_rect

    def level_one(self):
        if self.level_1:
            self.level_screen=False
            self.camera_x_y[0]+=self.player_rect.x-self.camera_x_y[0]-525
            self.camera_x_y[1]+=self.player_rect.y-self.camera_x_y[1]-300
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
                      #  pygame.draw.rect(SCREEN,(100,100,100),pygame.Rect((x_val-self.camera_x_y[0],y_val-self.camera_x_y[1],32,32)),width=1)