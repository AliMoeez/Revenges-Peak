import pygame


from Game_Asset_Code import *
from .boss_general_fucntions import BossGeneralFunctions

class GeneralBoss:
    def __init__(self,level_3,level_3_player_talk_4):
        self.level_3=level_3
        self.level_3_player_talk_4=level_3_player_talk_4
        self.general_boss_rect=general_boss_rect
        self.general_boss_health=general_boss_health
        self.player_rect=player_rect
        self.camera_x_y=camera_x_y

    def idle(self):
        self.general_boss_idle=general_boss_idle ; self.general_boss_idle_flip=general_boss_idle_flip ; self.general_boss_idle_number=general_boss_idle_number
        if self.level_3:
            pygame.draw.rect(SCREEN,(100,100,100),pygame.Rect(self.general_boss_rect.x-self.camera_x_y[0],self.general_boss_rect.y-self.camera_x_y[1],70,80),width=1)
            print(self.player_rect,self.general_boss_rect)
            BossGeneralFunctions.idle(self,self.general_boss_rect,self.general_boss_idle_flip,self.general_boss_idle,self.general_boss_idle_number,
                                    170,110,9,0.50,self.general_boss_health)


    def move(self):
        pass

    def attack(self):
        pass

    