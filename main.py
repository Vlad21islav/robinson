from random import *
from pygame import *
import pygame


init()

screen = display.set_mode((500, 500), flags=RESIZABLE)  # flags=NOFRAME
display.set_caption('robinzon')
icon = image.load('images/icons/test.jpg').convert_alpha()
display.set_icon(icon)

w, h = display.get_surface().get_size()

running = True
while running:

    screen.fill('black')



    display.update()

    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
            running = False
            pygame.quit()

