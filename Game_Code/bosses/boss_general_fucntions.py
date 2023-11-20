import pygame

from Game_Asset_Code import *

class BossGeneralFunctions:
    def __init__(self) -> None:
        self.player_rect=player_rect
        self.camera_x_y=camera_x_y

    def idle(self,boss_rect,idle:list,idle_flip:list,idle_number:list,offset_x:int,offset_y:int,idle_max_length:int,idle_increase:float):
        if self.player_rect.x<=boss_rect.x:
            SCREEN.blit(idle[int(idle_number[0])//2],(boss_rect.x-self.camera_x_y[0]-offset_x,boss_rect.y-self.camera_x_y[1]-offset_y))
        else:
            SCREEN.blit(idle_flip[int(idle_number[0])//2],(boss_rect.x-self.camera_x_y[0]-offset_x,boss_rect.y-self.camera_x_y[1]-offset_y))
        idle_number[0]+=idle_increase
        if idle_number[0]>idle_max_length:
            idle_number[0]=0

    def move(self,boss_rect,move_list:list,move_list_flip:list,move_list_number:list,offset_x:int,
             offset_y:int,move_max_length:int,move_increase:float,boss_x_movement:list,boss_y_movement:list,x_movement:int,y_movement:int):
        
        if self.player_rect.x<=boss_rect.x:
            SCREEN.blit(move_list[int(move_list_number[0])//2],(boss_rect.x-self.camera_x_y[0]-offset_x,boss_rect.y-self.camera_x_y[1]-offset_y))
            boss_x_movement[0]=-x_movement
            if self.player_rect.y<=boss_rect.y:
                boss_y_movement[0]=-y_movement
            else:
                boss_y_movement[0]=y_movement
        
        else:
            SCREEN.blit(move_list_flip[int(move_list_number[0])//2],(boss_rect.x-self.camera_x_y[0]-offset_x,boss_rect.y-self.camera_x_y[1]-offset_y))
            boss_x_movement[0]=x_movement
            if self.player_rect.y<=boss_rect.y:
                boss_y_movement[0]=-y_movement
            else:
                boss_y_movement[0]=y_movement

        move_list_number[0]+=move_increase
        if move_list_number[0]>move_max_length:
            move_list_number[0]=0

    def collision_with_object(self,tile_rect:list,boss_rect):
        self.tile_hit=[]
        for tile in tile_rect:
            if boss_rect.colliderect(tile):
                self.tile_hit.append(tile)
        return self.tile_hit
    
    def collision_with_object_logic(self,boss_rect,boss_x_movement:list,collision,boss_y_movement:list):
        boss_rect.x+=boss_x_movement[0]
        for tile in collision:
            if boss_x_movement[0]>0:
                boss_rect.right=tile.left
            if boss_x_movement[0]<0:
                boss_rect.left=tile.right
        boss_rect.y+=boss_y_movement[0]
        for tile in collision:
            if boss_y_movement[0]>0:
                boss_rect.bottom=tile.top
            if boss_y_movement[0]<0:
                boss_rect.top=tile.bottom

