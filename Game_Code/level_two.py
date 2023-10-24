import pygame

from Game_Asset_Code import *


class LevelTwo:
    def __init__(self,level_2):
        self.level_2=level_2

    def backround(self):
        if self.level_2:
            SCREEN.fill((100,100,100))
        