import pygame

from .general_assets import *

elder_idle=pygame.image.load(r"Assets\People\Wizard Pack\Idle.png").convert_alpha()

def elder_idles(images,frame,width,height):
    image=pygame.Surface((width,height),pygame.SRCALPHA) ; image.blit(images,(0,0),((frame*width),0,width,height)) ; image=pygame.transform.scale(image,(width//1.3,height//1.3))
    return image

idle_1=elder_idles(elder_idle,0,231,231); idle_2=elder_idles(elder_idle,1,231,231) ; idle_3=elder_idles(elder_idle,2,231,231)
idle_4=elder_idles(elder_idle,3,231,231) ; idle_5=elder_idles(elder_idle,4,231,231) ; idle_6=elder_idles(elder_idle,5,231,231)
elder_idle_list=[idle_1,idle_2,idle_3,idle_4,idle_5,idle_6] ; elder_idle_list_flip=[] ; elder_idle_number=[] ; elder_idle_number_level_4=[0]
for idx,num in enumerate(elder_idle_list[:]): elder_idle_list_flip.append(pygame.transform.flip(num,True,False))

elder_run=pygame.image.load(r"Assets\People\Wizard Pack\Run.png")

def elder_runs(images,frame,width,height):
    image=pygame.Surface((width,height),pygame.SRCALPHA) ; image.blit(images,(0,0),((frame*width),0,width,height)) ; image=pygame.transform.scale(image,(width//1.3,height//1.3))
    return image

run_1=elder_runs(elder_run,0,231,231); run_2=elder_runs(elder_run,1,231,231); run_3=elder_runs(elder_run,2,231,231) ; run_4=elder_runs(elder_run,3,231,231)
run_5=elder_runs(elder_run,4,231,231) ; run_6=elder_runs(elder_run,5,231,231) ; run_7=elder_runs(elder_run,6,231,231) ; run_8=elder_runs(elder_run,7,231,231)
elder_run_list=[run_1,run_2,run_3,run_4,run_5,run_6,run_7,run_8] ; elder_run_list_flip=[] ; elder_run_number=[]
for idx,num in enumerate(elder_run_list[:]): elder_run_list_flip.append(pygame.transform.flip(num,True,False))

elder_icon=pygame.image.load(r"Assets\People\Wizard Pack\Icon.png")
elder_icon=pygame.transform.scale(elder_icon,(150,120))

guard_idle=pygame.image.load(r"Assets\People\sprite sheets\medieval\shady_guy.png")


final_boss_x=[900]
final_boss_y=[2000]

final_boss_rect=pygame.Rect(final_boss_x[0],final_boss_y[0],100,100)

final_boss_health=[1000]

















def guard_idles(images,frame,width,height):
    image=pygame.Surface((width,height),pygame.SRCALPHA) ; image.blit(images,(0,0),((frame*width),0,width,height)) ; image=pygame.transform.scale(image,(width//0.5,height//0.5))
    return image

guard_idle_1=guard_idles(guard_idle,0,34,34) ; guard_idle_2=guard_idles(guard_idle,1,34,34) ; guard_idle_3=guard_idles(guard_idle,2,34,34) ; guard_idle_4=guard_idles(guard_idle,3,34,34)
guard_idle_5=guard_idles(guard_idle,4,34,34)

guard_idle_list=[guard_idle_1,guard_idle_2,guard_idle_3,guard_idle_4,guard_idle_5] ; guard_idle_list_flip=[] ; guard_idle_number=[0]
for idx,num in enumerate(guard_idle_list[:]): guard_idle_list_flip.append(pygame.transform.flip(num,True,False))

guard_icon=pygame.image.load(r"Assets\People\individual sprites\medieval\shady_guy\shady_guy_icon.png")
guard_icon=pygame.transform.scale(guard_icon,(130,100))

people_level_1_x=[400]
people_level_1_y=[1500]
people_level_x_movement=[]
people_level_y_movement=[]
people_level_1_rect=[]
people_health_list=[]

for i,y in enumerate(people_level_1_x): people_level_1_rect.append(pygame.Rect(people_level_1_x[i],people_level_1_y[i],231,231))

people_level_2_x=[350]
people_level_2_y=[500]
people_level_2_rect=[]
for i,y in enumerate(people_level_2_x): people_level_2_rect.append(pygame.Rect(people_level_2_x[i],people_level_2_y[i],34,34))



