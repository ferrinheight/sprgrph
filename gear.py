#!/usr/bin/env python
#gear.py

from utils import *
import pygame
import math


class Hole:
    """
    Represents a hole in a gear where the drawing utensil can be inserted.
    Handles its own position and drawing logic.
    """
    def __init__(self, parent, center=(0, 0)):
        self.parent = parent
        self.center = center
        self.points = [center, center]
        self.direction = -1
        self.distance = calculate_distance(point1=center, point2=parent.center)
        self.color = random_color()

    def draw(self, surface, graph_surface):
        """Draw the hole and its path on the given surfaces."""
        pygame.draw.circle(surface, (50, 255, 75), self.center, 4, 2)
        pygame.draw.line(graph_surface, self.color, self.points[0], self.points[1], 1)

    def rotate(self, old_center):
        """Update the hole's position as the gear rotates."""
        delta_x = self.parent.center[0] - old_center[0]
        delta_y = self.parent.center[1] - old_center[1]
        self.center = (self.center[0] + delta_x, self.center[1] + delta_y)
        angle_velocity = calculate_angular_velocity(point=self.center, center=self.parent.center, direction=self.direction)
        self.center = rotate_point_in_circle(center=self.parent.center, point=self.center, angle_velocity=angle_velocity)
        self.points.pop(0)
        self.points.append(self.center)


class SpiroGear:
    """
    Represents a spirograph gear that can contain multiple holes.
    Handles its own position, rotation, and drawing logic.
    """
    def __init__(self, parent, radius=10, center=(0, 0), holes=None):
        self.parent = parent
        self.radius = radius
        self.center = center
        self.direction = 1
        self.holes = holes if holes is not None else []

    def add_random_holes(self, count=1):
        """Add a number of randomly placed holes to the gear."""
        for _ in range(count):
            randomx = self.center[0] - randint(int(0.2 * self.radius), int(0.9 * self.radius))
            hole_center = (randomx, self.center[1])
            hole_center = rotate_point_in_circle(center=self.center, point=hole_center, angle_velocity=randint(0, 360))
            self.holes.append(Hole(self, center=hole_center))

    def add_holes(self, holes=None):
        """Add a list of holes to the gear."""
        if holes is None:
            return
        self.holes.extend(holes)

    def draw(self, surface, graph_surface):
        """Draw the gear and all its holes."""
        pygame.draw.circle(surface, (200, 200, 200), self.center, self.radius, 1)
        for hole in self.holes:
            hole.draw(surface, graph_surface)

    def rotate(self):
        """Rotate the gear and update all holes' positions."""
        angle_velocity = calculate_angular_velocity(point=self.center, center=self.parent.center, direction=self.direction)
        old_center = self.center
        self.center = rotate_point_in_circle(center=self.parent.center, point=self.center, angle_velocity=angle_velocity)
        for hole in self.holes:
            hole.rotate(old_center)


