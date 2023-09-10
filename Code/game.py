import pygame,sys
from general_assets import *
from player_assets import *


test_image=pygame.image.load(r"C:\Users\Owner\Desktop\We Will Fight\desert_6.png").convert()
test_image=pygame.transform.scale(test_image,(1200,800))


class Menu:
    def __init__(self):
        self.WHITE=(205,205,205)

    def backround(self):
        SCREEN.blit(test_image,(0,0))

class Level(Menu):
    def __init__(self,camera_x_y):
        self.camera_x_y=camera_x_y ; self.player_rect=player_rect

    def level_one(self):
        self.camera_x_y[0]+=self.player_rect.x-self.camera_x_y[0]
        self.camera_x_y[1]+=self.player_rect.y-self.camera_x_y[1]

class Player(Level):
    def __init__(self,player_x,player_y,player_width,player_height,player_rect):
        super().__init__(camera_x_y)
        self.player_x=player_x ; self.player_y=player_y ; self.player_width=player_width ; self.player_height=player_height
        self.player_rect=pygame.Rect(self.player_x,self.player_y,self.player_width,self.player_height)
        self.player_x_movement=player_x_movement ; self.player_y_movement=player_y_movement

    def idle(self):
        self.player_idle=player_idle ; self.player_idle_flip=player_idle_flip
        if not key[pygame.K_d] and not key[pygame.K_a] and not key[pygame.K_w] and not key[pygame.K_s]:
            SCREEN.blit(self.player_idle[0],(100,200))

    def move(self):
        self.player_run=player_run ; self.player_run_flip=player_run_flip ; self.player_run_number=player_run_number
        if key[pygame.K_d]:
            self.player_x_movement[0]=2
            if key[pygame.K_w]:
                self.player_x_movement[0]=1 ; self.player_y_movement[0]=-1
        elif key[pygame.K_w]: self.player_y_movement[0]=-2
        if key[pygame.K_d] or key[pygame.K_d] and key[pygame.K_w] or key[pygame.K_w]:
            SCREEN.blit(self.player_run[int(self.player_run_number[0])//2],(self.player_rect.x,self.player_rect.y))

        if key[pygame.K_a]:
            self.player_x_movement[0]=-2
            if key[pygame.K_s]:
                self.player_x_movement[0]=-1 ; self.player_y_movement[0]=1
        elif key[pygame.K_s]: self.player_y_movement[0]=2
        if key[pygame.K_a] or key[pygame.K_a] and key[pygame.K_s] or key[pygame.K_s]:
            SCREEN.blit(self.player_run_flip[int(self.player_run_number[0])//2],(self.player_rect.x,self.player_rect.y))

        self.player_run_number[0]+=0.10
        if self.player_run_number[0]>10:self.player_run_number[0]=0

    def collision(self):
        Player.move(self)
        self.player_rect.x+=self.player_x_movement[0]
        self.player_rect.y+=self.player_y_movement[0]

        print(self.player_rect.x,self.player_rect.y)

while run:
    key=pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit() 
            sys.exit()

    menu=Menu()
    menu.backround()

    level=Level(camera_x_y)
    level.level_one()

    player=Player(player_x,player_y,player_width,player_height,player_rect)
    player.idle()
    player.move()
    player.collision()

    pygame.display.update()

