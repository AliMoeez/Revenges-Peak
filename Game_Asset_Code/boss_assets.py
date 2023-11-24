import pygame

from .general_assets import * 

frost_brute_idle_1=pygame.image.load(r"Assets\Bosses\Frost Brute\Frost Brute Assets\idle\idle_1.png").convert_alpha()

frost_brute_idle_1=pygame.transform.scale(frost_brute_idle_1,(100,200))
frost_brute_idle_1=pygame.transform.scale(frost_brute_idle_1,(192*1.5,128*1.5))

frost_boss_x=500 #2850
frost_boss_y=1400 #735

frost_boss_x_movement=[0]
frost_boss_y_movement=[0]

frost_boss_x_increment=[0]
frost_boss_y_increment=[0]

frost_boss_damage=[0]

frost_boss_health=[1000]

frost_boss_fast_mode_timer=[0]
frost_boss_fast_mode_timer_max=[0]

frost_boss_slow_down_timer=[0]

frost_boss_rect=pygame.Rect(frost_boss_x,frost_boss_y,128*1.5,128*1.5)

frost_brute_image=pygame.image.load(r"Assets\Bosses\Frost Brute\Other\frost_guardian_free_192x128_SpriteSheet.png")

def frost_boss_idles(images,frame,width,height):
    image=pygame.Surface((width,height),pygame.SRCALPHA)
    image.blit(images,(0,0),((frame*width),0,width,height))
    image=pygame.transform.scale(image,(width*1.5,height*1.5))
    return image

frost_boss_idle_1=frost_boss_idles(frost_brute_image,0,192,128)
frost_boss_idle_2=frost_boss_idles(frost_brute_image,1,192,128)
frost_boss_idle_3=frost_boss_idles(frost_brute_image,2,192,128)
frost_boss_idle_4=frost_boss_idles(frost_brute_image,3,192,128)
frost_boss_idle_5=frost_boss_idles(frost_brute_image,4,192,128)
frost_boss_idle_6=frost_boss_idles(frost_brute_image,5,192,128)

frost_boss_idle=[frost_boss_idle_1,frost_boss_idle_2,frost_boss_idle_3,frost_boss_idle_4,frost_boss_idle_5,frost_boss_idle_6]
frost_boss_idle_flip=[]
frost_boss_idle_number=[0]
for i,frost_boss_image in enumerate(frost_boss_idle[:]): frost_boss_idle_flip.append(pygame.transform.flip(frost_boss_idle[i],True,False))

frost_boss_icon=pygame.image.load(r"Assets\Bosses\Frost Brute\Frost Brute Assets\idle\frost_icon.png")
frost_boss_icon=pygame.transform.scale(frost_boss_icon,(100,100))

def frost_boss_moves(images,frame,width,height):
    image=pygame.Surface((width,height),pygame.SRCALPHA)
    image.blit(images,(0,0),((frame*width),128,width,height))
    image=pygame.transform.scale(image,(width*1.5,height*1.5))
    return image

frost_boss_run_1=frost_boss_moves(frost_brute_image,0,192,128)
frost_boss_run_2=frost_boss_moves(frost_brute_image,1,192,128)
frost_boss_run_3=frost_boss_moves(frost_brute_image,2,192,128)
frost_boss_run_4=frost_boss_moves(frost_brute_image,3,192,128)
frost_boss_run_5=frost_boss_moves(frost_brute_image,4,192,128)
frost_boss_run_6=frost_boss_moves(frost_brute_image,5,192,128)
frost_boss_run_7=frost_boss_moves(frost_brute_image,6,192,128)
frost_boss_run_8=frost_boss_moves(frost_brute_image,7,192,128)
frost_boss_run_9=frost_boss_moves(frost_brute_image,8,192,128)
frost_boss_run_10=frost_boss_moves(frost_brute_image,9,192,128)

frost_boss_run=[frost_boss_run_1,frost_boss_run_2,frost_boss_run_3,frost_boss_run_4,frost_boss_run_5,frost_boss_run_6,frost_boss_run_7,frost_boss_run_8,frost_boss_run_9,frost_boss_run_10]
frost_boss_run_flip=[]
frost_boss_run_number=[0]
for i,frost_boss_image in enumerate(frost_boss_run[:]): frost_boss_run_flip.append(pygame.transform.flip(frost_boss_run[i],True,False))

def frost_boss_attacks(images,frame,width,height):
    image=pygame.Surface((width,height),pygame.SRCALPHA)
    image.blit(images,(0,0),((frame*width),256,width,height))
    image=pygame.transform.scale(image,(width*1.5,height*1.5))
    return image

frost_boss_attack_1=frost_boss_attacks(frost_brute_image,0,192,128)
frost_boss_attack_2=frost_boss_attacks(frost_brute_image,1,192,128)
frost_boss_attack_3=frost_boss_attacks(frost_brute_image,2,192,128)
frost_boss_attack_4=frost_boss_attacks(frost_brute_image,3,192,128)
frost_boss_attack_5=frost_boss_attacks(frost_brute_image,4,192,128)
frost_boss_attack_6=frost_boss_attacks(frost_brute_image,5,192,128)
frost_boss_attack_7=frost_boss_attacks(frost_brute_image,6,192,128)
frost_boss_attack_8=frost_boss_attacks(frost_brute_image,7,192,128)
frost_boss_attack_9=frost_boss_attacks(frost_brute_image,8,192,128)
frost_boss_attack_10=frost_boss_attacks(frost_brute_image,9,192,128)
frost_boss_attack_11=frost_boss_attacks(frost_brute_image,10,192,128)
frost_boss_attack_12=frost_boss_attacks(frost_brute_image,11,192,128)
frost_boss_attack_13=frost_boss_attacks(frost_brute_image,12,192,128)
frost_boss_attack_14=frost_boss_attacks(frost_brute_image,13,192,128)

frost_boss_attack=[frost_boss_attack_1,frost_boss_attack_2,frost_boss_attack_3,frost_boss_attack_4,frost_boss_attack_5,
                frost_boss_attack_6,frost_boss_attack_7,frost_boss_attack_8,frost_boss_attack_9,frost_boss_attack_10,frost_boss_attack_11,frost_boss_attack_12,frost_boss_attack_13,frost_boss_attack_14]
frost_boss_attack_flip=[]
frost_boss_attack_number=[0]
for i,frost_boss_image in enumerate(frost_boss_attack[:]): frost_boss_attack_flip.append(pygame.transform.flip(frost_boss_attack[i],True,False))

def frost_boss_falls(images,frame,width,height):
    image=pygame.Surface((width,height),pygame.SRCALPHA)
    image.blit(images,(0,0),((frame*width),512,width,height))
    image=pygame.transform.scale(image,(width*1.5,height*1.5))
    return image

frost_boss_fall_1=frost_boss_falls(frost_brute_image,0,192,128)
frost_boss_fall_2=frost_boss_falls(frost_brute_image,1,192,128)
frost_boss_fall_3=frost_boss_falls(frost_brute_image,2,192,128)
frost_boss_fall_4=frost_boss_falls(frost_brute_image,3,192,128)
frost_boss_fall_5=frost_boss_falls(frost_brute_image,4,192,128)
frost_boss_fall_6=frost_boss_falls(frost_brute_image,5,192,128)
frost_boss_fall_7=frost_boss_falls(frost_brute_image,6,192,128)
frost_boss_fall_8=frost_boss_falls(frost_brute_image,7,192,128)
frost_boss_fall_9=frost_boss_falls(frost_brute_image,8,192,128)
frost_boss_fall_10=frost_boss_falls(frost_brute_image,9,192,128)
frost_boss_fall_11=frost_boss_falls(frost_brute_image,10,192,128)
frost_boss_fall_12=frost_boss_falls(frost_brute_image,11,192,128)
frost_boss_fall_13=frost_boss_falls(frost_brute_image,12,192,128)
frost_boss_fall_14=frost_boss_falls(frost_brute_image,13,192,128)
frost_boss_fall_15=frost_boss_falls(frost_brute_image,14,192,128)
frost_boss_fall_16=frost_boss_falls(frost_brute_image,15,192,128)

frost_boss_fall=[frost_boss_fall_1,frost_boss_fall_2,frost_boss_fall_3,frost_boss_fall_4,frost_boss_fall_5,
                frost_boss_fall_6,frost_boss_fall_7,frost_boss_fall_8,frost_boss_fall_9,frost_boss_fall_10,frost_boss_fall_11,
                frost_boss_fall_12,frost_boss_fall_13,frost_boss_fall_14,frost_boss_fall_15,frost_boss_fall_16]
frost_boss_fall_flip=[]
frost_boss_fall_number=[0]
for i,frost_boss_image in enumerate(frost_boss_fall[:]): frost_boss_fall_flip.append(pygame.transform.flip(frost_boss_fall[i],True,False))

frost_boss_health_icon=pygame.image.load(r"Assets\Player\health_icon.png")
frost_boss_health_icon=pygame.transform.scale(frost_boss_health_icon,(17,17))

frost_boss_fast_mode_icon=pygame.image.load(r"Assets\Bosses\Frost Brute\Other\man-silhouette-running-escaping.png")
frost_boss_fast_mode_icon=pygame.transform.scale(frost_boss_fast_mode_icon,(17,17))

frost_boss_fall_type=[0]



