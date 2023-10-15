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
                enemy_x_movement[idx]=0 ; enemy_y_movement[idx]=0
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

    def attack(self):
        pass

    def player_hit(self):
        pass
    
    def fall(self,enemy_list:list,enemy_fall_type:list,fall_right,fall_left,fall_number:list,
             enemy_health:list,increment_fall_number,fall_max:int,offset_x:int,offset_y:int):
        for idx,enemy in enumerate(enemy_list):
            if enemy_health[idx]<=0:
                if enemy_fall_type[idx]==1:
                    SCREEN.blit(fall_right[int(fall_number[idx]//2)],(enemy_list[idx].x-self.camera_x_y[0]-offset_x,enemy_list[idx].y-self.camera_x_y[1]-offset_y))
                if enemy_fall_type[idx]==2:
                    SCREEN.blit(fall_left[int(fall_number[idx]//2)],(enemy_list[idx].x-self.camera_x_y[0]-offset_x,enemy_list[idx].y-self.camera_x_y[1]-offset_y))
                fall_number[idx]+=increment_fall_number
                if fall_number[idx]>fall_max:
                    fall_number[idx]=fall_max

    def collision_with_object(self):
        pass

    def collision_with_object_logic(self):
        pass

    