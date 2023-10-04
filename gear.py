#!/usr/bin/env python
#gear.py

from utils import *
import pygame
import math

class Hole:
    def __init__(self, parent, center = (0, 0)):
        self.parent = parent
        self.center = center
        self.points = [center, center]
        self.direction = -1
        self.distance = calculate_distance(point1 = center, point2 = parent.center)
        self.color = random_color()

    def draw(self, surface, graph_surface):
        pygame.draw.circle(surface, (50, 255, 75), self.center, 4, 2)
        pygame.draw.line(graph_surface, self.color, self.points[0], self.points[1], 1)

    def rotate(self):
        angle_velocity = calculate_angular_velocity(point = self.center, center = self.parent.center, direction = self.direction)
        self.center = rotate_point_in_circle(center = self.parent.center, point = self.center, angle_velocity = angle_velocity)
        delta_x = self.center[0] - self.parent.center[0]
        delta_y = self.center[1] - self.parent.center[1]
        theta = math.atan2(delta_y, delta_x)
        new_x = self.parent.center[0] + self.distance * math.cos(theta)
        new_y = self.parent.center[1] + self.distance * math.sin(theta)
        self.center = (new_x, new_y)
        self.points.pop(0)
        self.points.append(self.center)

class SpiroGear:
    def __init__(self, parent, radius = 10, center = (0, 0), holes = []):
        # gear radius and center, parent center
        # gear movement speed and direction(1 = clockwise)
        self.parent = parent
        self.radius = radius
        self.center = center
        self.direction = 1
        self.holes = holes

    def add_random_holes(self, count = 1):
        for i in range(count):
            randomx = self.center[0] - (self.radius * rand() + 0.2) - 0.2
            hole_center = (randomx, self.center[1])
            hole_center = rotate_point_in_circle(center = self.center, point = hole_center, angle_velocity = 360 * rand())
            self.holes.append(Hole(self, center = hole_center))

    def add_holes(self, holes = [(0, 0),]):
        self.holes.extend(holes)

    def draw(self, surface, graph_surface):
        pygame.draw.circle(surface, (150, 30, 60), self.center, self.radius, 1)
        if len(self.holes) > 0:
            for hole in self.holes:
                hole.draw(surface, graph_surface)

    def rotate(self):
        angle_velocity = calculate_angular_velocity(point = self.center, center = self.parent.center, direction = self.direction)
        self.center = rotate_point_in_circle(center = self.parent.center, point = self.center, angle_velocity = angle_velocity)
        for hole in self.holes:
            hole.rotate()

