from random import *
from pygame import *


init()

screen = display.set_mode(flags=RESIZABLE)  # flags=NOFRAME
display.set_caption('')
icon = image.load('images/icons/test.ico').convert_alpha()
display.set_icon(icon)

w, h = display.get_surface().get_size()

running = True
while running:

    screen.fill('black')



    display.update()

    keys = key.get_pressed()
    for event in event.get():
        if event.type == QUIT or keys[K_ESCAPE]:
            running = False
            quit()

