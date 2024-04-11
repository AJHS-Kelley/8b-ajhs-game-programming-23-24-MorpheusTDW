import pygame
from sys import exit
from random import randint, choice

resolution = 0 

if resolution == 0:
    x = 800
    y =600
else:
    x = 1920
    y = 1080
    pygame.init()
    difficulty = int(input("please choose a diffulcty.  enter 1 for easy or 2 for hard.\n"))
    

pygame.display.set_caption('name of game -- easy')
pygame.display.set_caption('name of game -- hard')

screen = pygame.display.set_mode(())

