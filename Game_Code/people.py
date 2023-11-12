import pygame
import math

from Game_Asset_Code import * 
from .lose import Lose

class People:
    def __init__(self,level_1,level_1_wizard_talk,reset_locations,level_2):
        Lose.__init__(self,level_1,player_lose_condition,reset_locations)
        self.level_1=level_1 ; self.people_level_1_rect=people_level_1_rect ; self.player_rect=player_rect
        self.people_level_x_movement=people_level_x_movement ; self.people_level_y_movement=people_level_y_movement
        self.camera_x_y=camera_x_y ; self.elder_idle_number=elder_idle_number ; self.elder_run_number=elder_run_number
        self.level_1_wizard_talk=level_1_wizard_talk ; self.reset_locations=reset_locations ; self.people_health_list=people_health_list
        self.elder_idle_list=elder_idle_list ; self.elder_idle_list_flip=elder_idle_list_flip ; self.level_2=level_2
        self.guard_idle_list=guard_idle_list ; self.guard_idle_list_flip=guard_idle_list_flip
        self.people_level_2_rect=people_level_2_rect ; self.guard_idle_number=guard_idle_number

        self.people_level_1_x=people_level_1_x ; self.people_level_1_y=people_level_1_y
        
        if self.level_1:
            self.people_rect=self.people_level_1_rect
            self.idle_list=self.elder_idle_list
            self.idle_flip=self.elder_idle_list_flip
            self.idle_number=self.elder_idle_number
            
        if self.level_2:
            self.people_rect=self.people_level_2_rect
            self.idle_list=self.guard_idle_list
            self.idle_flip=self.guard_idle_list_flip
            self.idle_number=self.guard_idle_number

          #  print(self.guard_idle_list,self.people_rect,self.player_rect.x,self.player_rect.y)

        if any([self.level_1,self.level_2]):
            for idx,person in enumerate(self.people_rect):
                self.people_level_x_movement.append(0) ; self.people_level_y_movement.append(0) ; self.elder_idle_number.append(0) ; self.elder_run_number.append(0)
                self.people_health_list.append(100)
            if len(self.people_level_x_movement)>len(self.people_rect):
                del self.people_level_x_movement[-1], self.people_level_y_movement[-1],self.elder_idle_number[-1], self.elder_run_number[-1] , self.people_health_list[-1]

    def distance(self):
        if any([self.level_1,self.level_2]):
            self.distance_player_person=[]
            for idx,distance in enumerate(self.people_rect):
                self.player_person_distance=math.hypot(self.player_rect.x-self.people_rect[idx].x,self.player_rect.y-self.people_rect[idx].y)
                self.distance_player_person.append(self.player_person_distance)
            return self.distance_player_person
        
    def distance_dialogue(self):
        if any([self.level_1,self.level_2]):
            self.distance_player_person=[]
            for idx,distance in enumerate(self.people_rect):
                self.player_person_distance=math.hypot(self.player_rect.x-self.people_rect[idx].x,self.player_rect.y-self.people_rect[idx].y)
                self.distance_player_person.append(self.player_person_distance)
            return self.distance_player_person


    def idle(self):
        self.elder_idle_list=elder_idle_list ; self.elder_idle_list_flip=elder_idle_list_flip
        if any([self.level_1,self.level_2]):
            for idx,person in enumerate(self.people_rect):
                if self.level_1_wizard_talk and self.level_1:
                    self.people_level_x_movement[idx]=0
                if self.people_level_x_movement[idx]==0 and self.people_level_y_movement[idx]==0:
                    SCREEN.blit(self.idle_list[int(self.idle_number[idx])//2],(self.people_rect[idx].x-self.camera_x_y[0],self.people_rect[idx].y-self.camera_x_y[1]))
                  #  pygame.draw.rect(SCREEN,(100,100,100),pygame.Rect(self.people_rect[idx].x-self.camera_x_y[0],self.people_rect[idx].y-self.camera_x_y[1],32,32),width=1)
           # print(self.idle_number)
            self.idle_number[idx]+=0.10
            if self.idle_number[idx]>4: self.idle_number[idx]=0

    def run(self):
        self.elder_run_list=elder_run_list ;self.elder_run_list_flip=elder_run_list_flip 
        if any([self.level_1]):
            for idx,person in enumerate(self.people_rect):
                if not self.level_1_wizard_talk:
                      self.people_level_x_movement[idx]=-2
                self.people_rect[idx].x+=self.people_level_x_movement[idx]
                self.people_rect[idx].y+=self.people_level_y_movement[idx]
                if self.people_level_x_movement[idx]!=0 or self.people_level_y_movement[idx]!=0:
                    SCREEN.blit(self.elder_run_list_flip[int(self.elder_run_number[idx])//2],(self.people_rect[idx].x-self.camera_x_y[0],self.people_rect[idx].y-self.camera_x_y[1]))
            self.elder_run_number[idx]+=0.20
            if self.elder_run_number[idx]>9: self.elder_run_number[idx]=0

    def reset_position(self):
        if self.level_1:
            if self.reset_locations:
                for idx,person in enumerate(self.people_rect):
                    self.people_level_x_movement[idx]=0
                Lose.reset_positions_multiple(self,self.people_rect,self.people_level_1_x,self.people_level_1_y,self.people_health_list,100)
                return True



            

