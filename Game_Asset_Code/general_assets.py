import pygame
from pytmx.util_pygame import load_pygame

SCREEN_WIDTH=1200 ; SCREEN_HEIGHT=800 ; SCREEN=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

camera_x_y=[0,0]

clock=pygame.time.Clock()

FPS=100

run=True

level_screen=False

level_1=False

backround_tile_set=load_pygame(r"Assets\Tileset\backround_tile_set_file\backround_tile_set.tmx")

level_1_tile_set=load_pygame(r"Assets\Tileset\Level_1_Tile_Set_Sheet.tmx") ; level_1_tile_set_rect=[]

object_rect=[]

left_mouse_button_icon=pygame.image.load(r"Assets\Keys\Buttons Pack\Buttons Pack\MOUSE\MOUSEBUTTONLEFT.png")
left_mouse_button_icon=pygame.transform.scale(left_mouse_button_icon,(40,40))

tile_interact_rect_distance=[]

dialogue_condition=False
