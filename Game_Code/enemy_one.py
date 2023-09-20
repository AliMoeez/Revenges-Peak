import pygame
import math

from Game_Asset_Code import *

class EnemyOne:
    def __init__(self,level_1,enemy_1_level_1_rect):
        self.level_1=level_1 ; self.camera_x_y=camera_x_y ; self.enemy_1_level_1_rect=enemy_1_level_1_rect ; self.skeleton_idle_number=skeleton_idle_number
        self.skeleton_run_number=skeleton_run_number ; self.skeleton_attack_number=skeleton_attack_number ; self.player_rect=player_rect
        self.enemy_1_x_movement=enemy_1_x_movement ; self.enemy_1_y_movement=enemy_1_y_movement ; self.player_control_index=player_control_index
        if level_1:
            self.enemy_1_rects=enemy_1_level_1_rect
            for idx,skeleton in enumerate(self.enemy_1_rects):
                self.skeleton_idle_number.append(0) ; self.skeleton_run_number.append(0) ; self.skeleton_attack_number.append(0)
                self.enemy_1_x_movement.append(0) ; self.enemy_1_y_movement.append(0)

    def distance(self):
        if any([self.level_1]):
            self.player_enemy_1_distance=[]
            for idx,skeleton in enumerate(self.enemy_1_rects):
                self.player_enemy_1_distance.append(math.hypot(self.player_rect.x-self.enemy_1_rects[idx].x,self.player_rect.y-self.enemy_1_rects[idx].y))
            return self.player_enemy_1_distance

    def idle(self):
        self.enemy_1_distance=EnemyOne.distance(self)
        self.skeleton_idle=skeleton_idle; self.skeleton_idle_flip=skeleton_idle_flip
        if any([self.level_1]):
            for idx,distance in enumerate(self.enemy_1_distance):
                if distance>200 and not self.player_control_index[0]==idx:
                    self.enemy_1_x_movement[idx]=0
                    self.enemy_1_y_movement[idx]=0
                    SCREEN.blit(self.skeleton_idle[int(self.skeleton_idle_number[idx]//2)],(self.enemy_1_rects[idx].x-self.camera_x_y[0],self.enemy_1_rects[idx].y-self.camera_x_y[1]))
                    pygame.draw.rect(SCREEN,(100,200,200),pygame.Rect(self.enemy_1_rects[idx].x-self.camera_x_y[0]+20,self.enemy_1_rects[idx].y-self.camera_x_y[1]+12,40,70),width=1)
                    self.skeleton_idle_number[idx]+=0.10
                    if self.skeleton_idle_number[idx]>4: self.skeleton_idle_number[idx]=0

    def run(self):
        self.enemy_1_distance=EnemyOne.distance(self)
        self.skeleton_run=skeleton_run; self.skeleton_run_flip=skeleton_run_flip
        if any([self.level_1]):
            for idx,distance in enumerate(self.enemy_1_distance):
                if distance>=100 and distance<=200 and not self.player_control_index[0]==idx:
                    if self.player_rect.x>=self.enemy_1_rects[idx].x:
                        SCREEN.blit(self.skeleton_run[int(self.skeleton_run_number[idx]//2)],(self.enemy_1_rects[idx].x-self.camera_x_y[0],self.enemy_1_rects[idx].y-self.camera_x_y[1]))
                    else:
                        SCREEN.blit(self.skeleton_run_flip[int(self.skeleton_run_number[idx]//2)],(self.enemy_1_rects[idx].x-self.camera_x_y[0],self.enemy_1_rects[idx].y-self.camera_x_y[1]))
                    pygame.draw.rect(SCREEN,(100,200,200),pygame.Rect(self.enemy_1_rects[idx].x-self.camera_x_y[0]+20,self.enemy_1_rects[idx].y-self.camera_x_y[1]+12,40,70),width=1)
                    self.skeleton_run_number[idx]+=0.10
                    if self.skeleton_run_number[idx]>7: self.skeleton_run_number[idx]=0

                    if self.player_rect.x>=self.enemy_1_rects[idx].x:
                        self.enemy_1_x_movement[idx]=1
                        if self.player_rect.y<self.enemy_1_rects[idx].y: self.enemy_1_y_movement[idx]=-1
                        if self.player_rect.y>=self.enemy_1_rects[idx].y: self.enemy_1_y_movement[idx]=1
                    
                    if self.player_rect.x<=self.enemy_1_rects[idx].x:
                        self.enemy_1_x_movement[idx]=-1
                        if self.player_rect.y<self.enemy_1_rects[idx].y: self.enemy_1_y_movement[idx]=-1
                        if self.player_rect.y>=self.enemy_1_rects[idx].y: self.enemy_1_y_movement[idx]=1

    def attack(self):
        self.enemy_1_distance=EnemyOne.distance(self)
        self.skeleton_attack=skeleton_attack; self.skeleton_attack_flip=skeleton_attack_flip
        if any([self.level_1]):
            for idx,distance in enumerate(self.enemy_1_distance):
                if distance<100 and not self.player_control_index[0]==idx:
                    self.enemy_1_x_movement[idx]=0
                    self.enemy_1_y_movement[idx]=0
                    if self.player_rect.x>=self.enemy_1_rects[idx].x:
                        SCREEN.blit(self.skeleton_attack[int(self.skeleton_attack_number[idx]//2)],(self.enemy_1_rects[idx].x-self.camera_x_y[0]-25,self.enemy_1_rects[idx].y-self.camera_x_y[1]-30))
                    else:
                        SCREEN.blit(self.skeleton_attack_flip[int(self.skeleton_attack_number[idx]//2)],(self.enemy_1_rects[idx].x-self.camera_x_y[0]-55,self.enemy_1_rects[idx].y-self.camera_x_y[1]-30))
                    pygame.draw.rect(SCREEN,(100,200,200),pygame.Rect(self.enemy_1_rects[idx].x-self.camera_x_y[0]+20,self.enemy_1_rects[idx].y-self.camera_x_y[1]+12,40,70),width=1)
                    self.skeleton_attack_number[idx]+=0.10
                    if self.skeleton_attack_number[idx]>7: self.skeleton_attack_number[idx]=0

    def collision(self):
        if any([self.level_1]):
            for idx,skeleton in enumerate(self.enemy_1_rects):
                self.enemy_1_rects[idx].x+=self.enemy_1_x_movement[idx]
                self.enemy_1_rects[idx].y+=self.enemy_1_y_movement[idx]

        