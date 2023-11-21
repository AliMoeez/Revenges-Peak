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
             offset_y:int,move_max_length:int,move_increase:float,boss_x_movement:list,boss_y_movement:list,x_movement:int,y_movement:int,attack_list_number): 
        attack_list_number[0]=0
        if self.player_rect.x<=boss_rect.x:
            SCREEN.blit(move_list[int(move_list_number[0])//2],(boss_rect.x-self.camera_x_y[0]-offset_x,boss_rect.y-self.camera_x_y[1]-offset_y))
            boss_x_movement[0]=-x_movement
            if self.player_rect.y<=boss_rect.y: boss_y_movement[0]=-y_movement
            else: boss_y_movement[0]=y_movement 
        else:
            SCREEN.blit(move_list_flip[int(move_list_number[0])//2],(boss_rect.x-self.camera_x_y[0]-offset_x,boss_rect.y-self.camera_x_y[1]-offset_y))
            boss_x_movement[0]=x_movement
            if self.player_rect.y<=boss_rect.y: boss_y_movement[0]=-y_movement
            else: boss_y_movement[0]=y_movement
        move_list_number[0]+=move_increase
        if move_list_number[0]>move_max_length: move_list_number[0]=0

    def attack(self,boss_rect,attack_list:list,attack_list_flip:list,attack_list_number:list,offset_x:int,offset_y:int,
               attack_max_length:int,attack_increase:float,boss_x_movement:list,boss_y_movement:list):
        boss_x_movement[0]=0 
        boss_y_movement[0]=0
        if self.player_rect.x<=boss_rect.x:
            SCREEN.blit(attack_list[int(attack_list_number[0])//2],(boss_rect.x-self.camera_x_y[0]-offset_x,boss_rect.y-self.camera_x_y[1]-offset_y))
        else:
            SCREEN.blit(attack_list_flip[int(attack_list_number[0])//2],(boss_rect.x-self.camera_x_y[0]-offset_x,boss_rect.y-self.camera_x_y[1]-offset_y))
        attack_list_number[0]+=attack_increase
        if attack_list_number[0]>attack_max_length:
            attack_list_number[0]=-2

    def health(self,boss_health,boss_max_health,health_bar_length,health_bar_ratio,health_icon):
        self.health_icon=pygame.draw.rect(SCREEN,(173,216,230),pygame.Rect(670,10,boss_health[0]/health_bar_ratio,25))
        SCREEN.blit(health_icon,(682,14))
        self.health_border=pygame.draw.rect(SCREEN,(220,220,220),pygame.Rect(670,10,health_bar_length,25),4)

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

