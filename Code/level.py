import pygame
from player import *

player=Player(player_x,player_y,player_width,player_height,player_rect)

camera_x_y=[0,0]

class Level(Player):
    def __init__(self):
        super().__init__(player_x,player_y,player_width,player_height,player_rect)
        self.camera_x_y=camera_x_y

    def level_one(self):
        self.camera_x_y[0]+=self.player_rect.x-self.camera_x_y[0]
        self.camera_x_y[1]+=self.player_rect,y-self.camera_x_y[1]

