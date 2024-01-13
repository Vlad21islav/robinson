from pygame import *
import pygame
import time

init()

path = ''

size = (500, 500)

screen = display.set_mode(size, flags=RESIZABLE)  # flags=NOFRAME
display.set_caption('robinson')
icon = image.load(path + 'images/icons/test.jpg').convert_alpha()
display.set_icon(icon)

left = [image.load(path + 'images/images/eyes_to_the_left.png').convert_alpha(),
        image.load(path + 'images/images/left_eye_1.png').convert_alpha(),
        image.load(path + 'images/images/left_eye_2.png').convert_alpha(),
        image.load(path + 'images/images/left_eye_3.png').convert_alpha(),
        image.load(path + 'images/images/left_eye_2.png').convert_alpha(),
        image.load(path + 'images/images/left_eye_1.png').convert_alpha()]

menu = 'start'

start_time = time.time()

turn = len(left)
next = time.time()

running = True
while running:
    w, h = pygame.display.get_surface().get_size()
    size = (w, h)
    man_size = (size[0] / 10, size[1] / 5)
    player_cor = ((size[0] - man_size[0]) / 10, (size[1] - man_size[1]) / 10 * 9)
    print(player_cor)
    screen.fill('black')

    if menu == 'start':
        bg = pygame.transform.scale(pygame.image.load('images/images/bg.jpg').convert_alpha(), size)
        screen.blit(bg, (0, 0))

    if time.time() - start_time >= 5:
        turn = 0
        start_time = time.time()
    if turn < len(left):
        if time.time() - next >= 0.1:
            next = time.time()
            man = left[turn]
            turn += 1
        else:
            man = left[turn]
    else:
        man = left[0]
    screen.blit(pygame.transform.scale(man, man_size), player_cor)

    display.update()

    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
            running = False
            pygame.quit()

