import pygame
import math

from Game_Asset_Code import *

class EnemyGeneralFunctions:

    def __init__(self) -> None:
        self.camera_x_y=camera_x_y ; self.player_rect=player_rect

    def distance(self,enemy_rects:list):
        self.player_enemy_distance=[]
        for idx,skeleton in enumerate(enemy_rects):
            self.player_enemy_distance.append(math.hypot(self.player_rect.x-enemy_rects[idx].x,self.player_rect.y-enemy_rects[idx].y))
        return self.player_enemy_distance
    
    def idle(self,distance_list:list,player_control_list:list,enemy_health:list,enemy_x_movement:list,enemy_y_movement:list,
             enemy_idle_right,enemy_idle_left,enemy_idle_number:list,enemy_rects:list,idle_increase:int,idle_max_number:int):
        for idx,distance in enumerate(distance_list):
            if distance>200 and not player_control_list[0]==idx and enemy_health[idx]>0:
                enemy_x_movement[idx]=0 
                enemy_y_movement[idx]=0
                SCREEN.blit(enemy_idle_right[int(enemy_idle_number[idx])//2],(enemy_rects[idx].x-self.camera_x_y[0],enemy_rects[idx].y-self.camera_x_y[1]))
                enemy_idle_number[idx]+=idle_increase
                if enemy_idle_number[idx]>idle_max_number:
                    enemy_idle_number[idx]=0

    def move(self,distance_list:list,player_control_list:list,enemy_health:list,enemy_rects,enemy_run_right,enemy_run_left,enemy_run_number:list,
             enemy_x_movement:list,enemy_y_movement:list,enemy_run_increment:int,enemy_run_max:int):
        for idx,distance in enumerate(distance_list):
            if distance>=100 and distance<=200 and enemy_health[idx]>0 and not player_control_list[0]==idx:
                if self.player_rect.x>=enemy_rects[idx].x: SCREEN.blit(enemy_run_right[int(enemy_run_number[idx])//2],(enemy_rects[idx].x-self.camera_x_y[0],enemy_rects[idx].y-self.camera_x_y[1]))
                else: SCREEN.blit(enemy_run_left[int(enemy_run_number[idx])//2],(enemy_rects[idx].x-self.camera_x_y[0],enemy_rects[idx].y-self.camera_x_y[1]))
                enemy_run_number[idx]+=enemy_run_increment
                if enemy_run_number[idx]>enemy_run_max: enemy_run_number[idx]=0
                if self.player_rect.x>=enemy_rects[idx].x:
                    enemy_x_movement[idx]=1
                    if self.player_rect.y<enemy_rects[idx].y: enemy_y_movement[idx]=-1
                    if self.player_rect.y>=enemy_rects[idx].y: enemy_y_movement[idx]=1
                if self.player_rect.x<enemy_rects[idx].x:
                    enemy_x_movement[idx]=-1
                    if self.player_rect.y<enemy_rects[idx].y: enemy_y_movement[idx]=-1
                    if self.player_rect.y>=enemy_rects[idx].y: enemy_y_movement[idx]=1

    def attack(self,distance_list:list,enemy_health:list,player_control_list:list,enemy_x_movement:list,enemy_y_movement:list,enemy_attack_right,enemy_attack_left,
               enemy_attack_number:list,enemy_rects:list,enemy_fall_type:list,attack_number_increment:int,attack_number_max:int,
               offset_x_right:int,offset_x_left:int,offset_y_right:int,offset_y_left:int,player_health:list,health_reduction:int):
        for idx,distance in enumerate(distance_list):
            if distance<100 and enemy_health[idx]>0 and not player_control_list[0]==idx:
                enemy_x_movement[idx]=0 
                enemy_y_movement[idx]=0
                if self.player_rect.x>=enemy_rects[idx].x:
                    SCREEN.blit(enemy_attack_right[int(enemy_attack_number[idx])//2],(enemy_rects[idx].x-self.camera_x_y[0]-offset_x_right,enemy_rects[idx].y-self.camera_x_y[1]-offset_y_right))
                    enemy_fall_type[idx]=1
                else:
                    SCREEN.blit(enemy_attack_left[int(enemy_attack_number[idx])//2],(enemy_rects[idx].x-self.camera_x_y[0]-offset_x_left,enemy_rects[idx].y-self.camera_x_y[1]-offset_y_left))
                    enemy_fall_type[idx]=2
                enemy_attack_number[idx]+=attack_number_increment
                if enemy_attack_number[idx]>attack_number_max:
                    enemy_attack_number[idx]=0
                    player_health[0]-=health_reduction
                

    def player_hit(self,font,colour:tuple,distance_list:list,player_attack_length:list,enemy_health:list,enemy_rects:list,player_key_list:list,offset_x:int):
        self.font_hit=pygame.font.Font(font,15)
        self.font_hit_render=self.font_hit.render("-25",True,colour)
        for idx,distance in enumerate(distance_list):
            if player_attack_length[0]>6.0 and distance<100 and enemy_health[idx]>0:
                if self.player_rect.x<=enemy_rects[idx].x and player_key_list[-1]=='d':
                    SCREEN.blit(self.font_hit_render,(enemy_rects[idx].x-self.camera_x_y[0]+offset_x,enemy_rects[idx].y-self.camera_x_y[1]))
                    enemy_health[idx]-=50
                if self.player_rect.x>=enemy_rects[idx].x and player_key_list[-1]=='a':
                        SCREEN.blit(self.font_hit_render,(enemy_rects[idx].x-self.camera_x_y[0]+offset_x,enemy_rects[idx].y-self.camera_x_y[1]))
                        enemy_health[idx]-=50
                
    
    def fall(self,enemy_list:list,enemy_fall_type:list,fall_right,fall_left,fall_number:list,
             enemy_health:list,increment_fall_number,fall_max:int,offset_x:int,offset_y:int,enemy_x_movement:list,enemy_y_movement:list):
        for idx,enemy in enumerate(enemy_list):
            if enemy_health[idx]<=0:
                enemy_x_movement[idx]=0 ; enemy_y_movement[idx]=0
                if enemy_fall_type[idx]==1:
                    SCREEN.blit(fall_right[int(fall_number[idx]//2)],(enemy_list[idx].x-self.camera_x_y[0]-offset_x,enemy_list[idx].y-self.camera_x_y[1]-offset_y))
                if enemy_fall_type[idx]==2:
                    SCREEN.blit(fall_left[int(fall_number[idx]//2)],(enemy_list[idx].x-self.camera_x_y[0]-offset_x,enemy_list[idx].y-self.camera_x_y[1]-offset_y))
                fall_number[idx]+=increment_fall_number
                if fall_number[idx]>fall_max:
                    fall_number[idx]=fall_max

    def collision_with_object(self,tile_level_list,enemy_rects:list):
        self.tile_hit=[]
        for tile in tile_level_list:
            for idx,enemy in enumerate(enemy_rects):
                if enemy.colliderect(tile):
                    self.tile_hit.append(tile)
        return self.tile_hit

    def collision_with_object_logic(self,enemy_rects:list,enemy_x_movement:list,enemy_y_movement:list,collision):
        for idx,enemy in enumerate(enemy_rects):
            enemy_rects[idx].x+=enemy_x_movement[idx]
            for tile in collision:
                if enemy_x_movement[idx]>0:
                    enemy_rects[idx].right=tile.left
                if enemy_x_movement[idx]<0:
                    enemy_rects[idx].left=tile.right
            enemy_rects[idx].y+=enemy_y_movement[idx]
            for tile in collision:
                if enemy_y_movement[idx]>0:
                    enemy_rects[idx].bottom=tile.top
                if enemy_y_movement[idx]<0:
                    enemy_rects[idx].top=tile.bottom




    