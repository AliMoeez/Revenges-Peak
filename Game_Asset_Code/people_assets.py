import pygame

elder_image=pygame.image.load(r"Assets\People\Wizard Pack\Idle.png")


def elder_idle(images,frame,width,height):
    image=pygame.Surface((width,height),pygame.SRCALPHA) ; image.blit(images,(0,0),((frame*width),0,width,height)) ; image=pygame.transform.scale(image,(width//1.3,height//1.3))
    return image

idle_1=elder_idle(elder_image,0,231,231) ; idle_2=elder_idle(elder_image,1,231,231) ; idle_3=elder_idle(elder_image,2,231,231)
idle_4=elder_idle(elder_image,3,231,231) ; idle_5=elder_idle(elder_image,4,231,231) ; idle_6=elder_idle(elder_image,5,231,231)
elder_idle_list=[idle_1,idle_2,idle_3,idle_4,idle_5,idle_6] ; elder_idle_list_flip=[] ; elder_idle_number=[0]
for idx,num in enumerate(elder_idle_list[:]): elder_idle_list_flip.append(pygame.transform.flip(num,True,False))


people_level_1_x=[430]
people_level_1_y=[1500]
people_level_1_x_movement=[0]
people_level_1_y_movement=[0]
people_level_1_rect=[]

for i,y in enumerate(people_level_1_x): people_level_1_rect.append(pygame.Rect(people_level_1_x[i],people_level_1_y[i],231,231))
