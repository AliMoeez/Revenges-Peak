import pygame
import math

from Game_Asset_Code import * 

class People:
    def __init__(self,level_1):
        self.level_1=level_1 ; self.people_level_1_rect=people_level_1_rect ; self.player_rect=player_rect
        self.people_level_x_movement=people_level_x_movement ; self.people_level_y_movement=people_level_y_movement
        self.camera_x_y=camera_x_y ; self.elder_idle_number=elder_idle_number ; self.elder_run_number=elder_run_number
        if self.level_1:
            self.people_rect=self.people_level_1_rect
        if any([self.level_1]):
            for idx,person in enumerate(self.people_rect):
                self.people_level_x_movement.append(0) ; self.people_level_y_movement.append(0) ; self.elder_idle_number.append(0) ; self.elder_run_number.append(0)
            if len(self.people_level_x_movement)>len(self.people_rect):
                del self.people_level_x_movement[-1], self.people_level_y_movement[-1],self.elder_idle_number[-1], self.elder_run_number[-1]

    def distance(self):
        if any([self.level_1]):
            self.distance_player_person=[]
            for idx,distance in enumerate(self.people_rect):
                self.player_person_distance=math.hypot(self.player_rect.x-self.people_rect[idx].x,self.player_rect.y-self.people_rect[idx].y)
                self.distance_player_person.append(self.player_person_distance)
            return self.distance_player_person

    def idle(self):
        self.elder_idle_list=elder_idle_list ; self.elder_idle_list_flip=elder_idle_list_flip
        if any([self.level_1]):
            for idx,person in enumerate(self.people_rect):
                if self.people_level_x_movement[idx]==0 and self.people_level_y_movement[idx]==0:
                    SCREEN.blit(self.elder_idle_list[int(self.elder_idle_number[idx])//2],(self.people_rect[idx].x-self.camera_x_y[0],self.people_rect[idx].y-self.camera_x_y[1]))
            self.elder_idle_number[idx]+=0.10
            if self.elder_idle_number[idx]>4: self.elder_idle_number[idx]=0

    def run(self):
        self.elder_run_list=elder_run_list ;self.elder_run_list_flip=elder_run_list_flip 
        if any([self.level_1]):
            for idx,person in enumerate(self.people_rect):
              #  self.people_level_x_movement[idx]=-2
                self.people_rect[idx].x+=self.people_level_x_movement[idx]
                self.people_rect[idx].y+=self.people_level_y_movement[idx]
                if self.people_level_x_movement[idx]!=0 or self.people_level_y_movement[idx]!=0:
                        SCREEN.blit(self.elder_run_list_flip[int(self.elder_run_number[idx])//2],(self.people_rect[idx].x-self.camera_x_y[0],self.people_rect[idx].y-self.camera_x_y[1]))
            self.elder_run_number[idx]+=0.20
            if self.elder_run_number[idx]>9: self.elder_run_number[idx]=0



            

