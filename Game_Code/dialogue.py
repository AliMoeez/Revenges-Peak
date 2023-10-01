from Game_Asset_Code import *
from .player import Player

class Dialouge:
    def __init__(self,level_1,dialogue_condition):
        self.dialogue_condition=dialogue_condition ; self.object_rect=object_rect ; self.camera_x_y=camera_x_y ; self.player_rect=player_rect ; self.level_1=level_1 ; self.mouse_button_blit_list=mouse_button_blit_list
        self.dialogue_click_list=dialogue_click_list ; self.font=r"Assets\Misc\Fonts\Pixellari.ttf"  ; self.WHITE=(255,55,55) ; self.dialouge_list=dialouge_list

    def text(self):
        if self.level_1:    
            self.test_level_1_dialogue=[
                ("This is a test of the dialogue system",1,1),
                ("This shoul work and it if does it will be autoamted",1,1)
            ]

            self.test_level_2_dialogue=[
                ("Other Words",1,1),
                ("Nice work",1,1)
            ]
    
    def get_index_object(self):
        if self.dialogue_condition:
            self.object_rect_idx=Player.level_object_interaction(self)
            for idx,object in enumerate(self.object_rect):
                if self.object_rect_idx==self.object_rect[idx]:
                    return idx
                
    def text_type(self):
        if self.dialogue_condition:
            Dialouge.text(self)
            self.object_index=Dialouge.get_index_object(self)
            if self.object_index==1:
                self.dialogue_show=self.test_level_1_dialogue
                self.dialouge_list.append(self.test_level_1_dialogue)
                return self.dialogue_show
            elif self.object_index==2:
                self.dialogue_show=self.test_level_2_dialogue
                self.dialouge_list.append(self.test_level_2_dialogue)
                return self.dialogue_show
        if len(self.dialouge_list)>1:
            del self.dialouge_list[1:]

    def show(self):
        if self.dialogue_condition:
            self.screen_fade=pygame.Surface((SCREEN_WIDTH,SCREEN_HEIGHT))  ; self.screen_fade.set_alpha(100) ; self.screen_fade.fill((0,0,0)) ; SCREEN.blit(self.screen_fade,(0,0))
            for idx,dialouge in enumerate(self.dialogue_show):
                if self.dialogue_click_list[0]==idx:
                    self.font_title=pygame.font.Font(self.font,52) 
                    self.font_title_render=self.font_title.render(self.dialogue_show[idx][0],True,self.WHITE) 
                    SCREEN.blit(self.font_title_render,(SCREEN_WIDTH//2-170,SCREEN_HEIGHT-700))  
    
    def end_dialouge(self,event,event_list):
        Dialouge.text_type(self)
        if self.dialogue_condition:
            if self.dialogue_click_list[0]>=len(self.dialouge_list[0]):
                self.dialogue_click_list[0]=-1
                print("HERE")
                return True

        

            