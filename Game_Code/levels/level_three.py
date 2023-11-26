import pygame

from Game_Asset_Code import * 


class LevelThree:
    def __init__(self,level_3) -> None:
        self.level_3=level_3

    def background(self):
        if self.level_3:
            SCREEN.fill((121,243,135))


            