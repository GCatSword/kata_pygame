import pygame
from pygame.locals import *
import sys


pygame.init()

pantalla = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Hola mundo")

rojo = 0
d = 1

juego_activo = True

while juego_activo:
    for event in pygame.event.get():
        if event.type == QUIT:
            juego_activo = False

    rojo += d

    if rojo == 255:
        d = -1
    if rojo == 0:
        d = 1

    pantalla.fill((rojo,0,0))
    pygame.display.flip()

    pygame.time.delay(5)
    

pygame.quit()
sys.exit()

