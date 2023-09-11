import pygame


player_x=100; player_y=100; player_width=100 ; player_height=100
player_rect=pygame.Rect(player_x,player_y,player_width,player_height)

idle_1=pygame.image.load(r"Assets\Player\Player Assets\animations\PNG\idle\idle_1.png") ; idle_2=pygame.image.load(r"Assets\Player\Player Assets\animations\PNG\idle\idle_2.png") ; idle_3=pygame.image.load(r"Assets\Player\Player Assets\animations\PNG\idle\idle_3.png") ; idle_4=pygame.image.load(r"Assets\Player\Player Assets\animations\PNG\idle\idle_4.png") ; idle_5=pygame.image.load(r"Assets\Player\Player Assets\animations\PNG\idle\idle_5.png") ; idle_6=pygame.image.load(r"Assets\Player\Player Assets\animations\PNG\idle\idle_6.png")
idle_7=pygame.image.load(r"Assets\Player\Player Assets\animations\PNG\idle\idle_7.png") ; idle_8=pygame.image.load(r"Assets\Player\Player Assets\animations\PNG\idle\idle_8.png") ; idle_9=pygame.image.load(r"Assets\Player\Player Assets\animations\PNG\idle\idle_9.png") ; idle_10=pygame.image.load(r"Assets\Player\Player Assets\animations\PNG\idle\idle_10.png") ; idle_11=pygame.image.load(r"Assets\Player\Player Assets\animations\PNG\idle\idle_11.png") ; idle_12=pygame.image.load(r"Assets\Player\Player Assets\animations\PNG\idle\idle_12.png")
player_idle=[idle_1,idle_2,idle_3,idle_4,idle_5,idle_6,idle_7,idle_7,idle_8,idle_9,idle_10,idle_11,idle_12] ; player_idle_flip=[] ; player_idle_loading_screen=[]
for idx,num in enumerate(player_idle): pygame.transform.scale(num,(100,100))
for idx,num in enumerate(player_idle[:]): player_idle_flip.append(pygame.transform.flip(num,True,False))
for idx,num in enumerate(player_idle[:]): player_idle_loading_screen.append(pygame.transform.scale(num,(200,200)))


run_1=pygame.image.load(r"Assets\Player\Player Assets\animations\PNG\run\run_1.png") ; run_2=pygame.image.load(r"Assets\Player\Player Assets\animations\PNG\run\run_2.png") ; run_3=pygame.image.load(r"Assets\Player\Player Assets\animations\PNG\run\run_3.png") ; run_4=pygame.image.load(r"Assets\Player\Player Assets\animations\PNG\run\run_4.png") ; run_5=pygame.image.load(r"Assets\Player\Player Assets\animations\PNG\run\run_5.png")
run_6=pygame.image.load(r"Assets\Player\Player Assets\animations\PNG\run\run_6.png") ; run_7=pygame.image.load(r"Assets\Player\Player Assets\animations\PNG\run\run_7.png") ; run_8=pygame.image.load(r"Assets\Player\Player Assets\animations\PNG\run\run_8.png") ; run_9=pygame.image.load(r"Assets\Player\Player Assets\animations\PNG\run\run_9.png") ; run_10=pygame.image.load(r"Assets\Player\Player Assets\animations\PNG\run\run_10.png")
player_run=[run_1,run_2,run_3,run_4,run_5,run_6,run_7,run_8,run_9,run_10] ; player_run_flip=[] ; player_run_number=[0]
for idx,num in enumerate(player_run): pygame.transform.scale(num,(100,100)) 
for idx,num in enumerate(player_run[:]): player_run_flip.append(pygame.transform.flip(num,True,False))

player_x_movement=[0] ; player_y_movement=[0]