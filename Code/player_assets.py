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

player_x_movement=[0] ; player_y_movement=[0]