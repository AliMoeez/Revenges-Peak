import pygame

from Game_Asset_Code import *

class EnemyOne:
    def __init__(self,level_1,enemy_1_level_1_rect):
        self.level_1=level_1 ; self.camera_x_y=camera_x_y ; self.enemy_1_level_1_rect=enemy_1_level_1_rect ; self.skeleton_idle_number=skeleton_idle_number
        if level_1:
            self.enemy_1_rects=enemy_1_level_1_rect

            for idx,skeleton in enumerate(self.enemy_1_rects):
                self.skeleton_idle_number.append(0)

    def idle(self):
        self.skeleton_idle=skeleton_idle; self.skeleton_idle_flip=skeleton_idle_flip
        if any([self.level_1]):
            for idx,enemy in enumerate(self.enemy_1_rects):
                SCREEN.blit(self.skeleton_idle[int(self.skeleton_idle_number[idx]//2)],(self.enemy_1_rects[idx].x-self.camera_x_y[0],self.enemy_1_rects[idx].y-self.camera_x_y[1]))
                pygame.draw.rect(SCREEN,(100,200,200),pygame.Rect(self.enemy_1_rects[idx].x-self.camera_x_y[0]+20,self.enemy_1_rects[idx].y-self.camera_x_y[1]+12,40,70),width=1)
                self.skeleton_idle_number[idx]+=0.10
                if self.skeleton_idle_number[idx]>4: self.skeleton_idle_number[idx]=0

    def run():
        pass

    def attack():
        pass
