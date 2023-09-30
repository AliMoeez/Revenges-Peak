from Game_Asset_Code import *
from .player import Player

class Dialouge:
    def __init__(self,level_1,dialogue_condition):
        self.dialogue_condition=dialogue_condition ; self.object_rect=object_rect ; self.camera_x_y=camera_x_y ; self.player_rect=player_rect ; self.level_1=level_1 ; self.mouse_button_blit_list=mouse_button_blit_list

    def text(self,icon_name,icon_blit):
        self.test_level_1_dialogue=[
            ("This is a test of the dialogue system",icon_name,icon_blit),
            ("This shoul work and it if does it will be autoamted",icon_name,icon_blit)
        ]

        self.test_level_2_dialogue=[
            ("Other Words",icon_name,icon_blit),
            ("Nice work",icon_name,icon_blit)
        ]
 
    def show(self):
        if self.dialogue_condition:
            self.object_rect_idx=Player.level_object_interaction(self)
            print(self.object_rect_idx,self.object_rect)
            for idx,object in enumerate(self.object_rect):
                if self.object_rect_idx==self.object_rect[idx]:
                    print(idx)
            