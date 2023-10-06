#!/usr/bin/env python
#main.py

from constants import *
from utils import *
import pygame
import math
import gear
import guide
from random import randint

# Initialize Pygame
pygame.init()


def main():
    clock = pygame.time.Clock()
    running = True
    spiro = guide.SpiroGuide(WIDTH, HEIGHT, PADDING, RADIUS, 60, (CENTERX, CENTERY))
    spiro.add_gear(0, 2)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            else:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    spiro.click(event.pos)
                if event.type == pygame.KEYDOWN:
                    spiro.key_press(event.key)

        spiro.update()
        clock.tick(spiro.speed)

    pygame.quit()

if __name__ == "__main__":
    main()
