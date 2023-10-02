from Game_Asset_Code import *
from .player import Player

class Dialouge:
    def __init__(self,level_1,dialogue_condition):
        self.dialogue_condition=dialogue_condition ; self.object_rect=object_rect ; self.camera_x_y=camera_x_y ; self.player_rect=player_rect ; self.level_1=level_1 ; self.mouse_button_blit_list=mouse_button_blit_list
        self.dialogue_click_list=dialogue_click_list ; self.font=r"Assets\Misc\Fonts\Pixellari.ttf"  ; self.WHITE=(255,55,55) ; self.dialouge_list=dialouge_list
        self.player_icon=player_icon ; self.abyss_icon=abyss_icon

    def text(self):
        if self.level_1:    
            self.test_level_1_dialogue=[
                ("This is a test of the dialogue system",self.player_icon,"You"),
                ("This shoul work and it if does it will be autoamted",self.abyss_icon,"The Abyss"),
            ]

            self.test_level_2_dialogue=[
                ("Other Words",self.player_icon,"You"),
                ("Nice work",self.abyss_icon,"The Abyss"),
                ("work",self.player_icon,"You"),
                ("Nice ",self.abyss_icon,"The Abyss"),
                ("Nices work",self.player_icon,"You")
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

    
    def scrolling_text(self):
        self.message_speed=2
        self.text_position=0
        if self.dialogue_condition:
            for idx,dialouge in enumerate(self.dialogue_show):
                if self.dialogue_click_list[0]==idx:
                    if self.text_position<self.message_speed*len(self.dialogue_show[idx][0]):
                        self.text_position+=1
                    else:
                        self.text_position=0
            print(self.text_position)


    def show(self):
        Dialouge.scrolling_text(self)
        if self.dialogue_condition:
            self.screen_fade=pygame.Surface((SCREEN_WIDTH,SCREEN_HEIGHT))  ; self.screen_fade.set_alpha(50) ; self.screen_fade.fill((0,0,0)) ; SCREEN.blit(self.screen_fade,(0,0))
            self.text_bgackround_fade=pygame.Surface((SCREEN_WIDTH,SCREEN_HEIGHT-250))  ; self.text_bgackround_fade.set_alpha(50) ; self.text_bgackround_fade.fill((100,100,100)) ; SCREEN.blit(self.text_bgackround_fade,(0,550))
            for idx,dialouge in enumerate(self.dialogue_show):
                if self.dialogue_click_list[0]==idx:
                    
                    self.font_title=pygame.font.Font(self.font,30) ; self.font_title_render=self.font_title.render(self.dialogue_show[idx][0][0:self.text_position//self.message_speed],True,self.WHITE) 
                    SCREEN.blit(self.font_title_render,(SCREEN_WIDTH//2-350,SCREEN_HEIGHT-200))  

                    self.icon_blit=SCREEN.blit(self.dialogue_show[idx][1],(SCREEN_WIDTH//2-550,SCREEN_HEIGHT-200))

                    self.font_name=pygame.font.Font(self.font,30)  ; self.font_name_render=self.font_name.render(self.dialogue_show[idx][2],True,self.WHITE)
                    SCREEN.blit(self.font_name_render,(SCREEN_WIDTH//2-550,SCREEN_HEIGHT-75))  

    
    def end_dialouge(self,event,event_list):
        Dialouge.text_type(self)
        if self.dialogue_condition:
            if self.dialogue_click_list[0]>=len(self.dialouge_list[0]):
                self.dialogue_click_list[0]=-1
                return True

        

            