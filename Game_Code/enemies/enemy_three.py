import pygame
import math

from Game_Asset_Code import * 
from .enemy_general_functions import EnemyGeneralFunctions
from Game_Code.control_test import ControlTest

class EnemyThree:
    def __init__(self,level_3,player_control) -> None:
        self.enemy_three_idle_number=enemy_three_idle_number ; self.enemy_three_move_number=enemy_three_move_number ; self.enemy_three_fall_number=enemy_three_fall_number ; self.enemy_three_attack_number=enemy_three_attack_number ; self.player_control_index=player_control_index
        self.level_3=level_3 ; self.enemy_3_health=enemy_3_health ; self.enemy_3_x_movement=enemy_3_x_movement ; self.enemy_3_y_movement=enemy_3_y_movement ; self.player_control_cooldown=player_control_cooldown
        self.player_control=player_control ; self.player_rect=player_rect ; self.camera_x_y=camera_x_y ; self.enemy_three_fall_type=enemy_three_fall_type ; self.player_health=player_health ; self.enemy_3_x_movement_control=enemy_3_x_movement_control
        self.enemy_3_y_movement_control=enemy_3_y_movement_control ; self.enemy_3_arrow_x_movement=enemy_3_arrow_x_movement ; self.enemy_3_arrow_y_movement=enemy_3_arrow_y_movement ; self.enemy_3_level_3_arrow_rect=enemy_3_level_3_arrow_rect
        self.enemy_three_arrow_list=enemy_three_arrow_list ; self.enemy_three_arrow_list_flip=enemy_three_arrow_list_flip ; self.enemy_three_arrow_number=enemy_three_arrow_number ; self.player_last_position=player_last_position ; self.player_health=player_health

        if self.level_3:
            self.tile_rect=level_3_tile_set_rect
            self.enemy_rect=enemy_3_level_3_rect
        
        if self.level_3:
            for idx,enemy in enumerate(self.enemy_rect):
                self.enemy_three_idle_number.append(0) ; self.enemy_three_move_number.append(0) ; self.enemy_three_fall_number.append(0) ; self.enemy_three_attack_number.append(0) ; self.enemy_3_health.append(100) ; self.enemy_3_x_movement.append(0) 
                self.enemy_3_y_movement.append(0) ; self.enemy_three_fall_type.append(0) ; self.enemy_3_arrow_x_movement.append(0) ; self.enemy_3_arrow_y_movement.append(0) ; self.enemy_three_arrow_number.append(0)
                if len(self.enemy_3_x_movement)>len(self.enemy_rect):
                    del self.enemy_three_idle_number[-1],self.enemy_3_health[1],self.enemy_3_x_movement[-1],self.enemy_3_y_movement[-1], self.enemy_three_move_number[-1], self.enemy_three_arrow_number[-1]
                    del self.enemy_three_fall_number[-1],self.enemy_three_attack_number[-1],self.enemy_three_fall_type[-1], self.enemy_3_arrow_x_movement[-1], self.enemy_3_arrow_y_movement[-1]

    def distance(self):
        if any([self.level_3]):
            self.distance=EnemyGeneralFunctions.distance(self,self.enemy_rect)
            return self.distance
        
    def iscontrolled(self):
        if any([self.level_3]) and self.player_control and self.player_control_cooldown[0]>0  and self.player_control_index[0][1]=="Enemy_1":
            return self.player_control_index[0][0]
    
    def enemy_index(self):
        if any([self.level_3]):
            for idx,range_attacker in enumerate(self.enemy_rect):
                  if idx==self.player_control_index[0][0] and self.player_control_index[0][1]=="Enemy_3":
                      return range_attacker

    def idle(self):
        self.enemy_three_idle_list=enemy_three_idle_list ; self.enemy_three_idle_list_flip=enemy_three_idle_list_flip
        if any([self.level_3]):
            self.distance=EnemyThree.distance(self)
            
            if EnemyThree.enemy_index(self) not in self.enemy_rect:
                self.enemy_3_rects_control=self.enemy_rect
                self.enemy_3_distance_control=self.distance

                EnemyGeneralFunctions.idle(self,self.distance,self.player_control_index,self.enemy_3_health,self.enemy_3_x_movement,self.enemy_3_y_movement,
                                            self.enemy_three_idle_list,self.enemy_three_idle_list_flip,self.enemy_three_idle_number,self.enemy_rect,0.75,11,40,50,700)
            
            if EnemyThree.enemy_index(self) in self.enemy_rect:
                self.enemy_3_rects_control=[i for i in self.enemy_rect if i!=EnemyThree.enemy_index(self)]
                self.enemy_3_distance_control=[i for idx, i in enumerate(self.distance) if idx!=self.player_control_index[0][0]]

                EnemyGeneralFunctions.idle_control(self,self.enemy_3_distance_control,self.player_control_index,self.enemy_3_health,self.enemy_3_x_movement,self.enemy_3_y_movement,
                                                        self.enemy_three_idle_list,self.enemy_three_idle_list_flip,self.enemy_three_idle_number,self.enemy_3_rects_control,0.75,11)
                                
    def move(self):
        self.enemy_three_move_list=enemy_three_move_list ; self.enemy_three_move_list_flip=enemy_three_move_list_flip
        if any([self.level_3]):
            self.distance=EnemyThree.distance(self)
            
            if EnemyThree.enemy_index(self) not in self.enemy_rect:
                self.enemy_3_rects_control=self.enemy_rect
                self.enemy_3_distance_control=self.distance

                EnemyGeneralFunctions.move(self,self.distance,self.player_control_index,self.enemy_3_health,self.enemy_rect,self.enemy_three_move_list,self.enemy_three_move_list_flip,
                                           self.enemy_three_move_number,self.enemy_3_x_movement,self.enemy_3_y_movement,0.75,9,40,50,40,50,400,700)

            if EnemyThree.enemy_index(self) in self.enemy_rect:
                self.enemy_3_rects_control=[i for i in self.enemy_rect if i!=EnemyThree.enemy_index(self)]
                self.enemy_3_distance_control=[i for idx, i in enumerate(self.distance) if idx!=self.player_control_index[0][0]]

                EnemyGeneralFunctions.move_control(self,self.enemy_3_distance_control,self.player_control_index,self.enemy_3_health,self.enemy_3_rects_control,self.enemy_three_move_list,self.enemy_three_move_list_flip,
                                                self.enemy_three_move_number,self.enemy_3_x_movement,self.enemy_3_y_movement,0.75,9)


    
    def arrow_distance(self):
        self.arrow_player_distance_list=[]
        for idx,arrow in enumerate(self.enemy_3_level_3_arrow_rect):
            
            self.player_last_position.append((self.player_rect.x,self.player_rect.y))

            self.arrow_player_distance=math.hypot(self.player_last_position[0][0]-arrow.x,self.player_last_position[0][1]-arrow.y)
            self.arrow_player_distance_list.append(self.arrow_player_distance)

         #   print(self.player_last_position)
        

            if len(self.player_last_position)>1:
                del self.player_last_position[-1]
            if self.arrow_player_distance_list[idx]<=50 or self.arrow_player_distance_list[idx]>400:
                self.player_last_position[0]=(self.player_rect.x,self.player_rect.y)

                

        return self.arrow_player_distance_list

    def arrow_angle(self):
        self.angle_list=[]
        for idx,arrow in enumerate(self.enemy_3_level_3_arrow_rect):
            self.dx,self.dy=self.player_last_position[0][0]-self.enemy_3_level_3_arrow_rect[idx].x, self.player_last_position[0][1]-self.enemy_3_level_3_arrow_rect[idx].y            
            self.angle=(math.degrees(math.atan2(-self.dy,self.dx))-180)/360
            self.angle_list.append(self.angle)
        return self.angle_list
    

    def arrow_movement(self,player_x,player_y,arrow_rect,arrow_x_movement,arrow_y_movement):
        slope_list=[]
        intercept_list=[]
        for idx,arrows in enumerate(arrow_rect):
            try: slope=(player_y-arrow_rect[idx].y)/(player_x-arrow_rect[idx].x)
            except ZeroDivisionError: slope=(player_y-arrow_rect[idx].y)
            slope_list.append(slope)
        for idx,slope in enumerate(slope_list):
            intercept=player_y-(slope*player_x)
            intercept_list.append(intercept)

         #   print(slope_list,player_y,arrow_rect[idx].y,player_x,arrow_rect[idx].x)

            if player_x>arrow_rect[idx].x:
                print("HERE")
                try: 
                    arrow_x_movement[idx]=((player_y-intercept_list[idx])/slope_list[idx])/100

                    if player_y>arrow_rect[idx].y:
                        arrow_y_movement[idx]=-((slope_list[idx]*player_x)-intercept_list[idx])/100
            
                    if player_y<=arrow_rect[idx].y:
                        arrow_y_movement[idx]=((slope_list[idx]*player_x)-intercept_list[idx])/100

                except ZeroDivisionError: 
                    arrow_x_movement[idx]=5
                    arrow_y_movement[idx]=0

                
       
            if player_x<=arrow_rect[idx].x:
                print("ELSE")
                try: 
                    arrow_x_movement[idx]=-((player_y-intercept_list[idx])/slope_list[idx])/100
               
                    if player_y>arrow_rect[idx].y:
                        arrow_y_movement[idx]=-((slope_list[idx]*player_x)-intercept_list[idx])/100
                    
                    if player_y<=arrow_rect[idx].y:
                        arrow_y_movement[idx]=((slope_list[idx]*player_x)-intercept_list[idx])/100
                
                except ZeroDivisionError: 
                    arrow_x_movement[idx]=-5
                    arrow_y_movement[idx]=0

            
            
           # if arrow_x_movement[idx]>0 and arrow_x_movement[idx]<10:
           #     arrow_x_movement[idx]=20
           # if arrow_x_movement[idx]>-10 and arrow_x_movement[idx]<0:
           #     arrow_x_movement[idx]=-20

          #  if arrow_y_movement[idx]>50:
          #      arrow_y_movement[idx]=arrow_y_movement[idx]//3*(1/50)
          #  if arrow_y_movement[idx]<-50:
          #      arrow_y_movement[idx]=arrow_y_movement[idx]//3*(1/50)


        #    print(arrow_y_movement)

        
    def arrow_logic(self):
        self.angle=EnemyThree.arrow_angle(self)
        for idx,enemy in enumerate(self.enemy_rect):
            
            pygame.draw.rect(SCREEN,(100,100,100),pygame.Rect(self.enemy_3_level_3_arrow_rect[idx].x-self.camera_x_y[0],self.enemy_3_level_3_arrow_rect[idx].y-self.camera_x_y[1],24,5),width=1)
          
            if self.player_last_position[0][0]>enemy.x:
                SCREEN.blit(self.enemy_three_arrow_list[0],(self.enemy_3_level_3_arrow_rect[idx].x-self.camera_x_y[0],self.enemy_3_level_3_arrow_rect[idx].y-self.camera_x_y[1]))    
            if self.player_last_position[0][0]<=enemy.x:
                SCREEN.blit(self.enemy_three_arrow_list_flip[0],(self.enemy_3_level_3_arrow_rect[idx].x-self.camera_x_y[0],self.enemy_3_level_3_arrow_rect[idx].y-self.camera_x_y[1]))

            
            EnemyThree.arrow_movement(self,self.player_last_position[0][0],self.player_last_position[0][1],self.enemy_rect,
                                      self.enemy_3_arrow_x_movement,self.enemy_3_arrow_y_movement)
            
           
#            print(self.player_last_position[0][0],self.player_last_position[0][1])

       #     print(self.enemy_3_level_3_arrow_rect)

         #   print(self.enemy_3_arrow_x_movement,self.enemy_3_arrow_y_movement)

            
            self.enemy_3_level_3_arrow_rect[idx].x+=self.enemy_3_arrow_x_movement[idx]*2
            self.enemy_3_level_3_arrow_rect[idx].y+=self.enemy_3_arrow_y_movement[idx]/4

    def arrow_total_logic(self):
        if any([self.level_3]):
            self.distance_list=EnemyThree.arrow_distance(self)
            self.angle=EnemyThree.arrow_angle(self)
            for idx,distance in enumerate(self.distance_list):
                if self.enemy_three_attack_number[idx]>7:
                    if self.distance_list[idx]>50 and self.distance_list[idx]<=400:
                        EnemyThree.arrow_logic(self)
                    if self.distance_list[idx]<=50 or self.distance_list[idx]>400:
                        self.enemy_three_attack_number[idx]=0
                      #  self.player_last_position[0]=(self.player_rect.x,self.player_rect.y)
                        self.enemy_3_level_3_arrow_rect[idx].x=self.enemy_rect[idx].x
                        self.enemy_3_level_3_arrow_rect[idx].y=self.enemy_rect[idx].y
                    if self.distance_list[idx]<=50:
                        print("HERE")
                        self.player_health[0]-=100

              #  print( self.enemy_3_level_3_arrow_rect)
                
    def attack(self):
        self.enemy_three_attack_list=enemy_three_attack_list ; self.enemy_three_attack_list_flip=enemy_three_attack_list_flip
        if any([self.level_3]):
            self.distance=EnemyThree.distance(self)

            if EnemyThree.enemy_index(self) not in self.enemy_rect:
                self.enemy_3_rects_control=self.enemy_rect
                self.enemy_3_distance_control=self.distance

                for idx,distance in enumerate(self.enemy_3_distance_control):
                    
                    if distance<400 and self.enemy_3_health[idx]>0:
                        
                        pygame.draw.rect(SCREEN,(100,100,100),pygame.Rect(self.enemy_rect[idx].x-self.camera_x_y[0],self.enemy_rect[idx].y-self.camera_x_y[1],45,55),width=1)
                        
                        self.enemy_3_x_movement[idx]=0 
                        self.enemy_3_y_movement[idx]=0
                        
                        if self.player_rect.x>=self.enemy_rect[idx].x:
                            SCREEN.blit(self.enemy_three_attack_list[int(self.enemy_three_attack_number[idx])//2],(self.enemy_rect[idx].x-self.camera_x_y[0]-50,self.enemy_rect[idx].y-self.camera_x_y[1]-50))
                            self.enemy_three_fall_type[idx]=1
                        else:
                            SCREEN.blit(self.enemy_three_attack_list_flip[int(self.enemy_three_attack_number[idx])//2],(self.enemy_rect[idx].x-self.camera_x_y[0]-50,self.enemy_rect[idx].y-self.camera_x_y[1]-50))
                            self.enemy_three_fall_type[idx]=2
                        
                        self.enemy_three_attack_number[idx]+=0.50
                        if self.enemy_three_attack_number[idx]>7:
                            self.enemy_three_attack_number[idx]=8

            if EnemyThree.enemy_index(self) in self.enemy_rect:
                self.enemy_3_rects_control=[i for i in self.enemy_rect if i!=EnemyThree.enemy_index(self)]
                self.enemy_3_distance_control=[i for idx, i in enumerate(self.distance) if idx!=self.player_control_index[0][0]]
                        
                EnemyGeneralFunctions.attack_control(self,self.enemy_3_distance_control,self.enemy_3_health,self.player_control_index,self.enemy_3_x_movement,self.enemy_3_y_movement,self.enemy_three_attack_list,
                                            self.enemy_three_attack_list_flip,self.enemy_three_attack_number,self.enemy_3_rects_control,self.enemy_three_fall_type,0.75,7,0,0,0,0,self.player_health,25)

    def fall(self):
        self.enemy_three_fall_list=enemy_three_fall_list ; self.enemy_three_fall_list_flip=enemy_three_fall_list_flip
        if any([self.level_3]):
            self.distance=EnemyThree.distance(self)
            EnemyGeneralFunctions.fall(self,self.enemy_rect,self.enemy_three_fall_type,self.enemy_three_fall_list,self.enemy_three_fall_list_flip,self.enemy_three_fall_number,
                                       self.enemy_3_health,0.50,11,0,0,self.enemy_3_x_movement,self.enemy_3_y_movement)

    def collision_with_object(self):
        if any([self.level_3]):
            if EnemyThree.enemy_index(self) not in self.enemy_rect:
                return EnemyGeneralFunctions.collision_with_object(self,self.tile_rect,self.enemy_rect)
            if not EnemyThree.enemy_index(self) not in self.enemy_rect:
                self.enemy_3_rects_control=[i for i in self.enemy_rect if i!=EnemyThree.enemy_index(self)]
                return EnemyGeneralFunctions.collision_with_object_control(self,self.tile_rect,self.enemy_3_rects_control)


    def collision_with_object_logic(self):
        if any([self.level_3]):
            if EnemyThree.enemy_index(self) not in self.enemy_rect:
                self.collision=EnemyThree.collision_with_object(self)
                EnemyGeneralFunctions.collision_with_object_logic(self,self.enemy_rect,self.enemy_3_x_movement,self.enemy_3_y_movement,self.collision)
            if EnemyThree.enemy_index(self) in self.enemy_rect:
                self.collision=EnemyThree.collision_with_object(self)
                self.enemy_3_rects_control=[i for i in self.enemy_rect if i!=EnemyThree.enemy_index(self)]
                EnemyGeneralFunctions.collision_with_object_logic_control(self,self.enemy_3_rects_control,self.enemy_3_x_movement_control,self.enemy_3_control_y_movement,self.collision)      
            

    def control_run(self,key):
        if any([self.level_3]) and self.player_control and self.player_control_cooldown[0]>0 and not key[pygame.K_e] and self.player_control_index[0][1]=="Enemy_3":
            if EnemyThree.enemy_index(self)  in self.enemy_rect:
                self.enemy_3_rects_control=[i for i in self.enemy_rect if i==EnemyThree.enemy_index(self)]
                ControlTest.mechanic_walk(self,key,self.enemy_three_move_list,self.enemy_3_rects_control[0],self.enemy_3_x_movement_control,self.enemy_3_y_movement_control,
                        self.enemy_three_move_list_flip,self.enemy_three_move_number,self.enemy_three_idle_list,self.enemy_three_idle_number,self.enemy_three_idle_list_flip)

    def control_attack(self,key):
        if any([self.level_3]) and self.player_control and self.player_control_cooldown[0]>0  and self.player_control_index[0][1]=="Enemy_3":
            if EnemyThree.enemy_index(self) in self.enemy_rect:
                self.enemy_3_rects_control=[i for i in self.enemy_rect if i==EnemyThree.enemy_index(self)]
                ControlTest.mechanic_attack(self,key,self.enemy_three_attack_list,self.enemy_3_rects_control[0],self.enemy_three_attack_list_flip,
                                        self.enemy_three_attack_number,self.enemy_3_x_movement_control,self.enemy_3_y_movement_control)

    def control_collision(self):
        if any([self.level_3]) and self.player_control and self.player_control_cooldown[0]>0  and self.player_control_index[0][1]=="Enemy_3":
            if EnemyThree.enemy_index(self) in self.enemy_rect:
                self.enemy_3_rects_control=[i for i in self.enemy_rect if i==EnemyThree.enemy_index(self)]
                ControlTest.mechanic_collision(self,self.tile_rect,self.enemy_3_rects_control[0])

    def control_collision_object_logic(self):
        if any([self.level_3]) and self.player_control and self.player_control_cooldown[0]>0  and self.player_control_index[0][1]=="Enemy_3":
            if EnemyThree.enemy_index(self)  in self.enemy_rect:
                self.enemy_3_rects_control=[i for i in self.enemy_1_rects if i==EnemyThree.enemy_index(self)]
                ControlTest.mechanic_collision_logic(self,self.tile_rect,self.enemy_3_rects_control[0],self.enemy_3_x_movement_control,self.enemy_3_y_movement_control,)       