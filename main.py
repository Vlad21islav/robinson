from random import *
from pygame import *
import pygame


init()

path = ''

size = (500, 500)

screen = display.set_mode(size, flags=RESIZABLE)  # flags=NOFRAME
display.set_caption('robinson')
icon = image.load(path + 'images/icons/test.jpg').convert_alpha()
display.set_icon(icon)

menu = 'start'

running = True
while running:
    w, h = pygame.display.get_surface().get_size()
    size = (w, h)
    screen.fill('black')

    if menu == 'start':
        bg = pygame.transform.scale(pygame.image.load('images/images/bg.jpg').convert_alpha(), size)
        screen.blit(bg, (0, 0))

    display.update()

    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
            running = False
            pygame.quit()

