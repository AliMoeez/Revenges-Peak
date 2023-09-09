import pygame,sys
from Code.menu import Menu
from Code.player import Player

SCREEN_WIDTH=1200 ; SCREEN_HEIGHT=800 ; SCREEN=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

clock=pygame.time.Clock()

run=True

while run:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit() ; sys.exit()

    menu=Menu()
    menu.backround(SCREEN)

    player=Player()
    player.blit(SCREEN)

    pygame.display.update()