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

test_tile_set=load_pygame(r"Assets\Tileset\Test_2\untitled.tmx")