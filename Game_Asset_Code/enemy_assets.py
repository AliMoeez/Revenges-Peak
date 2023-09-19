import pygame

skeleton_1_idle_1=pygame.image.load(r"Assets\Enemies\Skeleton Enemy\Skeleton Assets\ready_1.png")
skeleton_1_idle_1=pygame.transform.scale(skeleton_1_idle_1,(50*1.8,48*1.8))

enemy_1_level_1_x=[400,800]
enemy_1_level_2_y=[200,200]

enemy_1_level_1_rect=[]

for i,num in enumerate(enemy_1_level_1_x):
    enemy_1_level_1_rect.append(pygame.Rect(enemy_1_level_1_x[i],enemy_1_level_2_y[i],40,70))