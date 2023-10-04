#!/usr/bin/env python
#guide.py

from utils import *
import pygame
import math
import gear


#pygame.init()
class SpiroGuide:
    def __init__(self, width, height, padding, radius, speed, center = (0, 0)):
        self.surface = pygame.display.set_mode((width, height))
        self.graph_surface = pygame.Surface((width, height), pygame.SRCALPHA)
        self.radius = radius - padding
        self.center = center
        self.gears = []
        self.speed = speed

    def add_gear(self, gear_radius, hole_count = 1):
        if hole_count not in range(1, 11):
            hole_count = 1
        gear_center = (self.center[0] - (self.radius - gear_radius), self.center[1])
        gear_center = rotate_point_in_circle(center = self.center, point = gear_center, angle_velocity = 360 * rand())
        self.gears.append(gear.SpiroGear(self, radius = gear_radius, center = gear_center))
        self.gears[-1].add_random_holes(hole_count)
        
    def draw(self):
        self.surface.fill((0, 0, 0))
        pygame.draw.circle(self.surface, (255, 255, 255), self.center, self.radius, 2)
        for gear in self.gears:
            gear.draw(self.surface, self.graph_surface)
        self.surface.blit(self.graph_surface, (0, 0))
        pygame.display.flip()

    def update(self):
        # spin(move) gear(s) then draw
        for gear in self.gears:
            gear.rotate()
        self.draw()

    def speed_change(self, value):
        if value == 'up':
            self.speed += 5
        elif value == 'down':
            self.speed -= 5
