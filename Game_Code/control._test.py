import pygame


from Game_Asset_Code import *

class Control:
    def __init__(self) -> None:
        self.player_rect=player_rect
        self.camera_x_y=camera_x_y
        self.player_control_index=player_control_index
        self.player_key=player_key

    def enemy_camera(self,enemy_rects):
        for idx,enemy in enumerate(enemy_rects):
            if self.player_control_index[0]==idx:
                return enemy_rects[idx]
            
    def mechanic_idle(self):
        pass
    
    def mechanic_walk(self):
        pass

    def mechanic_attacK(self):
        pass

    def mechanic_collision(self):
        pass

    def mechanic_collision_logic(self):
        pass



