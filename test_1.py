import pygame,sys
from pytmx.util_pygame import load_pygame

pygame.init()

from Game_Asset_Code import *
from Game_Code import Menu
from Game_Code import LevelOne

while run:
    print(level_1)
    SCREEN.fill((0,0,0))
    key=pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit() 
            sys.exit()
    
    menu=Menu()
    menu.main_menu()
    menu.main_menu_buttons()
    menu.level_screen_blit_backround(event)
    menu.level_screen_blit(event,key)

    levelone=LevelOne(camera_x_y)
    levelone.level_one()

    pygame.display.update()