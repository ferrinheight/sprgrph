#!/usr/bin/env python
#main.py

from constants import *
from utils import *
import pygame
import math
import gear
import guide


# Initialize Pygame
pygame.init()

def main():
    clock = pygame.time.Clock()
    running = True
    spiro = guide.SpiroGuide(WIDTH, HEIGHT, PADDING, RADIUS, 60, (CENTERX, CENTERY))
    spiro.add_gear((rand() * (RADIUS * 0.8) + 20) - 20, hole_count = 2)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    spiro.speed_change('up')
                if event.key == pygame.K_DOWN:
                    spiro.speed_change('down')

        spiro.update()
        clock.tick(spiro.speed)

    pygame.quit()

if __name__ == "__main__":
    main()
