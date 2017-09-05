#! /usr/bin/env python
import pygame, random
from pygame.locals import *

width = 1920
height = 1080
gcm = 120
c = 0,255
size = 30

randompixels = pygame.Surface((gcm,gcm))
displaysurface = pygame.display.set_mode((width, height), FULLSCREEN, 32)
clock = pygame.time.Clock()

while True:
    for row in range(0,gcm,size):
        for column in range(0,gcm,size):
             red = random.choice(c)
             green = random.choice(c)
             blue = random.choice(c)
             pygame.draw.rect(randompixels, (red, green, blue), (column, row, size, size))
    for row in range(0,width,gcm):
        for column in range(0,height,gcm):
            displaysurface.blit(randompixels, (row, column)) 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    key=pygame.key.get_pressed()
    if key[pygame.K_q] or key[pygame.K_ESCAPE]:break
    pygame.display.flip()
    clock.tick(60)
