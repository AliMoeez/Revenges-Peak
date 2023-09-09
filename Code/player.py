import pygame

test_image=pygame.image.load(r"C:\Users\Owner\Desktop\A_Wits_End\A_Wit's_End\Player\Idle\idle_1.png")

class Player:
    def __init__(self):
        self.test_image=test_image

    def blit(self,SCREEN):
        SCREEN.blit(self.test_image,(50,50))

