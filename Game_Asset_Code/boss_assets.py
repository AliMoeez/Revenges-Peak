import pygame

from .general_assets import * 

frost_brute_idle_1=pygame.image.load(r"Assets\Bosses\Frost Brute\Frost Brute Assets\idle\idle_1.png").convert_alpha()

frost_brute_idle_1=pygame.transform.scale(frost_brute_idle_1,(100,200))
frost_brute_idle_1=pygame.transform.scale(frost_brute_idle_1,(192*1.5,128*1.5))

frost_boss_x=2850
frost_boss_y=735

frost_boss_rect=pygame.Rect(frost_boss_x,frost_boss_y,192*1.5,128*1.5)

