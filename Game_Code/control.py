import pygame
import math

from Game_Asset_Code import *

class Control:
    def __init__(self,level_1,player_control,player_control_index):
        self.player_rect=player_rect ; self.enemy_1_level_1_rect=enemy_1_level_1_rect ; self.level_1=level_1 ; self.player_control_index=player_control_index
        self.player_control=player_control ; self.player_control_cooldown=player_control_cooldown ; self.enemy_1_level_1_rect=enemy_1_level_1_rect 
        self.camera_x_y=camera_x_y ; self.enemy_run_number=enemy_run_number ; self.enemy_idle_number=enemy_idle_number ; self.player_key=player_key
        self.enemy_attack_number=enemy_attack_number ; self.enemy_2_level_1_rects=enemy_2_rects ; self.enemy_x_movement=enemy_x_movement ; self.enemy_y_movement=enemy_y_movement
        self.level_1_tile_set_rect=level_1_tile_set_rect

        if self.level_1:
          #  self.enemy_rects=self.enemy_1_level_1_rect+self.enemy_2_level_1_rects 
            self.tile_set=self.level_1_tile_set_rect
           # self.enemy_rects_type=[]

            self.enemy_rects=[]

            for idx,enemy in enumerate(self.enemy_1_level_1_rect):
                self.enemy_rects.append((self.enemy_1_level_1_rect[idx],"Enemy_1"))
            for idx,enemy in enumerate(self.enemy_2_level_1_rects):
                self.enemy_rects.append((self.enemy_2_level_1_rects[idx],"Enemy_2"))

#            print(self.enemy_rects)

          #  for idx,enemy_1 in enumerate(self.enemy_1_level_1_rect):
          #      self.enemy_rects_type.append("Enemy_1")
          #  for idx,enemy_2 in enumerate(self.enemy_2_level_1_rects):
          #      self.enemy_rects_type.append("Enemy_2")

    def distance(self):
        if any([self.level_1]):
            self.player_enemy_distance=[]
            for idx,enemy in enumerate(self.enemy_rects):
                self.player_enemy_distance.append(math.hypot(self.player_rect.x-self.enemy_rects[idx][0].x,self.player_rect.y-self.enemy_rects[idx][0].y))
            return self.player_enemy_distance
        
    def enemy_definition(self):
        if any([self.level_1]):
            for idx,enemy in enumerate(self.enemy_rects):
             #   for idy,enemy in enumerate(self.enemy_rects_type):
                    if self.player_control_index[0]==idx:
                     #   if idx==idy:
                            if self.enemy_rects[self.player_control_index[0]][1]=="Enemy_1":
                                self.enemy_walk=skeleton_run ; self.enemy_walk_flip=skeleton_run_flip 
                                self.enemy_idle=skeleton_idle  ; self.enemy_idle_flip=skeleton_idle_flip 
                                self.enemy_attack=skeleton_attack ; self.enemy_attack_flip=skeleton_attack_flip
                            if self.enemy_rects[self.player_control_index[0]][1]=="Enemy_2":
                                self.enemy_idle=brute_1_idle  ; self.enemy_idle_flip=brute_1_idle
                                self.enemy_walk=brute_1_run ; self.enemy_walk_flip=brute_1_run_flip
                                self.enemy_attack=brute_1_attack_1 ; self.enemy_attack_flip=brute_1_attack_flip_1

    def enemy_camera(self):
        if any([self.level_1]):
            for idx,enemy in enumerate(self.enemy_rects):
                if self.player_control_index[0]==idx:
                    return self.enemy_rects[idx][0]
                
    def enemy_index(self):
        if any([self.level_1]):
            for idx,enemy in enumerate(self.enemy_rects):
                if self.player_control_index[0]==idx:
                    if enemy in self.enemy_2_level_1_rects:
                        for idy,enemy_2 in enumerate(self.enemy_2_level_1_rects):
                            if enemy==enemy_2:
                                return idy
        
    def mechanic_idle(self,key):
        if self.player_key[-1]=='d':
            SCREEN.blit(self.enemy_idle[int(self.enemy_idle_number[0]//2)],(self.enemy_rects[self.player_control_index[0]][0].x-self.camera_x_y[0],self.enemy_rects[self.player_control_index[0]][0].y-self.camera_x_y[1]))
        else:
            SCREEN.blit(self.enemy_idle_flip[int(self.enemy_idle_number[0]//2)],(self.enemy_rects[self.player_control_index[0]][0].x-self.camera_x_y[0],self.enemy_rects[self.player_control_index[0]][0].y-self.camera_x_y[1]))
        self.enemy_idle_number[0]+=0.07
        if self.enemy_idle_number[0]>len(self.enemy_idle)-1:
            self.enemy_idle_number[0]=0

    def mechanic_walk(self,key):
        self.distance_player=Control.distance(self)
        if any([self.level_1]) and self.player_control and self.player_control_cooldown[0]>0 and not key[pygame.K_e]:
            for idx,enemy in enumerate(self.enemy_rects):
                if key[pygame.K_d] and not key[pygame.K_a]:
                    SCREEN.blit(self.enemy_walk[int(self.enemy_run_number[0]//2)],(self.enemy_rects[self.player_control_index[0]][0].x-self.camera_x_y[0],self.enemy_rects[self.player_control_index[0]][0].y-self.camera_x_y[1]))
                    self.enemy_x_movement[0]=2  ; self.player_key.append("d")
                    if key[pygame.K_w]:
                        self.enemy_x_movement[0]=math.sqrt(2) ; self.enemy_y_movement[0]=-math.sqrt(2)
                    elif key[pygame.K_s]:
                        self.enemy_x_movement[0]=math.sqrt(2) ; self.enemy_y_movement[0]=math.sqrt(2)

                elif key[pygame.K_w] and not key[pygame.K_s] : 
                    self.enemy_y_movement[0]=-2
                    if self.player_key[-1]=="d": SCREEN.blit(self.enemy_walk[int(self.enemy_run_number[0]//2)],(self.enemy_rects[self.player_control_index[0]][0].x-self.camera_x_y[0],self.enemy_rects[self.player_control_index[0]][0].y-self.camera_x_y[1]))
                    else:  SCREEN.blit(self.enemy_walk_flip[int(self.enemy_run_number[0]//2)],(self.enemy_rects[self.player_control_index[0]][0].x-self.camera_x_y[0],self.enemy_rects[self.player_control_index[0]][0].y-self.camera_x_y[1]))

                elif key[pygame.K_a] and not key[pygame.K_d]:
                    SCREEN.blit(self.enemy_walk_flip[int(self.enemy_run_number[0]//2)],(self.enemy_rects[self.player_control_index[0]][0].x-self.camera_x_y[0],self.enemy_rects[self.player_control_index[0]][0].y-self.camera_x_y[1]))
                    self.enemy_x_movement[0]=-2  ; self.player_key.append("a")
                    if key[pygame.K_w]:
                        self.enemy_x_movement[0]=-math.sqrt(2); self.enemy_y_movement[0]=-math.sqrt(2)
                    elif key[pygame.K_s]:
                        self.enemy_x_movement[0]=-math.sqrt(2) ; self.enemy_y_movement[0]=math.sqrt(2)

                elif key[pygame.K_s] and not key[pygame.K_w]: 
                    self.enemy_y_movement[0]=2
                    if self.player_key[-1]=="d": SCREEN.blit(self.enemy_walk[int(self.enemy_run_number[0]//2)],(self.enemy_rects[self.player_control_index[0]][0].x-self.camera_x_y[0],self.enemy_rects[self.player_control_index[0]][0].y-self.camera_x_y[1]))
                    else:  SCREEN.blit(self.enemy_walk_flip[int(self.enemy_run_number[0]//2)],(self.enemy_rects[self.player_control_index[0]][0].x-self.camera_x_y[0],self.enemy_rects[self.player_control_index[0]][0].y-self.camera_x_y[1]))
                
                else: 
                    Control.mechanic_idle(self,key) ; self.enemy_x_movement[0]=0 ; self.enemy_y_movement[0]=0
        
                self.enemy_run_number[0]+=0.15
                if self.enemy_run_number[0]>len(self.enemy_walk)+1: self.enemy_run_number[0]=0
   
    def mechanic_attack(self,key):
        if any([self.level_1]) and self.player_control and self.player_control_cooldown[0]>0:
            if key[pygame.K_e]:
                self.enemy_x_movement[0]=0
                self.enemy_y_movement[0]=0
                if self.player_key[-1]=='d':
                   SCREEN.blit(self.enemy_attack[int(self.enemy_attack_number[0]//2)],(self.enemy_rects[self.player_control_index[0]][0].x-self.camera_x_y[0]-25,self.enemy_rects[self.player_control_index[0]][0].y-self.camera_x_y[1]-30))
                else:
                    SCREEN.blit(self.enemy_attack_flip[int(self.enemy_attack_number[0]//2)],(self.enemy_rects[self.player_control_index[0]][0].x-self.camera_x_y[0]-55,self.enemy_rects[self.player_control_index[0]][0].y-self.camera_x_y[1]-30))
                self.enemy_attack_number[0]+=0.15
                if self.enemy_attack_number[0]>len(self.enemy_attack)+1: self.enemy_attack_number[0]=0
               
    def mechanic_collision(self):
        if any([self.level_1]) and self.player_control and self.player_control_cooldown[0]>0:
            self.tile_hit=[]
            for tile in self.tile_set:
                for idx,enemy in enumerate(self.enemy_rects):
                    if self.enemy_rects[self.player_control_index[0]][0].colliderect(tile):
                        self.tile_hit.append(tile)
            return self.tile_hit

    def mechanic_collision_logic(self):
        if any([self.level_1]) and self.player_control and self.player_control_cooldown[0]>0:
            for idx,eenmy in enumerate(self.enemy_rects):
                self.enemy_rects[self.player_control_index[0]][0].x+=self.enemy_x_movement[0]
                self.collision=Control.mechanic_collision(self)
                for tile in self.collision:
                    if self.enemy_x_movement[0]>0:
                        self.enemy_rects[self.player_control_index[0]][0].right=tile.left
                    if self.enemy_x_movement[0]<0:
                        self.enemy_rects[self.player_control_index[0]][0].left=tile.right
                self.enemy_rects[self.player_control_index[0]][0].y+=self.enemy_y_movement[0]
                self.collision=Control.mechanic_collision(self)
                for tile in self.collision:
                    if self.enemy_y_movement[0]>0:
                        self.enemy_rects[self.player_control_index[0]][0].bottom=tile.top
                    if self.enemy_y_movement[0]<0:
                        self.enemy_rects[self.player_control_index[0]][0].top=tile.bottom


