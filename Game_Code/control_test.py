import pygame
import math


from Game_Asset_Code import *

class ControlTest:
    def __init__(self) -> None:
        self.player_rect=player_rect
        self.camera_x_y=camera_x_y
        self.player_control_index=player_control_index
        self.player_key=player_key

 #   def enemy_camera(self,enemy_rects):
  #      for idx,enemy in enumerate(enemy_rects):
  #          if self.player_control_index[0][0]==idx:
  #              return enemy_rects[idx]
            
    def mechanic_idle(self,enemy_idle,enemy_idle_number,enemy_rects,enemy_idle_flip):
        enemy_x_movement[0]=0
        enemy_y_movement[0]=0
        if self.player_key[-1]=='d':
            SCREEN.blit(enemy_idle[int(enemy_idle_number[0]//2)],(enemy_rects.x-self.camera_x_y[0],enemy_rects.y-self.camera_x_y[1]))
        else:
            SCREEN.blit(enemy_idle_flip[int(enemy_idle_number[0]//2)],(enemy_rects.x-self.camera_x_y[0],enemy_rects.y-self.camera_x_y[1]))
        enemy_idle_number[0]+=0.07
        if enemy_idle_number[0]>len(enemy_idle)-1:
            enemy_idle_number[0]=0
    
    def mechanic_walk(self,key,enemy_walk,enemy_rects,enemy_x_movement,enemy_y_movement,enemy_walk_flip,enemy_run_number,enemy_idle,enemy_idle_number,enemy_idle_flip):
      #  for idx,enemy in enumerate(enemy_rects):
            if key[pygame.K_d] and not key[pygame.K_a]:
                SCREEN.blit(enemy_walk[int(enemy_run_number[0]//2)],(enemy_rects.x-self.camera_x_y[0],enemy_rects.y-self.camera_x_y[1]))
                enemy_x_movement[0]=2  ; self.player_key.append("d")
                if key[pygame.K_w]:
                    enemy_x_movement[0]=math.sqrt(2) 
                    enemy_y_movement[0]=-math.sqrt(2)
                elif key[pygame.K_s]:
                    enemy_x_movement[0]=math.sqrt(2) 
                    enemy_y_movement[0]=math.sqrt(2)

            elif key[pygame.K_w] and not key[pygame.K_s] : 
                enemy_y_movement[0]=-2
                if self.player_key[-1]=="d": SCREEN.blit(enemy_walk[int(enemy_run_number[0]//2)],(enemy_rects.x-self.camera_x_y[0],enemy_rects.y-self.camera_x_y[1]))
                else:  SCREEN.blit(enemy_walk_flip[int(enemy_run_number[0]//2)],(enemy_rects.x-self.camera_x_y[0],enemy_rects.y-self.camera_x_y[1]))

            elif key[pygame.K_a] and not key[pygame.K_d]:
                SCREEN.blit(enemy_walk_flip[int(enemy_run_number[0]//2)],(enemy_rects.x-self.camera_x_y[0],enemy_rects.y-self.camera_x_y[1]))
                enemy_x_movement[0]=-2  ; player_key.append("a")
                if key[pygame.K_w]:
                    enemy_x_movement[0]=-math.sqrt(2); enemy_y_movement[0]=-math.sqrt(2)
                elif key[pygame.K_s]:
                    enemy_x_movement[0]=-math.sqrt(2) ; enemy_y_movement[0]=math.sqrt(2)

            elif key[pygame.K_s] and not key[pygame.K_w]: 
                enemy_y_movement[0]=2
                if self.player_key[-1]=="d": SCREEN.blit(enemy_walk[int(enemy_run_number[0]//2)],(enemy_rects.x-self.camera_x_y[0],enemy_rects.y-self.camera_x_y[1]))
                else:  SCREEN.blit(enemy_walk_flip[int(enemy_run_number[0]//2)],(enemy_rects.x-self.camera_x_y[0],enemy_rects.y-self.camera_x_y[1]))
            
            else: 
                ControlTest.mechanic_idle(self,enemy_idle,enemy_idle_number,enemy_rects,enemy_idle_flip) ; enemy_x_movement[0]=0 ; enemy_y_movement[0]=0
    
            enemy_run_number[0]+=0.15
            if enemy_run_number[0]>len(enemy_walk): enemy_run_number[0]=0
   
    def mechanic_attack(self,key,enemy_attack,enemy_rects,enemy_attack_flip,enemy_attack_number,enemy_x_movement,enemy_y_movement):
        if any([self.level_1]) and self.player_control and self.player_control_cooldown[0]>0:
            if key[pygame.K_e]:
                enemy_x_movement[0]=0
                enemy_y_movement[0]=0
                if self.player_key[-1]=='d':
                   SCREEN.blit(enemy_attack[int(enemy_attack_number[0]//2)],(enemy_rects.x-self.camera_x_y[0]-25,enemy_rects.y-self.camera_x_y[1]-30))
                else:
                    SCREEN.blit(enemy_attack_flip[int(enemy_attack_number[0]//2)],(enemy_rects.x-self.camera_x_y[0]-55,enemy_rects.y-self.camera_x_y[1]-30))
                enemy_attack_number[0]+=0.15
                if enemy_attack_number[0]>len(enemy_attack)+1: enemy_attack_number[0]=0

    def mechanic_collision(self,tile_set,enemy_rects):
        if any([self.level_1]) and self.player_control and self.player_control_cooldown[0]>0:
            self.tile_hit=[]
            for tile in tile_set:
                for idx,enemy in enumerate(enemy_rects):
                    if enemy_rects.colliderect(tile):
                        self.tile_hit.append(tile)
            return self.tile_hit

    def mechanic_collision_logic(self,tile_set,enemy_rects,enemy_x_movement,enemy_y_movement):
        if any([self.level_1]) and self.player_control and self.player_control_cooldown[0]>0:
           for idx,enemy in enumerate(enemy_rects):
                enemy_rects.x+=enemy_x_movement[0]
                self.collision=ControlTest.mechanic_collision(self,tile_set,enemy_rects)
                for tile in self.collision:
                    if enemy_x_movement[0]>0:
                        enemy_rects.right=tile.left
                    if self.enemy_x_movement[0]<0:
                        enemy_rects.left=tile.right
                enemy_rects.y+=enemy_y_movement[0]
                self.collision=ControlTest.mechanic_collision(self,tile_set,enemy_rects)
                for tile in self.collision:
                    if enemy_y_movement[0]>0:
                        enemy_rects.bottom=tile.top
                    if enemy_y_movement[0]<0:
                        enemy_rects.top=tile.bottom
        



