import pygame 


from Game_Asset_Code import *
from .menu import Menu
from .control import Control
from .player import Player
from .objectives import Objectives

class LevelOne(Menu):
    def __init__(self,camera_x_y,level_1,level_screen,level_1_wizard_talk,talk_to_abyss_level_one,investigate_object_level_one):
        Objectives.__init__(self,level_1,level_1_wizard_talk,talk_to_abyss_level_one,investigate_object_level_one,dialogue_objective_list)
        self.camera_x_y=camera_x_y ; self.player_rect=player_rect ; self.level_1_tile_set=level_1_tile_set ; self.level_1=level_1
        self.level_screen=level_screen ; self.level_1_tile_set_rect=level_1_tile_set_rect ; self.object_rect=object_rect
        self.dialogue_condition=dialogue_condition 
        self.level_1_wizard_talk=level_1_wizard_talk ; self.talk_to_abyss_level_one=talk_to_abyss_level_one ; self.investigate_object_level_one=investigate_object_level_one 

    def border(self):
        self.player_control=player_control ; self.player_control_cooldown=player_control_cooldown ; self.enemy_rects=enemy_1_level_1_rect+enemy_2_rects  ; self.player_control_index=player_control_index
        self.enemy_rects_camera=Control.enemy_camera(self) 
        self.max_x_border=4000 ; self.max_y_border=2000 ; self.min_x_border=530 ; self.min_y_border=300
        self.max_x_player=4590 ; self.max_y_player=2415; self.min_x_player=50 ; self.min_y_player=25
      
        if self.player_control and self.player_control_cooldown[0]>0: self.rect_camera=self.enemy_rects_camera
        else: self.rect_camera=self.player_rect

        if self.level_1: 
            self.level_screen=False
            if self.rect_camera.x>self.min_x_border and self.rect_camera.x<self.max_x_border and self.rect_camera.y>self.min_y_border and self.rect_camera.y<self.max_y_border:
                 LevelOne.border_logic_total(self)
            if (self.rect_camera.x<self.min_x_border or self.rect_camera.x>self.max_x_border) and not self.rect_camera.y<self.min_y_border and not self.rect_camera.y>self.max_y_border:
                LevelOne.border_logic_y_axis(self)
            if (self.rect_camera.y<self.min_y_border or self.rect_camera.y>self.max_y_border) and not self.rect_camera.x<self.min_x_border and not self.rect_camera.x>self.max_x_border:
                LevelOne.border_logic_x_axis(self)
            if (self.rect_camera.y<self.min_y_border or self.rect_camera.y>self.max_y_border) and (self.rect_camera.x<self.min_x_border or self.rect_camera.x>self.max_x_border):
                LevelOne.border_logic_x_y_axis(self)

    def tile_set_function(self,layers:str):
        if self.level_1:
            self.level_screen=False
            for layer in self.level_1_tile_set:
                if layer.name in [layers]:
                    for tile in layer.tiles():
                        x_val=tile[0]*32 ; y_val=tile[1]*32
                        SCREEN.blit(tile[2],(x_val-self.camera_x_y[0],y_val-self.camera_x_y[1]))
                        if layer.name=="Tile Layer 5":
                            self.object_rect.append(pygame.Rect(x_val,y_val,32,32))

    def tile_set_level_direction(self):
        LevelOne.tile_set_function(self,"Tile Layer 5")

    def tile_set(self):
        if self.level_1:
            self.level_screen=False
            for layer in self.level_1_tile_set:
                if layer.name in ["Tile Layer 1","Tile Layer 2"]:
                    for tile in layer.tiles():
                        x_val=tile[0]*32 ; y_val=tile[1]*32
                        SCREEN.blit(tile[2],(x_val-self.camera_x_y[0],y_val-self.camera_x_y[1]))
                if layer.name=="Tile Layer 3":
                    for tile in layer.tiles():
                        x_val=tile[0]*32 ; y_val=tile[1]*32
                        SCREEN.blit(tile[2],(x_val-self.camera_x_y[0],y_val-self.camera_x_y[1]))
                        self.level_1_tile_set_rect.append(pygame.Rect(x_val,y_val,32,32))

    def tile_set_tree_top(self):
        LevelOne.tile_set_function(self,"Tile Layer 4")

    def win_condition(self):
        if self.level_1:
            if not self.investigate_object_level_one and Objectives.level_one_objectives(self)[0]<200:
                return True
            return False
            
    def border_logic_total(self):
        self.camera_x_y[0]+=self.rect_camera.x-self.camera_x_y[0]-525
        self.camera_x_y[1]+=self.rect_camera.y-self.camera_x_y[1]-self.min_y_border
    
    def border_logic_y_axis(self):
        self.camera_x_y[0]+=0
        self.camera_x_y[1]+=self.rect_camera.y-self.camera_x_y[1]-self.min_y_border
        if self.rect_camera.x<self.min_x_player: self.rect_camera.x=self.min_x_player
        if self.rect_camera.x>self.max_x_player: self.rect_camera.x=self.max_x_player

    def border_logic_x_axis(self):
        self.camera_x_y[0]+=self.rect_camera.x-self.camera_x_y[0]-525
        self.camera_x_y[1]+=0
        if self.rect_camera.y<self.min_y_player: self.rect_camera.y=self.min_y_player
        if self.rect_camera.y>self.max_y_player:self.rect_camera.y=self.max_y_player
            
    def border_logic_x_y_axis(self):
        self.camera_x_y[0]+=0 ; self.camera_x_y[1]+=0
        if self.rect_camera.y<self.min_y_player: self.rect_camera.y=self.min_y_player
        if self.rect_camera.x<self.min_x_player: self.rect_camera.x=self.min_x_player
        if self.rect_camera.x>self.max_x_player: self.rect_camera.x=self.max_x_player
        if self.rect_camera.y>self.max_y_player:self.rect_camera.y=self.max_y_player
