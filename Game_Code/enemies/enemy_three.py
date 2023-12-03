import pygame

from Game_Asset_Code import * 
from .enemy_general_functions import EnemyGeneralFunctions


class EnemyThree:
    def __init__(self,level_3,player_control) -> None:
        self.enemy_three_idle_number=enemy_three_idle_number
        self.player_control_index=player_control_index
        self.level_3=level_3
        self.enemy_3_health=enemy_3_health
        self.enemy_3_x_movement=enemy_3_x_movement
        self.enemy_3_y_movement=enemy_3_y_movement
        self.player_control_cooldown=player_control_cooldown
        self.player_control=player_control
        self.player_rect=player_rect
        self.camera_x_y=camera_x_y

        if self.level_3:
            self.tile_rect=level_3_tile_set_rect
            self.enemy_rect=enemy_3_level_3_rect
        
        if self.level_3:
            for idx,enemy in enumerate(self.enemy_rect):
                self.enemy_three_idle_number.append(0)
                self.enemy_3_health.append(100)
                self.enemy_3_x_movement.append(0)
                self.enemy_3_y_movement.append(0)
                if len(self.enemy_3_x_movement)>len(self.enemy_rect):
                    del self.enemy_three_idle_number[-1],self.enemy_3_health[1],self.enemy_3_x_movement[-1],self.enemy_3_y_movement[-1]

    def distance(self):
        if any([self.level_3]):
            self.distance=EnemyGeneralFunctions.distance(self,self.enemy_rect)
            print(self.distance)
            return self.distance
        
    def iscontrolled(self):
        if any([self.level_3]) and self.player_control and self.player_control_cooldown[0]>0  and self.player_control_index[0][1]=="Enemy_1":
            return self.player_control_index[0][0]
    
    def enemy_index(self):
        if any([self.level_3]):
            for idx,range_attacker in enumerate(self.enemy_rect):
                  if idx==self.player_control_index[0][0] and self.player_control_index[0][1]=="Enemy_3":
                      return range_attacker

    def idle(self):
        self.enemy_three_idle_list=enemy_three_idle_list ; self.enemy_three_idle_list_flip=enemy_three_idle_list_flip
        if any([self.level_3]):
            self.distance=EnemyThree.distance(self)
            
            if EnemyThree.enemy_index(self) not in self.enemy_rect:
                self.enemy_3_rects_control=self.enemy_rect
                self.enemy_3_distance_control=self.distance
            
                EnemyGeneralFunctions.idle(self,self.distance,self.player_control_index,self.enemy_3_health,self.enemy_3_x_movement,self.enemy_3_y_movement,
                                        self.enemy_three_idle_list,self.enemy_three_idle_list_flip,self.enemy_three_idle_number,self.enemy_rect,0.25,11)
                print(self.enemy_three_idle_number)
                for idx,enemy in enumerate(self.enemy_rect):
                    pygame.draw.rect(SCREEN,(100,100,100),pygame.Rect(self.enemy_rect[idx].x-self.camera_x_y[0],self.enemy_rect[idx].y-self.camera_x_y[1],30,30),width=1)
            
            if EnemyThree.enemy_index(self) in self.enemy_rect:
                self.enemy_3_rects_control=[i for i in self.enemy_rect if i!=EnemyThree.enemy_index(self)]
                self.enemy_3_distance_control=[i for idx, i in enumerate(self.distance) if idx!=self.player_control_index[0][0]]

                EnemyGeneralFunctions.idle_control(self,self.enemy_3_distance_control,self.player_control_index,self.enemy_3_health,self.enemy_3_x_movement,self.enemy_3_y_movement,
                                                   self.enemy_three_idle_list,self.enemy_three_idle_list_flip,self.enemy_three_idle_number,self.enemy_3_rects_control,0.25,11)
                 
            
    def move(self):
        pass

    def fall(self):
        pass

