import pygame

from .general_assets import *

player_x=450; player_y=2000; player_width=15 ; player_height=64 ; player_control=False #450,2000
player_rect=pygame.Rect(player_x,player_y,player_width,player_height)

player_x_movement=[0] ; player_y_movement=[0] ; player_key=[0] ; player_health=[1000] ; player_control_cooldown=[1] ; player_control_index=["placeholder"]

player_image=pygame.image.load(r"Assets\Player\swordman_1.png").convert_alpha() 
player_icon=pygame.image.load(r"Assets\Player\player_icon.png").convert_alpha() ; player_icon=pygame.transform.scale(player_icon,(100,100))
health_icon=pygame.image.load(r"Assets\Player\health_icon.png").convert_alpha() ; health_icon=pygame.transform.scale(health_icon,(17,17))
sword_icon=pygame.image.load(r"Assets\Player\sword.png").convert_alpha() ; sword_icon=pygame.transform.scale(sword_icon,(13,13)) ; 
potion_icon=pygame.image.load(r"Assets\Player\potion.png").convert_alpha() ; potion_icon=pygame.transform.scale(potion_icon,(13,13))

def player_idle(images,frame,width,height):    #set 0 value to 0 for idle, 64 for run , 128 for fall and 192 for attack
    image=pygame.Surface((width,height),pygame.SRCALPHA) ; image.blit(images,(0,0),((frame*width),0,width,height)) ; image=pygame.transform.scale(image,(width*2,height*2))
    return image
idle_1=player_idle(player_image,0,64,64) ; idle_2=player_idle(player_image,1,64,64) ; idle_3=player_idle(player_image,2,64,64) ; idle_4=player_idle(player_image,3,64,64) ; idle_5=player_idle(player_image,4,64,64) ; idle_6=player_idle(player_image,5,64,64)
player_idle_list=[idle_1,idle_2,idle_3,idle_4,idle_5,idle_6] ; player_idle_list_flip=[] ; player_idle_number=[0]
for idx,num in enumerate(player_idle_list[:]): player_idle_list_flip.append(pygame.transform.flip(num,True,False))

def player_run(images,frame,width,height):
    image=pygame.Surface((width,height),pygame.SRCALPHA) ; image.blit(images,(0,0),((frame*width),64,width,height)) ; image=pygame.transform.scale(image,(width*2,height*2))
    return image
run_1=player_run(player_image,0,64,64) ; run_2=player_run(player_image,1,64,64) ; run_3=player_run(player_image,2,64,64) ; run_4=player_run(player_image,3,64,64) ; run_5=player_run(player_image,4,64,64) ; run_6=player_run(player_image,5,64,64)
player_run_list=[run_1,run_2,run_3,run_4,run_5,run_6] ; player_run_list_flip=[] ; player_run_number=[0]
for idx,num in enumerate(player_run_list[:]): player_run_list_flip.append(pygame.transform.flip(num,True,False))

def player_fall(images,frame,width,height):
    image=pygame.Surface((width,height),pygame.SRCALPHA) ; image.blit(images,(0,0),((frame*width),128,width,height)) ; image=pygame.transform.scale(image,(width*2,height*2))
    return image
fall_1=player_fall(player_image,0,64,64) ; fall_2=player_fall(player_image,1,64,64) ; fall_3=player_fall(player_image,2,64,64) ; fall_4=player_fall(player_image,3,64,64) ; fall_5=player_fall(player_image,4,64,64) ; fall_6=player_fall(player_image,5,64,64)
player_fall_list=[fall_1,fall_2,fall_3,fall_4,fall_5,fall_6] ; player_fall_list_flip=[] ; player_fall_number=[0]
for idx,num in enumerate(player_fall_list[:]): player_fall_list_flip.append(pygame.transform.flip(num,True,False))

def player_attack(images,frame,width,height): 
    image=pygame.Surface((width,height),pygame.SRCALPHA) ; image.blit(images,(0,0),((frame*width),192,width,height)) ; image=pygame.transform.scale(image,(width*2,height*2))
    return image
attack_1=player_attack(player_image,0,64,64) ; attack_2=player_attack(player_image,1,64,64) ; attack_3=player_attack(player_image,2,64,64) ; attack_4=player_attack(player_image,3,64,64) ; attack_5=player_attack(player_image,4,64,64) ; attack_6=player_attack(player_image,5,64,64)
player_attack_list=[attack_1,attack_2,attack_3,attack_4,attack_5,attack_6] ; player_attack_list_flip=[] ; player_attack_number=[0] ; player_attack_cooldown=[4]
for idx,num in enumerate(player_attack_list[:]): player_attack_list_flip.append(pygame.transform.flip(num,True,False))



