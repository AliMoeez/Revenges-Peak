import pygame

from Game_Asset_Code import *

class LevelFour:
    def __init__(self,level_4) -> None:
        self.level_4=level_4

    def background(self):
        if self.level_4:
            SCREEN.fill((100,100,100))