import pygame

x=1

class dog():
    def __init__(self,x):
        self.x=x
    
    def func(self):
        self.x=39
        print(self.x,"HER")

do=dog(x)
do.func()