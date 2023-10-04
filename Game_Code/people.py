import pygame

from Game_Asset_Code import * 

class People:
    def __init__(self,level_1):
        self.level_1=level_1 ; self.people_level_1_rect=people_level_1_rect
        self.people_level_1_x_movement=people_level_1_x_movement ; self.people_level_1_y_movement=people_level_1_y_movement
        self.camera_x_y=camera_x_y


    def idle(self):
        self.elder_idle_list=elder_idle_list ; self.elder_idle_list_flip=elder_idle_list_flip ; self.elder_idle_number=elder_idle_number
        if self.level_1:
            for idx,person in enumerate(self.people_level_1_rect):
                SCREEN.blit(self.elder_idle_list[int(self.elder_idle_number[0])//2],(self.people_level_1_rect[idx].x-self.camera_x_y[0],self.people_level_1_rect[idx].y-self.camera_x_y[1]))
        self.elder_idle_number[0]+=0.15
        if self.elder_idle_number[0]>4: self.elder_idle_number[0]=0

    def run(self):
        if self.level_1:
            for idx,person in enumerate(self.people_level_1_rect):
                self.people_level_1_rect[idx].y+=2


            

