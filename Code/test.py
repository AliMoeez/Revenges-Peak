import pygame

SCREEN_WIDTH=1200 ; SCREEN_HEIGHT=800 ; SCREEN=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

player_image=pygame.image.load(r"Assets\Player\swordman_1.png").convert_alpha()

def func(images,frame,w,h):    #set 0 value to 0 for idle, 64 for run , 128 for fall and 192 for attack
    image=pygame.Surface((w,h),pygame.SRCALPHA)
    image.blit(images,(0,0),((frame*w),0,w,h))
    image=pygame.transform.scale(image,(w*2,h*2))
    return image

test_1=func(player_image,0,64,64) ; test_2=func(player_image,1,64,64) ; test_3=func(player_image,2,64,64) ; test_4=func(player_image,3,64,64)
test_5=func(player_image,4,64,64) ; test_6=func(player_image,5,64,64)

list_test=[test_1,test_2,test_3,test_4,test_5,test_6]

test=func(player_image,140,64,64)

number=[0]

run=True

while run:
    SCREEN.fill((100,0,0))
    event_list = pygame.event.get()
    for event in event_list:
        if event.type == pygame.QUIT:
            run = False 

    SCREEN.blit(test,(400,200))
    SCREEN.blit(list_test[int(number[0])//2],(100,200))
    
    number[0]+=0.02
    if number[0]>7:
        number[0]=0



    SCREEN.blit(player_image,(100,400))

    pygame.display.update()

pygame.quit()
exit()