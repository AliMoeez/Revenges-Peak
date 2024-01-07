import pygame
from .general_assets import *


pygame.init()

skeleton_1_idle_1=pygame.image.load(r"Assets\Enemies\Skeleton Enemy\Skeleton Assets\ready_1.png").convert_alpha()
skeleton_1_idle_2=pygame.image.load(r"Assets\Enemies\Skeleton Enemy\Skeleton Assets\ready_2.png").convert_alpha() 
skeleton_1_idle_3=pygame.image.load(r"Assets\Enemies\Skeleton Enemy\Skeleton Assets\ready_3.png").convert_alpha()
skeleton_idle=[skeleton_1_idle_1,skeleton_1_idle_2,skeleton_1_idle_3] ; skeleton_idle_flip=[] ; skeleton_idle_number=[]
for i,skeleton in enumerate(skeleton_idle): skeleton_idle[i]=pygame.transform.scale(skeleton_idle[i],(50*1.8,48*1.8))
for i,skeleton in enumerate(skeleton_idle[:]): skeleton_idle_flip.append(pygame.transform.flip(skeleton_idle[i],True,False))

skeleton_1_run_1=pygame.image.load(r"Assets\Enemies\Skeleton Enemy\Skeleton Assets\run_1.png").convert_alpha() 
skeleton_1_run_2=pygame.image.load(r"Assets\Enemies\Skeleton Enemy\Skeleton Assets\run_2.png").convert_alpha() 
skeleton_1_run_3=pygame.image.load(r"Assets\Enemies\Skeleton Enemy\Skeleton Assets\run_3.png").convert_alpha()
skeleton_1_run_4=pygame.image.load(r"Assets\Enemies\Skeleton Enemy\Skeleton Assets\run_4.png").convert_alpha() 
skeleton_1_run_5=pygame.image.load(r"Assets\Enemies\Skeleton Enemy\Skeleton Assets\run_5.png").convert_alpha() 
skeleton_1_run_6=pygame.image.load(r"Assets\Enemies\Skeleton Enemy\Skeleton Assets\run_6.png").convert_alpha()
skeleton_run=[skeleton_1_run_1,skeleton_1_run_2,skeleton_1_run_3,skeleton_1_run_4,skeleton_1_run_5,skeleton_1_run_6] ; skeleton_run_flip=[] ; skeleton_run_number=[]
for i,skeleton in enumerate(skeleton_run): skeleton_run[i]=pygame.transform.scale(skeleton_run[i],(50*1.8,48*1.8))
for i,skeleton in enumerate(skeleton_run[:]): skeleton_run_flip.append(pygame.transform.flip(skeleton_run[i],True,False))

skeleton_1_attack_1=pygame.image.load(r"Assets\Enemies\Skeleton Enemy\Skeleton Assets\attack1_1.png").convert_alpha() 
skeleton_1_attack_2=pygame.image.load(r"Assets\Enemies\Skeleton Enemy\Skeleton Assets\attack1_2.png").convert_alpha() 
skeleton_1_attack_3=pygame.image.load(r"Assets\Enemies\Skeleton Enemy\Skeleton Assets\attack1_3.png").convert_alpha()
skeleton_1_attack_4=pygame.image.load(r"Assets\Enemies\Skeleton Enemy\Skeleton Assets\attack1_4.png").convert_alpha() 
skeleton_1_attack_5=pygame.image.load(r"Assets\Enemies\Skeleton Enemy\Skeleton Assets\attack1_5.png").convert_alpha() 
skeleton_1_attack_6=pygame.image.load(r"Assets\Enemies\Skeleton Enemy\Skeleton Assets\attack1_6.png").convert_alpha()
skeleton_attack=[skeleton_1_attack_1,skeleton_1_attack_2,skeleton_1_attack_3,skeleton_1_attack_4,skeleton_1_attack_5,skeleton_1_attack_6] ; skeleton_attack_flip=[] ; skeleton_attack_number=[]
for i,skeleton in enumerate(skeleton_attack): skeleton_attack[i]=pygame.transform.scale(skeleton_attack[i],(100*1.8,65*1.8))
for i,skeleton in enumerate(skeleton_attack[:]): skeleton_attack_flip.append(pygame.transform.flip(skeleton_attack[i],True,False))

skeleton_1_fall_1=pygame.image.load(r"Assets\Enemies\Skeleton Enemy\Skeleton Assets\dead_far_1.png").convert_alpha() 
skeleton_1_fall_2=pygame.image.load(r"Assets\Enemies\Skeleton Enemy\Skeleton Assets\dead_far_2.png").convert_alpha() 
skeleton_1_fall_3=pygame.image.load(r"Assets\Enemies\Skeleton Enemy\Skeleton Assets\dead_far_3.png").convert_alpha()
skeleton_1_fall_4=pygame.image.load(r"Assets\Enemies\Skeleton Enemy\Skeleton Assets\dead_far_4.png").convert_alpha() 
skeleton_1_fall_5=pygame.image.load(r"Assets\Enemies\Skeleton Enemy\Skeleton Assets\dead_far_5.png").convert_alpha() 
skeleton_1_fall_6=pygame.image.load(r"Assets\Enemies\Skeleton Enemy\Skeleton Assets\dead_far_6.png").convert_alpha()
skeleton_fall=[skeleton_1_fall_1,skeleton_1_fall_2,skeleton_1_fall_3,skeleton_1_fall_4,skeleton_1_fall_5,skeleton_1_fall_6] ; skeleton_fall_flip=[] ; skeleton_fall_number=[]
for i,skeleton in enumerate(skeleton_fall): skeleton_fall[i]=pygame.transform.scale(skeleton_fall[i],(75*1.8,40*1.8))
for i,skeleton in enumerate(skeleton_fall[:]): skeleton_fall_flip.append(pygame.transform.flip(skeleton_fall[i],True,False))

enemy_1_level_1_x=[457,428,3500,3650,3950,4050,4070,4300,4450] ; enemy_1_level_1_y=[519,484,1700,1715,1880,1895,1800,705,755] #400,200  800,200

enemy_1_level_2_x=[1900,1920,1970,1990] ; enemy_1_level_2_y=[1550,1590,1570,1590,1592]

enemy_1_level_3_x=[3853,3964,4743,3454,3364] ; enemy_1_level_3_y=[725,983,1046,1043,13404]

enemy_1_level_4_x=[770,890,912] ; enemy_1_level_4_y=[300,195,315]

enemy_1_x_movement=[] ; enemy_1_y_movement=[]

enemy_1_level_1_rect=[] ; enemy_1_level_2_rect=[] ; enemy_1_level_3_rect=[] ; enemy_1_level_4_rect=[]

enemy_1_health=[] ; enemy_1_fall_type=[]

enemy_1_x_control_movement=[0] ; enemy_1_y_control_movement=[0]

for i,num in enumerate(enemy_1_level_1_x): enemy_1_level_1_rect.append(pygame.Rect(enemy_1_level_1_x[i],enemy_1_level_1_y[i],40,70))
for i,num in enumerate(enemy_1_level_2_x): enemy_1_level_2_rect.append(pygame.Rect(enemy_1_level_2_x[i],enemy_1_level_2_y[i],40,70))
for i,num in enumerate(enemy_1_level_3_x): enemy_1_level_3_rect.append(pygame.Rect(enemy_1_level_3_x[i],enemy_1_level_3_y[i],40,70))
for i,num in enumerate(enemy_1_level_4_x): enemy_1_level_4_rect.append(pygame.Rect(enemy_1_level_4_x[i],enemy_1_level_4_y[i],40,70))

brute_1_icon=pygame.image.load(r"Assets\Enemies\Brute_Enemy\Brute_Assets\imp_red\icon.png")
brute_1_icon=pygame.transform.scale(brute_1_icon,(150,100))

brute_1_idle_1=pygame.image.load(r"Assets\Enemies\Brute_Enemy\Brute_Assets\imp_red\ready_1.png").convert_alpha() 
brute_1_idle_2=pygame.image.load(r"Assets\Enemies\Brute_Enemy\Brute_Assets\imp_red\ready_2.png").convert_alpha() 
brute_1_idle_3=pygame.image.load(r"Assets\Enemies\Brute_Enemy\Brute_Assets\imp_red\ready_3.png").convert_alpha()
brute_1_idle_4=pygame.image.load(r"Assets\Enemies\Brute_Enemy\Brute_Assets\imp_red\ready_4.png").convert_alpha() 
brute_1_idle_5=pygame.image.load(r"Assets\Enemies\Brute_Enemy\Brute_Assets\imp_red\ready_5.png").convert_alpha() 
brute_1_idle_6=pygame.image.load(r"Assets\Enemies\Brute_Enemy\Brute_Assets\imp_red\ready_6.png").convert_alpha()
brute_1_idle=[brute_1_idle_1,brute_1_idle_2,brute_1_idle_3,brute_1_idle_4,brute_1_idle_5,brute_1_idle_6]
brute_1_idle_flip=[] ; brute_1_idle_number=[]
for i,brute in enumerate(brute_1_idle): brute_1_idle[i]=pygame.transform.scale(brute_1_idle[i],(50*1.8,48*1.8))
for i,brtue in enumerate(brute_1_idle[:]): brute_1_idle_flip.append(pygame.transform.flip(brute_1_idle[i],True,False))

brute_1_run_1=pygame.image.load(r"Assets\Enemies\Brute_Enemy\Brute_Assets\imp_red\run_1.png").convert_alpha() 
brute_1_run_2=pygame.image.load(r"Assets\Enemies\Brute_Enemy\Brute_Assets\imp_red\run_2.png").convert_alpha() 
brute_1_run_3=pygame.image.load(r"Assets\Enemies\Brute_Enemy\Brute_Assets\imp_red\run_3.png").convert_alpha()
brute_1_run_4=pygame.image.load(r"Assets\Enemies\Brute_Enemy\Brute_Assets\imp_red\run_4.png").convert_alpha() 
brute_1_run_5=pygame.image.load(r"Assets\Enemies\Brute_Enemy\Brute_Assets\imp_red\run_5.png").convert_alpha() 
brute_1_run_6=pygame.image.load(r"Assets\Enemies\Brute_Enemy\Brute_Assets\imp_red\run_6.png").convert_alpha()
brute_1_run=[brute_1_run_1,brute_1_run_2,brute_1_run_3,brute_1_run_4,brute_1_run_5,brute_1_run_6]
brute_1_run_flip=[] ; brute_1_run_number=[]
for i,brute in enumerate(brute_1_run): brute_1_run[i]=pygame.transform.scale(brute_1_run[i],(50*1.8,48*1.8))
for i,brtue in enumerate(brute_1_run[:]): brute_1_run_flip.append(pygame.transform.flip(brute_1_run[i],True,False))

brute_1_attack_1_1=pygame.image.load(r"Assets\Enemies\Brute_Enemy\Brute_Assets\imp_red\attack1_1.png").convert_alpha() 
brute_1_attack_1_2=pygame.image.load(r"Assets\Enemies\Brute_Enemy\Brute_Assets\imp_red\attack1_2.png").convert_alpha() 
brute_1_attack_1_3=pygame.image.load(r"Assets\Enemies\Brute_Enemy\Brute_Assets\imp_red\attack1_3.png").convert_alpha()
brute_1_attack_1_4=pygame.image.load(r"Assets\Enemies\Brute_Enemy\Brute_Assets\imp_red\attack1_4.png").convert_alpha() 
brute_1_attack_1_5=pygame.image.load(r"Assets\Enemies\Brute_Enemy\Brute_Assets\imp_red\attack1_5.png").convert_alpha() 
brute_1_attack_1_6=pygame.image.load(r"Assets\Enemies\Brute_Enemy\Brute_Assets\imp_red\attack1_6.png").convert_alpha()
brute_1_attack_1=[brute_1_attack_1_1,brute_1_attack_1_2,brute_1_attack_1_3,brute_1_attack_1_4,brute_1_attack_1_5,brute_1_attack_1_6]
brute_1_attack_flip_1=[] ; brute_1_attack_number=[0]
for i,brute in enumerate(brute_1_attack_1): brute_1_attack_1[i]=pygame.transform.scale(brute_1_attack_1[i],(100*1.8,65*1.8))
for i,brute in enumerate(brute_1_attack_1[:]) : brute_1_attack_flip_1.append(pygame.transform.flip(brute_1_attack_1[i],True,False))

brute_1_fall_1_1=pygame.image.load(r"Assets\Enemies\Brute_Enemy\Brute_Assets\imp_red\fall_back_1.png").convert_alpha() 
brute_1_fall_1_2=pygame.image.load(r"Assets\Enemies\Brute_Enemy\Brute_Assets\imp_red\fall_back_2.png").convert_alpha()  
brute_1_fall_1_3=pygame.image.load(r"Assets\Enemies\Brute_Enemy\Brute_Assets\imp_red\fall_back_3.png").convert_alpha()
brute_1_fall_1_4=pygame.image.load(r"Assets\Enemies\Brute_Enemy\Brute_Assets\imp_red\fall_back_4.png").convert_alpha()
brute_1_fall_1_5=pygame.image.load(r"Assets\Enemies\Brute_Enemy\Brute_Assets\imp_red\fall_back_5.png").convert_alpha() 
brute_1_fall_1=[brute_1_fall_1_1,brute_1_fall_1_2,brute_1_fall_1_3,brute_1_fall_1_4,brute_1_fall_1_5]
brute_1_fall_flip_1=[] ; brute_1_fall_number=[]
for i,brute in enumerate(brute_1_fall_1): brute_1_fall_1[i]=pygame.transform.scale(brute_1_fall_1[i],(59*1.8,35*1.8))
for i,brute in enumerate(brute_1_fall_1[:]) : brute_1_fall_flip_1.append(pygame.transform.flip(brute_1_fall_1[i],True,False))

enemy_2_level_1_x=[377,353,3525,3950,4370] ; enemy_2_level_1_y=[450,525,1775,1950,754]  #600,200

enemy_2_level_2_x=[1700,1800,1827,1900] ; enemy_2_level_2_y=[1500,1550,1570,1580] #1700,1500

enemy_2_level_3_x=[3830,3763,3773,3604,3833] ; enemy_2_level_3_y=[725,520,1276,1073,1326] #1700,1500

enemy_2_level_4_x=[817,947,992] ; enemy_2_level_4_y=[112,217,354]

enemy_2_x_movement=[] ; enemy_2_y_movement=[]

enemy_2_rects=[] ; enemy_2_fall_type=[]  ; enemy_2_health=[] ; enemy_2_level_2_rects=[] ; enemy_2_level_3_rects=[] ; enemy_2_level_4_rects=[]

enemy_run_number=[0] ; enemy_idle_number=[0] ; enemy_attack_number=[0] ; enemy_x_movement=[0] ; enemy_y_movement=[0]

enemy_2_x_control_movement=[0] ; enemy_2_y_control_movement=[0]

for i,y in enumerate(enemy_2_level_1_x): enemy_2_rects.append(pygame.Rect(enemy_2_level_1_x[i],enemy_2_level_1_y[i],40,70))
for i,y in enumerate(enemy_2_level_2_x): enemy_2_level_2_rects.append(pygame.Rect(enemy_2_level_2_x[i],enemy_2_level_2_y[i],40,70))
for i,y in enumerate(enemy_2_level_3_x): enemy_2_level_3_rects.append(pygame.Rect(enemy_2_level_3_x[i],enemy_2_level_3_y[i],40,70))
for i,y in enumerate(enemy_2_level_4_x): enemy_2_level_4_rects.append(pygame.Rect(enemy_2_level_4_x[i],enemy_2_level_4_y[i],40,70))

enemy_three_idle_image=pygame.image.load(r"Assets\Enemies\Arrow Enemy\Sprites\Character\Idle.png")
enemy_three_move_image=pygame.image.load(r"Assets\Enemies\Arrow Enemy\Sprites\Character\Run.png")
enemy_three_attack_image=pygame.image.load(r"Assets\Enemies\Arrow Enemy\Sprites\Character\Attack.png")
enemy_three_fall_image=pygame.image.load(r"Assets\Enemies\Arrow Enemy\Sprites\Character\Death.png")
enemy_three_arrow_image=pygame.image.load(r"Assets\Enemies\Arrow Enemy\Sprites\Arrow\Move.png")

def enemy_three_idle(images,frame,width,height): 
    image=pygame.Surface((width,height),pygame.SRCALPHA) ; image.blit(images,(0,0),((frame*width),0,width,height)) ; image=pygame.transform.scale(image,(width*1.50,height*1.50))
    return image

idle_1=enemy_three_idle(enemy_three_idle_image,0,100,100)  ; idle_2=enemy_three_idle(enemy_three_idle_image,1,100,100)  ; idle_3=enemy_three_idle(enemy_three_idle_image,2,100,100)  ; idle_4=enemy_three_idle(enemy_three_idle_image,3,100,100)  
idle_5=enemy_three_idle(enemy_three_idle_image,4,100,100)  ; idle_6=enemy_three_idle(enemy_three_idle_image,5,100,100) ; idle_7=enemy_three_idle(enemy_three_idle_image,6,100,100)  ; idle_8=enemy_three_idle(enemy_three_idle_image,7,100,100) 
idle_9=enemy_three_idle(enemy_three_idle_image,8,100,100)  ; idle_10=enemy_three_idle(enemy_three_idle_image,9,100,100) 

def enemy_three_move(images,frame,width,height): 
    image=pygame.Surface((width,height),pygame.SRCALPHA) ; image.blit(images,(0,0),((frame*width),0,width,height)) ; image=pygame.transform.scale(image,(width*1.50,height*1.50))
    return image

move_1=enemy_three_move(enemy_three_move_image,0,100,100)  ; move_2=enemy_three_move(enemy_three_move_image,1,100,100)  ; move_3=enemy_three_move(enemy_three_move_image,2,100,100)  ; move_4=enemy_three_move(enemy_three_move_image,3,100,100)  
move_5=enemy_three_move(enemy_three_move_image,4,100,100)  ; move_6=enemy_three_move(enemy_three_move_image,5,100,100) ; move_7=enemy_three_move(enemy_three_move_image,6,100,100)  ; move_8=enemy_three_move(enemy_three_move_image,7,100,100) 


def enemy_three_fall(images,frame,width,height): 
    image=pygame.Surface((width,height),pygame.SRCALPHA) ; image.blit(images,(0,0),((frame*width),0,width,height)) ; image=pygame.transform.scale(image,(width*1.50,height*1.50))
    return image

fall_1=enemy_three_fall(enemy_three_fall_image,0,100,100)  ; fall_2=enemy_three_fall(enemy_three_fall_image,1,100,100)  ; fall_3=enemy_three_fall(enemy_three_fall_image,2,100,100)  ; fall_4=enemy_three_fall(enemy_three_fall_image,3,100,100)  
fall_5=enemy_three_fall(enemy_three_fall_image,4,100,100)  ; fall_6=enemy_three_fall(enemy_three_fall_image,5,100,100) ; fall_7=enemy_three_fall(enemy_three_fall_image,6,100,100)  ; fall_8=enemy_three_fall(enemy_three_fall_image,7,100,100) 
fall_9=enemy_three_fall(enemy_three_fall_image,8,100,100)  ; fall_10=enemy_three_fall(enemy_three_fall_image,9,100,100) 


def enemy_three_attack(images,frame,width,height): 
    image=pygame.Surface((width,height),pygame.SRCALPHA) ; image.blit(images,(0,0),((frame*width),0,width,height)) ; image=pygame.transform.scale(image,(width*1.50,height*1.50))
    return image

attack_1=enemy_three_attack(enemy_three_attack_image,0,100,100)  ; attack_2=enemy_three_attack(enemy_three_attack_image,1,100,100)  ; attack_3=enemy_three_attack(enemy_three_attack_image,2,100,100)  ; attack_4=enemy_three_attack(enemy_three_attack_image,3,100,100)  
attack_5=enemy_three_attack(enemy_three_attack_image,4,100,100)  ; attack_6=enemy_three_attack(enemy_three_attack_image,5,100,100)

def enemy_three_arrow(images,frame,width,height): 
    image=pygame.Surface((width,height),pygame.SRCALPHA) ; image.blit(images,(0,0),((frame*width),0,width,height)) ; image=pygame.transform.scale(image,(width*1.50,height*1.50))
    return image

arrow_1=enemy_three_arrow(enemy_three_arrow_image,0,24,5) ; arrow_2=enemy_three_arrow(enemy_three_arrow_image,1,24,5)

enemy_three_idle_list=[idle_1,idle_2,idle_3,idle_4,idle_5,idle_6,idle_7,idle_8,idle_9,idle_10] ; enemy_three_idle_list_flip=[] ; enemy_three_idle_number=[]
for idx,num in enumerate(enemy_three_idle_list[:]): enemy_three_idle_list_flip.append(pygame.transform.flip(num,True,False))

enemy_three_move_list=[move_1,move_2,move_3,move_4,move_5,move_6,move_7,move_8] ; enemy_three_move_list_flip=[] ; enemy_three_move_number=[]
for idx,num in enumerate(enemy_three_move_list[:]): enemy_three_move_list_flip.append(pygame.transform.flip(num,True,False))

enemy_three_fall_list=[fall_1,fall_2,fall_3,fall_4,fall_5,fall_6,fall_7,fall_8,fall_9,fall_10] ; enemy_three_fall_list_flip=[] ; enemy_three_fall_number=[]
for idx,num in enumerate(enemy_three_fall_list[:]): enemy_three_fall_list_flip.append(pygame.transform.flip(num,True,False))

enemy_three_attack_list=[attack_1,attack_2,attack_3,attack_4,attack_5,attack_6] ; enemy_three_attack_list_flip=[] ; enemy_three_attack_number=[]
for idx,num in enumerate(enemy_three_attack_list[:]): enemy_three_attack_list_flip.append(pygame.transform.flip(num,True,False))

enemy_three_arrow_list=[arrow_1,arrow_2] ; enemy_three_arrow_list_flip=[] ; enemy_three_arrow_number=[]
for idx,num in enumerate(enemy_three_arrow_list[:]): enemy_three_arrow_list_flip.append(pygame.transform.flip(num,True,False))

enemy_three_level_3_x=[2992,2902,3867,3356,3853] #700
enemy_three_level_3_y=[996,1806,1306,1412,1900] #2000


enemy_three_level_4_x=[870,992,1025] #700
enemy_three_level_4_y=[230,327,359] #2000


enemy_three_fall_type=[]

enemy_3_level_3_rect=[]
enemy_3_level_3_arrow_rect=[]
enemy_3_level_4_rect=[]
enemy_3_level_4_arrow_rect=[]

enemy_3_health=[]
player_last_position=[]

enemy_3_x_movement=[]
enemy_3_y_movement=[]

enemy_3_arrow_x_movement=[]
enemy_3_arrow_y_movement=[]

enemy_3_x_movement_control=[0]
enemy_3_y_movement_control=[0]

for idx,enemy_three in enumerate(enemy_three_level_3_x): enemy_3_level_3_rect.append(pygame.Rect(enemy_three_level_3_x[idx],enemy_three_level_3_y[idx],30,30))
for idx,enemy_three in enumerate(enemy_three_level_4_x): enemy_3_level_4_rect.append(pygame.Rect(enemy_three_level_4_x[idx],enemy_three_level_4_y[idx],30,30))

for idx,arrow in enumerate(enemy_three_level_3_x): enemy_3_level_3_arrow_rect.append(pygame.Rect(enemy_three_level_3_x[idx],enemy_three_level_3_y[idx],25,5))
for idx,arrow in enumerate(enemy_three_level_4_x): enemy_3_level_4_arrow_rect.append(pygame.Rect(enemy_three_level_4_x[idx],enemy_three_level_4_y[idx],25,5))


final_boss_support_x=[]
final_boss_support_y=[] 

final_boss_support_fall_type=[]

final_boss_support_health=[]

final_boss_support_x_movement=[]
final_boss_support_y_movement=[]


final_boss_support_rect=[]

