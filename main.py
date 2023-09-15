import pygame,sys
from pytmx.util_pygame import load_pygame

pygame.init()

from Game_Asset_Code import *
from Game_Code import Menu,LevelOne,Player

while run:
    SCREEN.fill((0,0,0))
    key=pygame.key.get_pressed()
    event_list=pygame.event.get()

    for event in event_list:
        if event.type==pygame.QUIT:
            pygame.quit() 
            sys.exit()
        if not level_screen:
            if event.type==pygame.MOUSEBUTTONDOWN and menu.main_menu_buttons().collidepoint(event.pos):
                level_screen= not level_screen
        if level_screen:
            if key[pygame.K_q]:level_screen=False
            if menu.level_screen_blit_background() is not None:
                if event.type==pygame.MOUSEBUTTONDOWN and menu.level_screen_blit_background().collidepoint(event.pos):
                    level_screen=False
                    level_1=True

    menu=Menu(level_screen,level_1)
    menu.main_menu()
    menu.main_menu_buttons()
    menu.level_screen_blit_background()
    menu.level_screen_blit()

    levelone=LevelOne(camera_x_y,level_1,level_screen)
    levelone.level_one()

    player=Player(player_x,player_y,player_width,player_height,player_rect,level_1)
    player.idle(key)
    player.move(key)
    player.collision()

    pygame.display.update()