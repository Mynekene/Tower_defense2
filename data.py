import pygame
import os

pygame.init()

size_window = (1024,700)
size_tower = (90, 90)
size_mob = (80, 80)
size_font = (70)

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

path = [
    (0, 216),
    (680, 216),
    (680, 116),      
    (930, 116),        
    (930, 390),        
    (740, 390),
    (740, 480),
    (95, 480),
    (95, 700)
]

FPS = 60

abs_path = os.path.abspath(__file__ + "/..")
background_image = pygame.transform.scale(pygame.image.load(os.path.join(abs_path, "image", "background.png")), size_window)
menu_background_image = pygame.transform.scale(pygame.image.load(os.path.join(abs_path, "image", "menu_background.png")), size_window)
mob_image = pygame.transform.scale(pygame.image.load(os.path.join(abs_path, "image", "mob.png")), size_mob)