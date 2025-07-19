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


# --- Code below added from older base dir main.py for reference ---
# The following main() implementation is from the older version and may be useful for reference or alternative logic.

# def main():
#     running = True
#     spiro = guide.SpiroGuide(WIDTH, HEIGHT, PADDING, RADIUS, 60, (CENTERX, CENTERY))
#     spiro.add_gear(0, 2)
#     while running:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 running = False
#             else:
#                 if event.type == pygame.MOUSEBUTTONDOWN:
#                     spiro.click(event.pos)
#                 if event.type == pygame.KEYDOWN:
#                     spiro.key_press(event.key)
#         spiro.update()
#
#     pygame.quit()

# --- End of code added from older base dir main.py ---
