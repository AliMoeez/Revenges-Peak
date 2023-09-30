import pygame
import math

from Game_Asset_Code import *

class Player:
    def __init__(self,player_x,player_y,player_width,player_height,player_rect,level_1,player_control,dialogue_condition):
        self.player_x=player_x ; self.player_y=player_y ; self.player_width=player_width ; self.player_height=player_height ; self.player_rect=player_rect ; self.player_x_movement=player_x_movement ; self.player_y_movement=player_y_movement
        self.camera_x_y=camera_x_y  ; self.level_1=level_1 ;  self.level_screen=level_screen ; self.player_key=player_key ; self.player_attack_cooldown=player_attack_cooldown ; self.level_1_tile_set_rect=level_1_tile_set_rect ; self.player_health=player_health
        self.player_control_cooldown=player_control_cooldown ; self.player_control=player_control ; self.object_rect=object_rect ; self.dialogue_condition=dialogue_condition
        self.mouse_button_blit_list=mouse_button_blit_list

    def distance_level_object(self):
        self.tile_interact_rect_distance=[]
        for idx,tile in enumerate(self.object_rect):
            self.tile_interact_rect_distance.append(math.hypot(self.player_rect.x-self.object_rect[idx].x,self.player_rect.y-self.object_rect[idx].y))
        return self.tile_interact_rect_distance

    def level_object_interaction(self):
        Player.distance_level_object(self)
        self.left_mouse_button_icon=left_mouse_button_icon
        if any([self.level_1]):
            self.mouse_button_blit_list.clear()
            for idx,distance in enumerate(self.tile_interact_rect_distance):
                if self.tile_interact_rect_distance[idx]<100: 
                    SCREEN.blit(self.left_mouse_button_icon,(self.object_rect[idx].x-self.camera_x_y[0]-15,self.object_rect[idx].y-self.camera_x_y[1]-100))
                    self.mouse_button_blit_list.append("Mouse Button Blitted")
                    return self.object_rect[idx]
        
    def level_dialogue_condition(self,event,event_list):
        if any([self.level_1]):
            if event.type==pygame.MOUSEBUTTONDOWN and len(self.mouse_button_blit_list)>0:
                return True 

    def idle(self,key):
        self.player_idle_list=player_idle_list ; self.player_idle_list_flip=player_idle_list_flip ; self.player_idle_number=player_idle_number
        
        if self.player_key[-1]=="d": SCREEN.blit(self.player_idle_list[int(self.player_idle_number[0])//2],(self.player_rect.x-self.camera_x_y[0]-40,self.player_rect.y-self.camera_x_y[1]-40))
        else: SCREEN.blit(self.player_idle_list_flip[int(self.player_idle_number[0])//2],(self.player_rect.x-self.camera_x_y[0]-60,self.player_rect.y-self.camera_x_y[1]-40))

        if len(self.player_key)>5: del self.player_key[0]
        
        self.player_idle_number[0]+=0.15
        if self.player_idle_number[0]>7: self.player_idle_number[0]=0

        self.player_attack_cooldown[0]+=0.02/2
        if self.player_attack_cooldown[0]>4: self.player_attack_cooldown[0]=4

    def move(self,key):
        self.player_run_list=player_run_list ; self.player_run_list_flip=player_run_list_flip ; self.player_run_number=player_run_number
        if any([self.level_1]) and not key[pygame.K_e] or self.player_attack_cooldown[0]<=0:
            if key[pygame.K_d] and not key[pygame.K_a]:
                SCREEN.blit(self.player_run_list[int(self.player_run_number[0])//2],(self.player_rect.x-self.camera_x_y[0]-40,self.player_rect.y-self.camera_x_y[1]-40))
                self.player_x_movement[0]=3  ; self.player_key.append("d")
                if key[pygame.K_w]:
                    self.player_x_movement[0]=math.sqrt(3) ; self.player_y_movement[0]=-math.sqrt(3)
                elif key[pygame.K_s]:
                    self.player_x_movement[0]=math.sqrt(3) ; self.player_y_movement[0]=math.sqrt(3)

            elif key[pygame.K_w] and not key[pygame.K_s] : 
                self.player_y_movement[0]=-3
                if self.player_key[-1]=="d": SCREEN.blit(self.player_run_list[int(self.player_run_number[0])//2],(self.player_rect.x-self.camera_x_y[0]-40,self.player_rect.y-self.camera_x_y[1]-40))
                else: SCREEN.blit(self.player_run_list_flip[int(self.player_run_number[0])//2],(self.player_rect.x-self.camera_x_y[0]-60,self.player_rect.y-self.camera_x_y[1]-40))

            elif key[pygame.K_a] and not key[pygame.K_d]:
                SCREEN.blit(self.player_run_list_flip[int(self.player_run_number[0])//2],(self.player_rect.x-self.camera_x_y[0]-60,self.player_rect.y-self.camera_x_y[1]-40))
                self.player_x_movement[0]=-3  ; self.player_key.append("a")
                if key[pygame.K_w]:
                    self.player_x_movement[0]=-math.sqrt(3); self.player_y_movement[0]=-math.sqrt(3)
                elif key[pygame.K_s]:
                    self.player_x_movement[0]=-math.sqrt(3) ; self.player_y_movement[0]=math.sqrt(3)

            elif key[pygame.K_s] and not key[pygame.K_w]: 
                self.player_y_movement[0]=3
                if self.player_key[-1]=="d": SCREEN.blit(self.player_run_list[int(self.player_run_number[0])//2],(self.player_rect.x-self.camera_x_y[0]-40,self.player_rect.y-self.camera_x_y[1]-40))
                else: SCREEN.blit(self.player_run_list_flip[int(self.player_run_number[0])//2],(self.player_rect.x-self.camera_x_y[0]-60,self.player_rect.y-self.camera_x_y[1]-40))
            
            else: 
                Player.idle(self,key) ; self.player_x_movement[0]=0 ; self.player_y_movement[0]=0
    
            self.player_run_number[0]+=0.15
            if self.player_run_number[0]>7:self.player_run_number[0]=0

            self.player_attack_cooldown[0]+=0.01/2
            if self.player_attack_cooldown[0]>4: self.player_attack_cooldown[0]=4

    def attack(self,key):
        self.player_attack_list=player_attack_list ; self.player_attack_list_flip=player_attack_list_flip ; self.player_attack_number=player_attack_number
        if any([self.level_1]) and key[pygame.K_e] and self.player_attack_cooldown[0]>0:
            self.player_x_movement[0]=0 ; self.player_y_movement[0]=0

            if self.player_key[-1]=="d":
                SCREEN.blit(self.player_attack_list[int(self.player_attack_number[0])//2],(self.player_rect.x-self.camera_x_y[0]-40,self.player_rect.y-self.camera_x_y[1]-40))
            else:
                SCREEN.blit(self.player_attack_list_flip[int(self.player_attack_number[0])//2],(self.player_rect.x-self.camera_x_y[0]-60,self.player_rect.y-self.camera_x_y[1]-40))
            self.player_attack_number[0]+=0.15
            if self.player_attack_number[0]>7: 
                self.player_attack_number[0]=0
                self.player_attack_cooldown[0]-=1
        if not key[pygame.K_e]: self.player_attack_number[0]=0

    def control(self,key):
        if any([self.level_1]):
            if self.player_control and self.player_control_cooldown[0]>0:
                self.player_control_cooldown[0]-=0.01/2 #0.01/2
                self.player_x_movement[0]=0 ; self.player_y_movement[0]=0

            if not self.player_control:
               self.player_control_cooldown[0]+=0.1/2 #0.001/2

            if self.player_control_cooldown[0]<=0: self.player_control_cooldown[0]=0
            if self.player_control_cooldown[0]>=1: self.player_control_cooldown[0]=1

    def health_power_cooldown_icons(self):
        self.maximum_health=1000 ; self.health_bar_length=500 ; self.health_bar_ratio=self.maximum_health/self.health_bar_length ; self.health_icon=health_icon
        self.sword_icon=sword_icon ; self.potion_icon=potion_icon
        if any([self.level_1]):
            
            self.health_icons=pygame.draw.rect(SCREEN,(178,34,34),pygame.Rect(20,10,self.player_health[0]/self.health_bar_ratio,25))
            SCREEN.blit(self.health_icon,(32,14)) ; self.health_border=pygame.draw.rect(SCREEN,(220,220,220),pygame.Rect(20,10,self.health_bar_length,25),4) 

            self.attack_cool_down_icon=pygame.draw.rect(SCREEN,(30,144,255),pygame.Rect(20,40,((self.player_attack_cooldown[0]*100)/2)*2.5,25))
            SCREEN.blit(self.sword_icon,(32,44)) ; self.attack_cool_down_border=pygame.draw.rect(SCREEN,(220,220,220),pygame.Rect(20,40,500,25),4)

            self.control_icon=pygame.draw.rect(SCREEN,(148,0,211),pygame.Rect(20,70,(self.player_control_cooldown[0]*1000/2),25))
            SCREEN.blit(self.potion_icon,(32,74)) ; self.control_border=pygame.draw.rect(SCREEN,(220,220,220),pygame.Rect(20,70,500,25),4)

    def fall(self):
        if any([self.level_1]): pass
          #  SCREEN.blit(frost_brute_idle_1,(200-self.camera_x_y[0],200-self.camera_x_y[1]))

    def collision_with_object(self):
        if self.level_1:
            self.tile_hit=[]
            for tiles in self.level_1_tile_set_rect:
                if self.player_rect.colliderect(tiles):
                    self.tile_hit.append(tiles)
            return self.tile_hit
                    
    def collision_with_object_logic(self):
        if self.level_1:
            self.player_rect.x+=self.player_x_movement[0]
            collision=Player.collision_with_object(self)
            for tile in collision:
                if self.player_x_movement[0]>0:
                    self.player_rect.right=tile.left
                if self.player_x_movement[0]<0:
                    self.player_rect.left=tile.right
            self.player_rect.y+=self.player_y_movement[0]
            collision=Player.collision_with_object(self)
            for tile in collision:
                if self.player_y_movement[0]>0:
                    self.player_rect.bottom=tile.top
                if self.player_y_movement[0]<0:
                    self.player_rect.top=tile.bottom


