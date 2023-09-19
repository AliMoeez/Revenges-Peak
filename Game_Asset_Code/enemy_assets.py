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
for i,skeleton in enumerate(skeleton_attack): skeleton_attack[i]=pygame.transform.scale(skeleton_attack[i],(50*1.8,48*1.8))
for i,skeleton in enumerate(skeleton_attack[:]): skeleton_attack_flip.append(pygame.transform.flip(skeleton_attack[i],True,False))

enemy_1_level_1_x=[400,800] ; enemy_1_level_2_y=[200,200]

enemy_1_level_1_rect=[]

for i,num in enumerate(enemy_1_level_1_x): enemy_1_level_1_rect.append(pygame.Rect(enemy_1_level_1_x[i],enemy_1_level_2_y[i],40,70))