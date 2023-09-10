import pygame

x_1=pygame.image.load(r"Assets\Player\Player Assets\animations\PNG\idle\idle_1.png")
x_2=pygame.image.load(r"Assets\Player\Player Assets\animations\PNG\idle\idle_2.png")
player_idle=[x_1,x_2] ; player_idle_flip=[]
for idx,num in enumerate(player_idle): pygame.transform.scale(num,(100,100))
for idx,num in enumerate(player_idle[:]): player_idle_flip.append(pygame.transform.flip(num,True,False))

run_1=pygame.image.load(r"Assets\Player\Player Assets\animations\PNG\run\run_1.png") ; run_2=pygame.image.load(r"Assets\Player\Player Assets\animations\PNG\run\run_2.png") ; run_3=pygame.image.load(r"Assets\Player\Player Assets\animations\PNG\run\run_3.png") ; run_4=pygame.image.load(r"Assets\Player\Player Assets\animations\PNG\run\run_4.png") ; run_5=pygame.image.load(r"Assets\Player\Player Assets\animations\PNG\run\run_5.png")
run_6=pygame.image.load(r"Assets\Player\Player Assets\animations\PNG\run\run_6.png") ; run_7=pygame.image.load(r"Assets\Player\Player Assets\animations\PNG\run\run_7.png") ; run_8=pygame.image.load(r"Assets\Player\Player Assets\animations\PNG\run\run_8.png") ; run_9=pygame.image.load(r"Assets\Player\Player Assets\animations\PNG\run\run_9.png") ; run_10=pygame.image.load(r"Assets\Player\Player Assets\animations\PNG\run\run_10.png")
player_run=[run_1,run_2,run_3,run_4,run_5,run_6,run_7,run_8,run_9,run_10] ; player_run_flip=[] ; player_run_number=[0]
for idx,num in enumerate(player_run): pygame.transform.scale(num,(100,100)) 
for idx,num in enumerate(player_run[:]): player_run_flip.append(pygame.transform.flip(num,True,False))

player_x_movement=[0]
player_y_movement=[0]

class Player():

    def __init__(self,player_x,player_y,player_width,player_height,player_rect):
        self.player_x=player_x ; self.player_y=player_y ; self.player_width=player_width ; self.player_height=player_height
        self.player_rect=pygame.Rect(self.player_x,self.player_y,self.player_width,self.player_height)
        self.player_x_movement=player_x_movement ; self.player_y_movement=player_y_movement

    def idle(self,key,SCREEN):
        self.player_idle=player_idle ; self.player_idle_flip=player_idle_flip
        if not key[pygame.K_d] or  key[pygame.K_a]:
            SCREEN.blit(self.player_idle[0],(100,200))

    def move(self,key,SCREEN):
        self.player_run=player_run ; self.player_run_flip=player_run_flip ; self.player_run_number=player_run_number
        if key[pygame.K_d]:
            self.player_x_movement[0]=2
        if key[pygame.K_d] and key[pygame.K_w]:
            self.player_x_movement[0]=1
            self.player_y_movement[0]=-1
        if key[pygame.K_w]:
            self.player_y_movement[0]=-2
        if key[pygame.K_d] or key[pygame.K_d] and key[pygame.K_w]:
            SCREEN.blit(self.player_run[int(self.player_run_number[0])//2],(self.player_rect.x,self.player_rect.y))

        if key[pygame.K_a]:
            self.player_x_movement[0]=-2
        if key[pygame.K_a] and key[pygame.K_s]:
            self.player_x_movement[0]=-1
            self.player_y_movement[0]=1
        if key[pygame.K_s]:
            self.player_y_movement[0]=2
        if key[pygame.K_a] or key[pygame.K_a] and key[pygame.K_s]:
            SCREEN.blit(self.player_run_flip[int(self.player_run_number[0])//2],(self.player_rect.x,self.player_rect.y))

        self.player_run_number[0]+=0.13
        if self.player_run_number[0]>10:
            self.player_run_number[0]=0

        self.player_rect.x+=self.player_x_movement[0]
        self.player_rect.y+=self.player_y_movement[0]




