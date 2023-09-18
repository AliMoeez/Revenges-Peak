import pygame

from Game_Asset_Code import *

class EnemyOne:
    def __init__(self,level_1,enemy_1_level_1_rect):
        self.level_1=level_1 ; self.camera_x_y=camera_x_y ; self.enemy_1_level_1_rect=enemy_1_level_1_rect
        if level_1:
            self.enemy_1_rects=enemy_1_level_1_rect

    def idle(self):
        if any([self.level_1]):
            for idx,enemy in enumerate(self.enemy_1_rects):
                SCREEN.blit(skeleton_1_idle_1,(self.enemy_1_rects[idx].x-self.camera_x_y[0],self.enemy_1_rects[idx].y-self.camera_x_y[1]))
                pygame.draw.rect(SCREEN,(100,200,200),pygame.Rect(self.enemy_1_rects[idx].x-self.camera_x_y[0]+20,self.enemy_1_rects[idx].y-self.camera_x_y[1]+12,40,70),width=1)



