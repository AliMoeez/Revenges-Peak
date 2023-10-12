import pygame

skeleton_1_idle_1=pygame.image.load(r"Assets\Enemies\Skeleton Enemy\Skeleton Assets\ready_1.png") ; skeleton_1_idle_2=pygame.image.load(r"Assets\Enemies\Skeleton Enemy\Skeleton Assets\ready_2.png") ; skeleton_1_idle_3=pygame.image.load(r"Assets\Enemies\Skeleton Enemy\Skeleton Assets\ready_3.png")
skeleton_idle=[skeleton_1_idle_1,skeleton_1_idle_2,skeleton_1_idle_3] ; skeleton_idle_flip=[] ; skeleton_idle_number=[]
for i,skeleton in enumerate(skeleton_idle): skeleton_idle[i]=pygame.transform.scale(skeleton_idle[i],(50*1.8,48*1.8))
for i,skeleton in enumerate(skeleton_idle[:]): skeleton_idle_flip.append(pygame.transform.flip(skeleton_idle[i],True,False))

skeleton_1_run_1=pygame.image.load(r"Assets\Enemies\Skeleton Enemy\Skeleton Assets\run_1.png") ; skeleton_1_run_2=pygame.image.load(r"Assets\Enemies\Skeleton Enemy\Skeleton Assets\run_2.png") ; skeleton_1_run_3=pygame.image.load(r"Assets\Enemies\Skeleton Enemy\Skeleton Assets\run_3.png")
skeleton_1_run_4=pygame.image.load(r"Assets\Enemies\Skeleton Enemy\Skeleton Assets\run_4.png") ; skeleton_1_run_5=pygame.image.load(r"Assets\Enemies\Skeleton Enemy\Skeleton Assets\run_5.png") ; skeleton_1_run_6=pygame.image.load(r"Assets\Enemies\Skeleton Enemy\Skeleton Assets\run_6.png")
skeleton_run=[skeleton_1_run_1,skeleton_1_run_2,skeleton_1_run_3,skeleton_1_run_4,skeleton_1_run_5,skeleton_1_run_6] ; skeleton_run_flip=[] ; skeleton_run_number=[]
for i,skeleton in enumerate(skeleton_run): skeleton_run[i]=pygame.transform.scale(skeleton_run[i],(50*1.8,48*1.8))
for i,skeleton in enumerate(skeleton_run[:]): skeleton_run_flip.append(pygame.transform.flip(skeleton_run[i],True,False))

skeleton_1_attack_1=pygame.image.load(r"Assets\Enemies\Skeleton Enemy\Skeleton Assets\attack1_1.png") ; skeleton_1_attack_2=pygame.image.load(r"Assets\Enemies\Skeleton Enemy\Skeleton Assets\attack1_2.png") ; skeleton_1_attack_3=pygame.image.load(r"Assets\Enemies\Skeleton Enemy\Skeleton Assets\attack1_3.png")
skeleton_1_attack_4=pygame.image.load(r"Assets\Enemies\Skeleton Enemy\Skeleton Assets\attack1_4.png") ; skeleton_1_attack_5=pygame.image.load(r"Assets\Enemies\Skeleton Enemy\Skeleton Assets\attack1_5.png") ; skeleton_1_attack_6=pygame.image.load(r"Assets\Enemies\Skeleton Enemy\Skeleton Assets\attack1_6.png")
skeleton_attack=[skeleton_1_attack_1,skeleton_1_attack_2,skeleton_1_attack_3,skeleton_1_attack_4,skeleton_1_attack_5,skeleton_1_attack_6] ; skeleton_attack_flip=[] ; skeleton_attack_number=[]
for i,skeleton in enumerate(skeleton_attack): skeleton_attack[i]=pygame.transform.scale(skeleton_attack[i],(100*1.8,65*1.8))
for i,skeleton in enumerate(skeleton_attack[:]): skeleton_attack_flip.append(pygame.transform.flip(skeleton_attack[i],True,False))

enemy_1_level_1_x=[400,450] ; enemy_1_level_1_y=[2000,2000] #400,200  800,200

enemy_1_x_movement=[] ; enemy_1_y_movement=[] 

enemy_1_level_1_rect=[]

for i,num in enumerate(enemy_1_level_1_x): enemy_1_level_1_rect.append(pygame.Rect(enemy_1_level_1_x[i],enemy_1_level_1_y[i],40,70))


brute_1_idle_1=pygame.image.load(r"Assets\Enemies\Brute_Enemy\Brute_Assets\imp_red\ready_1.png") ; brute_1_idle_2=pygame.image.load(r"Assets\Enemies\Brute_Enemy\Brute_Assets\imp_red\ready_2.png") ; brute_1_idle_3=pygame.image.load(r"Assets\Enemies\Brute_Enemy\Brute_Assets\imp_red\ready_3.png")
brute_1_idle_4=pygame.image.load(r"Assets\Enemies\Brute_Enemy\Brute_Assets\imp_red\ready_4.png") ; brute_1_idle_5=pygame.image.load(r"Assets\Enemies\Brute_Enemy\Brute_Assets\imp_red\ready_5.png") ; brute_1_idle_6=pygame.image.load(r"Assets\Enemies\Brute_Enemy\Brute_Assets\imp_red\ready_6.png")
brute_1_idle=[brute_1_idle_1,brute_1_idle_2,brute_1_idle_3,brute_1_idle_4,brute_1_idle_5,brute_1_idle_6]
brute_1_idle_flip=[] ; brute_1_idle_number=[]
for i,brute in enumerate(brute_1_idle): brute_1_idle[i]=pygame.transform.scale(brute_1_idle[i],(50*1.8,48*1.8))
for i,brtue in enumerate(brute_1_idle[:]): brute_1_idle_flip.append(pygame.transform.flip(brute_1_idle[i],True,False))

brute_1_run_1=pygame.image.load(r"Assets\Enemies\Brute_Enemy\Brute_Assets\imp_red\run_1.png") ; brute_1_run_2=pygame.image.load(r"Assets\Enemies\Brute_Enemy\Brute_Assets\imp_red\run_2.png") ; brute_1_run_3=pygame.image.load(r"Assets\Enemies\Brute_Enemy\Brute_Assets\imp_red\run_3.png")
brute_1_run_4=pygame.image.load(r"Assets\Enemies\Brute_Enemy\Brute_Assets\imp_red\run_4.png") ; brute_1_run_5=pygame.image.load(r"Assets\Enemies\Brute_Enemy\Brute_Assets\imp_red\run_5.png") ; brute_1_run_6=pygame.image.load(r"Assets\Enemies\Brute_Enemy\Brute_Assets\imp_red\run_6.png")
brute_1_run=[brute_1_run_1,brute_1_run_2,brute_1_run_3,brute_1_run_4,brute_1_run_5,brute_1_run_6]
brute_1_run_flip=[] ; brute_1_run_number=[]
for i,brute in enumerate(brute_1_run): brute_1_run[i]=pygame.transform.scale(brute_1_run[i],(50*1.8,48*1.8))
for i,brtue in enumerate(brute_1_run[:]): brute_1_run_flip.append(pygame.transform.flip(brute_1_run[i],True,False))

brute_1_attack_1_1=pygame.image.load(r"Assets\Enemies\Brute_Enemy\Brute_Assets\imp_red\attack1_1.png") ; brute_1_attack_1_2=pygame.image.load(r"Assets\Enemies\Brute_Enemy\Brute_Assets\imp_red\attack1_2.png")  ; brute_1_attack_1_3=pygame.image.load(r"Assets\Enemies\Brute_Enemy\Brute_Assets\imp_red\attack1_3.png")
brute_1_attack_1_4=pygame.image.load(r"Assets\Enemies\Brute_Enemy\Brute_Assets\imp_red\attack1_4.png") ; brute_1_attack_1_5=pygame.image.load(r"Assets\Enemies\Brute_Enemy\Brute_Assets\imp_red\attack1_5.png") ; brute_1_attack_1_6=pygame.image.load(r"Assets\Enemies\Brute_Enemy\Brute_Assets\imp_red\attack1_6.png")
brute_1_attack_1=[brute_1_attack_1_1,brute_1_attack_1_2,brute_1_attack_1_3,brute_1_attack_1_4,brute_1_attack_1_5,brute_1_attack_1_6]
brute_1_attack_flip_1=[] ; brute_1_attack_number=[0]
for i,brute in enumerate(brute_1_attack_1): brute_1_attack_1[i]=pygame.transform.scale(brute_1_attack_1[i],(100*1.8,65*1.8))
for i,brute in enumerate(brute_1_attack_1[:]) : brute_1_attack_flip_1.append(pygame.transform.flip(brute_1_attack_1[i],True,False))

enemy_2_level_1_x=[500] ; enemy_2_level_1_y=[2000]  #600,200

enemy_2_x_movement=[] ; enemy_2_y_movement=[]

enemy_2_rects=[]

enemy_run_number=[0] ; enemy_idle_number=[0] ; enemy_attack_number=[0] ; enemy_x_movement=[0] ; enemy_y_movement=[0]

