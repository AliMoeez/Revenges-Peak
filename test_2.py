import pygame,sys
from pytmx.util_pygame import load_pygame

pygame.init()

from Game_Asset_Code import *

class Try:
    def __init__(self,level_1):
        self.mouse=pygame.mouse.get_pos() ; self.level_1=level_1

    def method(self,event_list):
        x=SCREEN.blit(player_image,(100,200))
        for event in event_list:
            if event.type==pygame.MOUSEBUTTONDOWN and player_image.get_rect().collidepoint(event.pos):
                self.level_1=True
        
        print(self.level_1)

while run:
    SCREEN.fill((0,0,0))
    key=pygame.key.get_pressed()
    event_list=pygame.event.get()

    trial=Try(level_1)
    
    for event in event_list:
        if event.type==pygame.QUIT:
            pygame.quit() 
            sys.exit()
        if event.type==pygame.MOUSEBUTTONDOWN and player_image.get_rect().collidepoint(event.pos):
            level_1=True
        
    trial.method(event_list)


    pygame.display.update()