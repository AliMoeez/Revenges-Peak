import pygame
import sys
import math
from pytmx.util_pygame import load_pygame

pygame.init()

from Game_Asset_Code import *
from Game_Code import Menu,LevelOne,Player,EnemyOne,EnemyTwo,Control

while run:
    level_1_tile_set_rect.clear()
    SCREEN.fill((0,0,0))
    key=pygame.key.get_pressed()
    event_list=pygame.event.get()

    for event in event_list:
        if event.type==pygame.QUIT:
            pygame.quit() 
            sys.exit()
        if not level_screen and not any([level_1]):
            if event.type==pygame.MOUSEBUTTONDOWN and menu.main_menu_buttons().collidepoint(event.pos):
                level_screen= not level_screen
        if level_screen:
            if key[pygame.K_q]:level_screen=False
            if menu.level_screen_blit_background() is not None:
                if event.type==pygame.MOUSEBUTTONDOWN and menu.level_screen_blit_background().collidepoint(event.pos):
                    level_screen=False
                    level_1=True
        if level_1:
            if key[pygame.K_q]:
                level_1=False ; level_screen=True
            if key[pygame.K_f] and player_control_cooldown[0]==1:
                for idx,distance in enumerate(control.distance()):
                    if distance<100:
                        player_control_index.clear()
                        player_control_index.append(idx)
                        player_control=True
    if player_control_cooldown[0]<=0:
        player_control=False
        player_control_index[0]="placeholder"

    menu=Menu(level_screen,level_1)
    menu.main_menu()
    menu.main_menu_buttons()
    menu.level_screen_blit_background()
    menu.level_screen_blit()

    levelone=LevelOne(camera_x_y,level_1,level_screen)
    levelone.level_one(player_control,player_control_cooldown)

    player=Player(player_x,player_y,player_width,player_height,player_rect,level_1,player_control)
    player.idle(key)
    player.move(key)
    player.attack(key)
    player.control(key)
    player.fall()
    player.collision_with_object()
    player.collision_with_object_logic()

    enemy_one=EnemyOne(level_1,enemy_1_level_1_rect)
    enemy_one.distance()
    enemy_one.idle()
    enemy_one.run()
    enemy_one.attack()
    enemy_one.collision()

    enemy_two=EnemyTwo(level_1,enemy_2_rects)
    enemy_two.distance()
    enemy_two.idle()
    enemy_two.run()
    enemy_two.attack()
    enemy_two.collision()

    control=Control(level_1,player_control,player_control_index)
    control.distance()
    control.enemy_definition()
    control.mechanic_idle(key)
    control.mechanic_walk(key)
    control.mechanic_attack(key)
    control.print_statement()

    player.health_power_cooldown_icons()

    pygame.display.update()