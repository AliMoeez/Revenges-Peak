import pygame,sys
from menu import Menu
from level import Level
from player import Player

SCREEN_WIDTH=1200 ; SCREEN_HEIGHT=800 ; SCREEN=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

clock=pygame.time.Clock()

run=True

while run:
    key=pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit() ; sys.exit()

    menu=Menu()
    menu.backround(SCREEN)

    level=Level()
    level.level_one()

    player=Player(100,200,100,100,0)
    player.idle(key,SCREEN)
    player.move(key,SCREEN)

    pygame.display.update()