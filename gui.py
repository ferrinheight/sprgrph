#!/usr/bin/env python
"""
gui.py - Pygame-based GUI for Spirograph
Handles all drawing, event handling, and user interaction.
Imports pure logic from gear.py and guide.py.
"""

import pygame
from guide import SpiroGuide
from constants import WIDTH, HEIGHT, PADDING, RADIUS, CENTERX, CENTERY

def run_gui():
    pygame.init()
    clock = pygame.time.Clock()
    running = True
    spiro = SpiroGuide(WIDTH, HEIGHT, PADDING, RADIUS, 60, (CENTERX, CENTERY))
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
    run_gui()
