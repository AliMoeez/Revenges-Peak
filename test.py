import pygame,sys

pygame.init()

SCREEN_WIDTH=1200 ; SCREEN_HEIGHT=800 ; SCREEN=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

camera_x_y=[0,0]

clock=pygame.time.Clock()

FPS=100

run=True

while run:
    SCREEN.fill((0,0,0))
    key=pygame.key.get_pressed()
    event_list=pygame.event.get()

    for event in event_list:
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()


    pygame.display.update()