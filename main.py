import pygame
import sys
import math
from pytmx.util_pygame import load_pygame

pygame.init()

from Game_Asset_Code import *
from Game_Code import Menu,LevelOne,Player,EnemyOne,EnemyTwo,Control,Dialouge,People,Objectives,Lose,Tutorial,Win

while run:
    level_1_tile_set_rect.clear()
    object_rect.clear()
    key=pygame.key.get_pressed()
    event_list=pygame.event.get()
    if level_1:
        SCREEN.fill((131,164,72))

    menu=Menu(level_screen,level_1)
    levelone=LevelOne(camera_x_y,level_1,level_screen,level_1_wizard_talk,talk_to_abyss_level_one,investigate_object_level_one)

    player=Player(player_x,player_y,player_width,player_height,player_rect,level_1,
                  player_control,dialogue_condition,dialogue_story_condition,reset_locations,tutorial_one,tutorial_two)
    enemy_one=EnemyOne(level_1,enemy_1_level_1_rect,reset_locations)
    enemy_two=EnemyTwo(level_1,enemy_2_rects,reset_locations)
    people=People(level_1,level_1_wizard_talk,reset_locations)
    
    dialogue=Dialouge(level_1,dialogue_condition,dialogue_story_condition,level_1_wizard_talk)
    lose=Lose(level_1,player_lose_condition,reset_locations)
    tutorial=Tutorial(level_1,tutorial_one,tutorial_two)
    win=Win(level_1)
    
    for event in event_list:
        if dialogue.level_dialogue_condition(event,event_list):
            dialogue_condition=True ; dialogue_story_condition=False
            if event.type==pygame.MOUSEBUTTONDOWN :
                dialogue_click_list[0]+=1 ; text_position[0]=0

        if dialogue.level_dialogue_story(event,event_list):
            mouse_button_blit_list.clear() ; dialogue_story_condition=True ; dialogue_condition=False
            if event.type==pygame.MOUSEBUTTONDOWN:
                dialogue_click_list[0]+=1 ; text_position[0]=0
     
        if (dialogue_condition or dialogue_story_condition) and dialogue.end_dialouge(event,event_list): 
            mouse_button_blit_list.clear() ; dialogue_condition=False ; dialogue_story_condition=False
            if dialogue_objective_list[0]==1:
                level_1_wizard_talk=False
            if dialogue_objective_list[0]==2:
                talk_to_abyss_level_one=False
            if dialogue_objective_list[0]==3:
                investigate_object_level_one=False
                
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
            if tutorial.skip(event,event_list):
                text_position[0]=0
                if tutorial_one: tutorial_one=False
                if tutorial_two: tutorial_two=False
            if tutorial.begin_tutorial(event,event_list): tutorial_two=True
            if key[pygame.K_f] and player_control_cooldown[0]==1:
                for idx,distance in enumerate(control.distance()):
                    if distance<100:
                        player_control_index.clear()
                        player_control_index.append(idx)
                        player_control=True
            if key[pygame.K_v] and player_control:
                player_control_cooldown[0]=-0.05

        if lose.retry(event):
            player_lose_condition=False
            reset_locations=True

        if lose.back_to_menu(event):
            player_lose_condition=False
            reset_locations=True
            level_1=False
        
        if win.back_to_menu(event):
            reset_locations=True
            level_1=False
        #    level_1_wizard_talk=True
        #    talk_to_abyss_level_one=True
        #    investigate_object_level_one=True

    print(level_1_wizard_talk,talk_to_abyss_level_one,investigate_object_level_one)

    if win.story_reset_conditions():
        level_1_wizard_talk=True
        talk_to_abyss_level_one=True
        investigate_object_level_one=True
           
    if lose.condition():
        player_lose_condition=True
              
    if player_control_cooldown[0]<=0:
        player_control=False
        player_control_index[0]="placeholder"

    if player.reset_position() and enemy_one.reset_position() and enemy_two.reset_position() and people.reset_position():
        level_1_wizard_talk=True
        reset_locations=False

    menu.main_menu()
    menu.main_menu_buttons()
    menu.level_screen_blit_background()
    menu.level_screen_blit()

    levelone.border()
    levelone.tile_set_level_direction()
    levelone.tile_set()
 #   levelone.win_condition()

    player.move(key)
    player.attack(key)
    player.control(key)
    player.dialouge_state(key)
    player.fall()
    player.collision_with_object()
    player.collision_with_object_logic()

    enemy_one.distance()
    enemy_one.idle()
    enemy_one.run()
    enemy_one.attack()
    enemy_one.player_hit()
    enemy_one.fall()
    enemy_one.collision_with_object()
    enemy_one.collision_with_object_logic()

    enemy_two.distance()
    enemy_two.idle()
    enemy_two.run()
    enemy_two.attack()
    enemy_two.player_hit()
    enemy_two.fall()
    enemy_two.collision_with_object()
    enemy_two.collision_with_object_logic()

    control=Control(level_1,player_control,player_control_index)
    control.distance()
    control.enemy_definition()
    control.mechanic_walk(key)
    control.mechanic_attack(key)
    control.mechanic_collision()
    control.mechanic_collision_logic()

    people.idle()
    people.run()

    tutorial.player_idle_show()

    levelone.tile_set_tree_top()

    player.health_power_cooldown_icons()

    objectives=Objectives(level_1,level_1_wizard_talk,talk_to_abyss_level_one,investigate_object_level_one,dialogue_objective_list)
    objectives.level_one_objectives()
    objectives.show_objectives()
    
    dialogue.level_object_interaction()
    dialogue.text_type()
    dialogue.text_type_story()
    dialogue.show()

    tutorial.show()

    win.condition() 
    win.blit()

    lose.show_loss()

    pygame.display.update()