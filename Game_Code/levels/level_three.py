import pygame
import math

from Game_Asset_Code import * 


class LevelThree:
    def __init__(self,level_3) -> None:
        self.level_3=level_3
        self.level_3_tile_set=level_3_tile_set
        self.level_3_tile_set_rect=level_3_tile_set_rect
        self.player_rect=player_rect
        self.camera_x_y=camera_x_y
        self.object_rect=object_rect

    def distance(self,x_val,y_val,player_rect):
        self.distance_list=[]
        self.distance_player_tile=math.hypot(player_rect.x-x_val,player_rect.y-y_val)
        self.distance_list.append(self.distance_player_tile)
        return self.distance_list

    def background(self):
        self.max_x_border=3410 ; self.max_y_border=2000 ; self.min_x_border=530 ; self.min_y_border=300
        self.max_x_player=4000 ; self.max_y_player=2415; self.min_x_player=50 ; self.min_y_player=25
      #  if self.player_control and self.player_control_cooldown[0]>0: self.rect_camera=self.enemy_rects_camera
      #else
        self.rect_camera=self.player_rect

        if self.level_3:
            SCREEN.fill((132,145,65))
            if self.rect_camera.x>self.min_x_border and self.rect_camera.x<self.max_x_border and self.rect_camera.y>self.min_y_border and self.rect_camera.y<self.max_y_border:
                LevelThree.border_logic_total(self)
            if (self.rect_camera.x<self.min_x_border or self.rect_camera.x>self.max_x_border) and not self.rect_camera.y<self.min_y_border and not self.rect_camera.y>self.max_y_border:
                LevelThree.border_logic_y_axis(self)
            if (self.rect_camera.y<self.min_y_border or self.rect_camera.y>self.max_y_border) and not self.rect_camera.x<self.min_x_border and not self.rect_camera.x>self.max_x_border:
                LevelThree.border_logic_x_axis(self)
            if (self.rect_camera.y<self.min_y_border or self.rect_camera.y>self.max_y_border) and (self.rect_camera.x<self.min_x_border or self.rect_camera.x>self.max_x_border):
                LevelThree.border_logic_x_y_axis(self)

    def general_tiles(self,layers:str):
        for layer in self.level_3_tile_set:
            if layer.name==layers:
                for tile in layer.tiles():
                    x_val=tile[0]*16 ; y_val=tile[1]*16
                    self.distance_list=LevelThree.distance(self,x_val,y_val,self.player_rect)
                    for distance in self.distance_list:
                        if distance<1000:
                            SCREEN.blit(tile[2],(x_val-self.camera_x_y[0],y_val-self.camera_x_y[1]))

    def general_tile_rect(self,layers:str,rect_list:list,width:int,height:int):
        for layer in self.level_3_tile_set:
            if layer.name==layers:
                for tile in layer.tiles():
                    x_val=tile[0]*16 ; y_val=tile[1]*16
                    self.distance_list=LevelThree.distance(self,x_val,y_val,self.player_rect)
                    for distance in self.distance_list:
                        if distance<1000:
                            SCREEN.blit(tile[2],(x_val-self.camera_x_y[0],y_val-self.camera_x_y[1]))
                            rect_list.append(pygame.Rect(x_val,y_val,width,height))
                        #    pygame.draw.rect(SCREEN,(100,100,100),pygame.Rect(x_val-self.camera_x_y[0],y_val-self.camera_x_y[1],width,height),width=1)


    def ground_tiles(self):
        if self.level_3:
            LevelThree.general_tiles(self,"Tile Layer 2")

    def filler_tiles(self):
        if self.level_3:
            LevelThree.general_tiles(self,"Tile Layer 1")

    def collision_tiles(self):
        if self.level_3:
            LevelThree.general_tile_rect(self,"Tile Layer 3",self.level_3_tile_set_rect,16,16)

    def tree_top_tiles(self):
        if self.level_3:
            LevelThree.general_tiles(self,"Tile Layer 4")

    def object_tiles(self):
        if self.level_3:
            LevelThree.general_tile_rect(self,"Tile Layer 5",self.object_rect,16,16)

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





            